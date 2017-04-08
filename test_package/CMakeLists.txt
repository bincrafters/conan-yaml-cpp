cmake_minimum_required(VERSION 2.8)

file(GLOB test_headers include/[a-z]*.h)
file(GLOB test_sources src/[a-z]*.cpp)
file(GLOB test_old_api_sources src/old-api/[a-z]*.cpp)

list(APPEND test_sources ${test_old_api_sources})
include_directories(include)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake) 
conan_basic_setup()

add_executable(run-tests ${test_sources} ${test_headers})
target_link_libraries(run-tests ${CONAN_LIBS})

enable_testing()
add_test(NAME yaml-reader-test 
         COMMAND run-tests
         WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
