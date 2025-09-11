#!/bin/bash

# === Configuration variables ===
PROFILE=profiles/linux-clang

# === Release ===
conan install . -pr:a=$PROFILE -s build_type=Release --build=missing
conan build . -pr:a=$PROFILE -s build_type=Release --build=missing 

# === Debug ===
# conan install . -pr:a=$PROFILE -s build_type=Debug --build=missing
# conan build . -pr:a=$PROFILE -s build_type=Debug --build=missing