#include <engine/Engine.hpp>

#include <gtest/gtest.h> // Include the Google Test header

#include <string_view>

// Define a test fixture if you need common setup/teardown for multiple tests
// For example, if your Engine needs to be initialized before each test:
class EngineTest : public ::testing::Test
{
protected:
    void SetUp() override {}

    void TearDown() override {}
};

TEST( EngineTest, Initialization ) { EXPECT_EQ( std::ssize( Engine::greetings() ), 22 ); }
