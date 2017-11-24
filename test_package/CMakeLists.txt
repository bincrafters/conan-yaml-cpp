cmake_minimum_required(VERSION 2.8)
project(test-package)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(${CMAKE_PROJECT_NAME} main.cpp)
target_link_libraries(${CMAKE_PROJECT_NAME} ${CONAN_LIBS})

enable_testing()
add_test(NAME yaml-reader-test
         COMMAND ${CMAKE_PROJECT_NAME}
         WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
