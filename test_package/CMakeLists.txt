cmake_minimum_required(VERSION 2.8)
project(test-package CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

file(GLOB test_headers [a-z]*.h)
file(GLOB test_sources [a-z]*.cpp)

add_executable(${PROJECT_NAME}
	${test_sources}
	${test_headers}
)
target_link_libraries(${PROJECT_NAME} yaml-cpp)

enable_testing()
add_test(NAME test-all
         COMMAND ${PROJECT_NAME}
			 WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
