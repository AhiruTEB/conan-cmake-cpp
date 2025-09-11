cmake_minimum_required(VERSION 3.23)

project(craftgl
    VERSION 0.1.0 
    DESCRIPTION "A simple OpenGL game project."
    HOMEPAGE_URL "http://example.com"
    LANGUAGES CXX)

# Enable export of compile commands for tools like clang-tidy
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

include(cmake/StaticAnalysis.cmake)

option(ENABLE_TESTS "Enable building tests" ON)

# --- Find required packages ---
find_package(opengl_system REQUIRED)
find_package(glu REQUIRED)
find_package(Microsoft.GSL REQUIRED)
find_package(glm REQUIRED)

# --- Create executable ---
add_executable(craftgl)

# --- Subdirectories ---
add_subdirectory(src)

# --- Tests ---
if(ENABLE_TESTS)
    message(STATUS "Building tests is enabled. Set ENABLE_TESTS to OFF to disable it.")
    find_package(GTest REQUIRED)
    enable_testing()
    add_subdirectory(tests)
else()
    message(STATUS "Building tests is disabled.")
endif()

# --- Installation  ---
install(TARGETS ${PROJECT_NAME} DESTINATION bin)

# --- Packaging  ---
set(CPACK_PACKAGE_NAME "${PROJECT_NAME}")
set(CPACK_PACKAGE_VERSION "${PROJECT_VERSION}")
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "${PROJECT_DESCRIPTION}")
set(CPACK_PACKAGE_HOMEPAGE_URL "${PROJECT_HOMEPAGE_URL}")
set(CPACK_PACKAGE_CONTACT "norbert221198@gmail.com")
set(CPACK_DEBIAN_PACKAGE_DEPENDS "libgl-dev, libgl1-mesa-dev, libglu1-mesa-dev")

include(CPack)

# clangd support
add_custom_command(
    TARGET craftgl POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy_if_different
            "${CMAKE_BINARY_DIR}/compile_commands.json"
            "${CMAKE_SOURCE_DIR}/compile_commands.json"
    COMMENT "Copying compile_commands.json for clangd"
)
