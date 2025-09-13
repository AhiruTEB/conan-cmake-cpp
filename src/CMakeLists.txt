add_subdirectory(engine)

# ----------------------------------------------------------------------------
set(GAME_SOURCES
    main.cpp
)

set(GAME_HEADERS
)

target_sources(${CMAKE_PROJECT_NAME} PRIVATE ${GAME_SOURCES} ${GAME_HEADERS})
target_compile_features(${PROJECT_NAME} PRIVATE cxx_std_23)
target_include_directories(${CMAKE_PROJECT_NAME} PRIVATE "${CMAKE_CURRENT_BINARY_DIR}")
target_link_libraries(${PROJECT_NAME} PRIVATE ${PROJECT_NAME}::engine)
