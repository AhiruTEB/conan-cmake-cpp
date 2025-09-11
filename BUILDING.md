# Building and Running the Project (Conan 2.x with CMake Presets)

This document provides instructions for building and running the project using **Conan 2.x** and **CMake Presets**. This approach simplifies the build process by defining all build configurations in a single `CMakePresets.json` file.

### Prerequisites

You must have the following tools installed and available in your system's PATH:

#### Versions
* Conan: 2.x or newer
* CMake: 3.20 or newer
* LLVM: 18 or newer (for full C++23 support, including std::print)

#### Commands
* **Windows**: 
```batch
choco install conan cmake ninja llvm
```

* **Linux**:
```bash
sudo apt install conan cmake ninja-build clang clang-format clang-tidy libglu1-mesa-dev freeglut3-dev
```

### Step-by-Step Instructions
TODO: There are also scripts that run generation phase accordingly for Windows system `configure.cmd` script and for Linux `configure.sh`.

#### 1. Generate the Conan Toolchain and Dependencies
This step uses Conan to download all project dependencies and generate the conan_toolchain.cmake file that CMake needs.

* **Windows**:
```batch
conan install . --output-folder=build/windows-clang-release --build=missing -pr:h=profiles/windows-clang -pr:b=profiles/windows-clang
```

* **Linux**:
```bash
conan install . --output-folder=build/linux-clang-release --build=missing -pr:h=profiles/linux-clang -pr:b=profiles/linux-clang
```

This command will create the build directory and populate it with Conan's toolchain file and other necessary configuration.

#### 2. Configure the Project

The `cmake --preset` command will automatically resolve and install all project dependencies using Conan. It will create a build directory and generate the necessary files for building.

* **Windows**:
```batch
cmake --preset windows-clang-release
```

* **Linux**:
```bash
cmake --preset linux-clang-release
```

After this command, a new directory, `build/linux-clang-release` or `build/windows-clang-release`, will be created containing the build configuration.

#### 2. Build the Project

Once the project is configured, you can build it using the same preset name.

* **Linux**:
```
cmake --build --preset linux-clang-release
```

* **Windows**:
```
cmake --build --preset windows-clang-release
```

This will compile your source code and produce the final executable.

#### 3. Run the Executable

The executable is located inside the build directory. The exact name of the executable will depend on your `CMakeLists.txt` configuration.

* **Linux**:
```
./build/linux-clang-release/your_executable_name
```

* **Windows**:
```
`./build/windows-clang-release/your_executable_name.exe
```

### How It Works

The `cmake --preset` command is the key to this workflow. It tells CMake to:

1. Read the configuration specified in the `CMakePresets.json` file.

2. Automatically invoke Conan to download all the dependencies defined in your `conanfile.py`.

3. Set up the build environment with Conan's toolchain file, ensuring that the compiler, C++ standard, and other settings are correctly configured for your chosen preset.

This eliminates the need to run manual `conan install` and `cmake -DCMAKE_TOOLCHAIN_FILE=...` commands separately, creating a single, consistent entry point for building your project.