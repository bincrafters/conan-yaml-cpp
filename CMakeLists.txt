cmake_minimum_required(VERSION 2.8)
project(conan-yaml-cpp)

include("${CMAKE_BINARY_DIR}/conanbuildinfo.cmake")
conan_basic_setup()

if(MSVC)
  add_definitions("-D_NOEXCEPT=noexcept")
endif()

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_subdirectory(source_subfolder)
