cmake_minimum_required( VERSION 3.23 )

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                              Project  Settings                              #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
project( EXAMPLE )
set( CMAKE_CXX_STANDARD 23 )

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                               CMake  Includes                               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
include( cmake/CMakeSettings.cmake )
include( CompilerOptions )
include( NinjaColorFix )

include( ExternalProject )
include( CTest )

add_subdirectory( src )

include( Install )

include( CPackConfig )
include( CPack )

add_executable( NAME
    ./Source1.cpp
    ./Source2.cpp
    ./Source3.cpp
    ./Source4.cpp
    ./Source5.cpp
    ./Source6.cpp
    ./Source7.cpp
    ./Source8.cpp
    ./Source9.cpp
    ./Source10.cpp
    ./Source11.cpp
    ./Source12.cpp
    ./Source13.cpp
    ./Source14.cpp
    ./Source15.cpp
    ./Source16.cpp
)

