# Building and Running the Project (Conan 2.x with CMake Presets)

This document provides instructions for building and running the project using **Conan 2.x** and **CMake Presets**. This approach simplifies the build process.

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
sudo apt install conan cmake ninja-build clang clang-format clang-tidy
```

### Step-by-Step Instructions
There are also scripts that run generation phase accordingly for Windows system `configure.cmd` and for Linux `configure.sh`.

#### 1. Generate the Conan Toolchain and Dependencies
This step uses Conan to download all project dependencies and generate the conan_toolchain.cmake file that CMake needs. This is an example, parameters like profile used or build type can be changed.

* **Windows**:
```batch
conan install . -pr:a=profiles/windows-clang -s build_type=Release --build=missing
```

* **Linux**:
```bash
conan install . -pr:a=profiles/linux-clang -s build_type=Release --build=missing
```

This command will create the build directory and populate it with Conan's toolchain file and other necessary configuration. Also `CMakeUserPresets.json` and `compile_commands.json` files will be generated.

#### 2. Build the Project

Once the project is configured, you can build it using the same profile. This is an example, parameters like profile used or build type can be changed.

* **Windows**:
```
conan build . -pr:a=%PROFILE% -s build_type=Release --build=missing 
```

* **Linux**:
```
conan build . -pr:a=%PROFILE% -s build_type=Release --build=missing 
```

This will compile your source code and produce the final executable.

#### 3. Run the Executable

The executable is located inside the build directory. The exact path to the executable will depend on choosen profile and build type.

```
./build/{compiler-compiler_version-arch"}/{{PROJECT_NAME_LOWER}}.exe
```