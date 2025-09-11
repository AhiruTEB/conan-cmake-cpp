#pragma once

#include <string_view>

class Engine
{
    static constexpr std::string_view s_greeting = "Hello from the Engine!";

public:
    static constexpr auto greetings() -> std::string_view { return s_greeting; }
};
