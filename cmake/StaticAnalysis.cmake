option(ENABLE_CLANG_TIDY "Enable Clang-Tidy for static analysis" ON)
option(ENABLE_CPPCHECK "Enable Cppcheck for static analysis" ON)

if(ENABLE_CLANG_TIDY)
    message(STATUS "Clang-Tidy is enabled for static analysis.")
    
    # Find the clang-tidy executable.
    find_program(CLANG_TIDY clang-tidy)
    
    if(CLANG_TIDY)
        message(STATUS "Found clang-tidy: ${CLANG_TIDY}")

        set(CLANG_TIDY_ARGS "--config-file=${CMAKE_SOURCE_DIR}/.clang-tidy")
        if(WIN32 AND CMAKE_CXX_COMPILER_ID MATCHES "MSVC|Clang")
            list(APPEND CLANG_TIDY_ARGS "--extra-arg=/EHsc")
        endif()
        
        set(CMAKE_CXX_CLANG_TIDY ${CLANG_TIDY} ${CLANG_TIDY_ARGS})
    else()
        message(WARNING "Clang-tidy not found. Static analysis will not be performed during compilation.")
    endif()
else()
    message(STATUS "Clang-Tidy is disabled. Set ENABLE_CLANG_TIDY to ON to enable it.")
endif()

if(ENABLE_CPPCHECK)
    message(STATUS "Cppcheck is enabled for static analysis.")

    # Find the cppcheck executable.
    find_program(CPPCHECK cppcheck)
    
    if(CPPCHECK)
        message(STATUS "Found cppcheck: ${CPPCHECK}")
        file(MAKE_DIRECTORY ${CMAKE_BINARY_DIR}/cppcheck)

        add_custom_target(static_analysis_cppcheck ALL
            COMMAND ${CPPCHECK}
                    --cppcheck-build-dir=${CMAKE_BINARY_DIR}/cppcheck
                    --project=${CMAKE_BINARY_DIR}/compile_commands.json
                    --enable=all
                    --inconclusive
                    --std=c++23
                    --suppress=missingIncludeSystem
            COMMENT "Running cppcheck analysis on the entire project..."
        )

        add_dependencies(static_analysis_cppcheck craftgl)
    else()
        message(WARNING "Cppcheck not found. Static analysis target for cppcheck will be not created nor run.")
    endif()
else()
    message(STATUS "Cppcheck is disabled. Set ENABLE_CPPCHECK to ON to enable it.")
endif()