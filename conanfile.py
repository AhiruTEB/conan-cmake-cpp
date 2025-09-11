from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout
from conan.tools.build import check_min_cppstd
from conan.tools.files import load
import json
import os
import re
import shutil

def get_version(conanfile):
    try:
        cmakelist = load(conanfile, "CMakeLists.txt")
        version = re.search("\sVERSION (.*)\s", cmakelist).group(1)
        return version.strip()
    except Exception as e:
        return None

class CraftGLConan(ConanFile):
    name = "{{PROJECT_NAME_LOWER}}"
    url = "{{PROJECT_HOMEPAGE_URL}}"
    description = "{{PROJECT_DESCRIPTION}}"
    license = ""
    settings = "os", "compiler", "build_type", "arch"

    def set_version(self):
        self.version = get_version(self)

    def validate(self):
        check_min_cppstd(self, "23")

#    def requirements(self):
#        self.requires("glm/1.0.1")

    def build_requirements(self):
        self.test_requires("gtest/1.16.0")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        
        if shutil.which("ccache") is not None:
            tc.variables["CMAKE_C_COMPILER_LAUNCHER"] = "ccache"
            tc.variables["CMAKE_CXX_COMPILER_LAUNCHER"] = "ccache"

        tc.cache_variables["ENABLE_CPPCHECK"] = os.environ.get("ENABLE_CPPCHECK", "ON")
        tc.cache_variables["ENABLE_CLANG_TIDY"] = os.environ.get("ENABLE_CLANG_TIDY", "ON")
        
        tc.generate()

        deps = CMakeDeps(self)
        deps.generate()

        self.apply_presets_extension()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def upgrade_cmakeuserpresets_version(self, version):
        cmakeuserpresets_file = os.path.join(self.source_folder, "CMakeUserPresets.json")

        if not os.path.exists(cmakeuserpresets_file):
            print(f"CMakeUserPresets.json file not found: {cmakeuserpresets_file}")
            return

        try:
            with open(cmakeuserpresets_file, 'r') as f:
                presets = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error parsing CMakeUserPresets.json: {e}")
            return

        presets['version'] = version

        try:
            with open(cmakeuserpresets_file, 'w') as f:
                json.dump(presets, f, indent=4)
            print(f"Updated CMakeUserPresets.json version to {presets['version']}.")
        except IOError as e:
            print(f"Error writing to CMakeUserPresets.json: {e}")

    def apply_presets_extension(self):
        extension_file = os.path.join(self.source_folder, "conan/PresetsExtension.json")
        generated_file = os.path.join(self.build_folder, "generators/CMakePresets.json")

        # Check files exist
        if not os.path.exists(generated_file):
            print(f"Generated presets file not found: {generated_file}")
            return

        if not os.path.exists(extension_file):
            print(f"Presets extension file not found: {extension_file}")
            return

        # Read generated presets to json
        try:
            with open(generated_file, 'r') as f:
                presets = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error parsing generated presets file: {e}")
            return

        # Read extension presets as a text file
        try:
            with open(extension_file, 'r') as f:
                extension_content = f.read()
        except FileNotFoundError as e:
            print(f"Error reading extension file: {e}")
            return

        # Find preset name in generated file
        preset_name = None
        if configure_presets := presets.get('configurePresets'):
            preset_name = configure_presets[0].get('name') # Assuming all the presets have the same name

            if not preset_name:
                print("Could not determine preset name from generated file. No configure presets found.")
                # We can still proceed to merge, just without placeholder replacement
                pass
        
        # Replace placeholder in extension file if preset_name is found
        if preset_name:
            print(f"Replacing '${{preset_name}}' with '{preset_name}' in extension presets.")
            extension_content = extension_content.replace('${preset_name}', preset_name)

        # Finally load the extension text file as JSON
        try:
            extension_presets = json.loads(extension_content)
        except json.JSONDecodeError as e:
            print(f"Error parsing extension file after placeholder replacement: {e}")
            return
        
        # Upgrade version in generated preset files to support extension presets (must have higher version than generated ones)
        version = extension_presets['version']
        presets['version'] = version
        self.upgrade_cmakeuserpresets_version(version)

        # Merge extension presets into generated ones
        for key in ['configurePresets', 'buildPresets', 'testPresets', 'packagePresets', 'workflowPresets']:
            if key in extension_presets:
                if key not in presets:
                    presets[key] = []
                print(f"Merging {len(extension_presets[key])} preset(s) into '{key}'...")
                presets[key].extend(extension_presets[key])

        # Write the updated presets back to the generated file
        with open(generated_file, 'w') as f:
            json.dump(presets, f, indent=4)
        
        print("Successfully merged presets from extension file.")