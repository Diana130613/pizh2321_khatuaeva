cmake_minimum_required(VERSION 4.0.1)
project(labwork1 VERSION 0.1.0)

add_executable(
    labwork1
    src/main.cpp
    src/WordCount.cpp
)

include_directories(src)
