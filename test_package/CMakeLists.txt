cmake_minimum_required(VERSION 2.8)
project(test-package)

file(GLOB test_headers include/[a-z]*.h)
file(GLOB test_sources src/[a-z]*.cpp)
file(GLOB test_old_api_sources src/old-api/[a-z]*.cpp)

list(APPEND test_sources ${test_old_api_sources})
include_directories(include)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

if(CMAKE_COMPILER_IS_GNUCXX)
    set(CMAKE_CXX_FLAGS "-Wno-deprecated-declarations ${CMAKE_CXX_FLAGS}")
endif()

add_executable(${CMAKE_PROJECT_NAME} ${test_sources} ${test_headers})
target_link_libraries(${CMAKE_PROJECT_NAME} ${CONAN_LIBS})

enable_testing()
add_test(NAME yaml-reader-test
         COMMAND ${CMAKE_PROJECT_NAME}
         WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
