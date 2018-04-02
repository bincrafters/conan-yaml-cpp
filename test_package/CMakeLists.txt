cmake_minimum_required(VERSION 2.8.11)
project(test_package)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(${PROJECT_NAME} main.cpp)
target_link_libraries(${PROJECT_NAME} ${CONAN_LIBS})

enable_testing()
add_test(NAME test-all
         COMMAND ${PROJECT_NAME}
			   WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
