#include <engine/Engine.hpp>

#include <exception>
#include <print>

auto main() -> int
{
    enum ErrorMessages
    {
        Success,
        StandardException,
        UnknownException,
        ErrorMessagePrintFailure,
    };

    try
    {
        try
        {
            std::println( "Hello World!" );
            std::print( "Engine says: {}\n", Engine::greetings() );
            return ErrorMessages::Success;
        }
        catch( const std::exception& e )
        {
            std::println( "Caught standard exception: {}", e.what() );
            return ErrorMessages::StandardException;
        }
        catch( ... )
        {
            std::println( "Caught unknown exception." );
            return ErrorMessages::UnknownException;
        }
    }
    catch( ... )
    {
        return ErrorMessages::ErrorMessagePrintFailure;
    }
}
