function(add_test_target test_name test_sources test_libraries)
    set(target_name "${test_name}_test")

    set(src_abs_paths "")
    foreach(src ${test_sources})
        list(APPEND src_abs_paths "${CMAKE_SOURCE_DIR}/src/${src}")
    endforeach()

    add_executable(${target_name} ${target_name}.cpp ${src_abs_paths})

    target_compile_features(${target_name} PRIVATE cxx_std_23)
    target_include_directories(${target_name} PRIVATE "${CMAKE_SOURCE_DIR}/src")
    target_link_libraries(${target_name} PRIVATE GTest::gtest_main ${test_libraries})

    add_test(NAME ${test_name} COMMAND ${target_name} WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}")
endfunction()

add_test_target(engine "engine/Engine.cpp" "")
