#!/bin/bash

# === Configuration variables ===
PROFILE=profiles/linux-clang
BUILD_TYPE=Release
PRESET=linux-clang-release
OUT_DIR=build/${PRESET}

REM === Environment variables ===
set ENABLE_CLANG_TIDY=ON 
set ENABLE_CPPCHECK=ON

echo "Installing dependencies and generating toolchain for Linux (${BUILD_TYPE})..."
conan install . --output-folder=${OUT_DIR} --build=missing --profile:all=${PROFILE} -s build_type=${BUILD_TYPE}

echo "Configuring the project with CMake (${BUILD_TYPE})..."
cmake --preset ${PRESET}

echo "Building the project (${BUILD_TYPE})..."
cmake --build --preset ${PRESET}
