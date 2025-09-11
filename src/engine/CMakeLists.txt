set(ENGINE_SOURCE
    Engine.cpp
)

set(ENGINE_HEADERS
    Engine.hpp
)

add_library(engine STATIC)
target_sources(engine PRIVATE ${ENGINE_SOURCE} ${ENGINE_HEADERS})
target_compile_features(engine PUBLIC cxx_std_23)
target_include_directories(engine PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}/..")
target_link_libraries(engine PUBLIC Microsoft.GSL::GSL)

add_library(${PROJECT_NAME}::engine ALIAS engine)