cmake_minimum_required(VERSION 2.8)
project(test-package)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

<<<<<<< HEAD
add_executable(${PROJECT_NAME} main.cpp)
target_link_libraries(${PROJECT_NAME} ${CONAN_LIBS})

enable_testing()
add_test(NAME test-all
         COMMAND ${PROJECT_NAME}
			   WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
=======
add_executable(${CMAKE_PROJECT_NAME} main.cpp)
target_link_libraries(${CMAKE_PROJECT_NAME} ${CONAN_LIBS})

enable_testing()
add_test(NAME yaml-reader-test
         COMMAND ${CMAKE_PROJECT_NAME}
         WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
>>>>>>> testing/0.3.0
