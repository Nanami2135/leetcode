cmake_minimum_required(VERSION 3.16)
project(leetcode_cpp LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

file(GLOB PROBLEM_SOURCES CONFIGURE_DEPENDS "${CMAKE_SOURCE_DIR}/problems/*.cpp")

foreach(src ${PROBLEM_SOURCES})
    get_filename_component(name ${src} NAME_WE)
    add_executable(${name} ${src})

    target_compile_options(${name} PRIVATE
        -Wall -Wextra -Wpedantic
    )
endforeach()
