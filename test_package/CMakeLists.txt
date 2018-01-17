<<<<<<< HEAD
cmake_minimum_required(VERSION 2.8)
project(test-package)
=======
cmake_minimum_required(VERSION 2.8.11)
project(test_package)
>>>>>>> testing/0.2.5

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(${PROJECT_NAME} main.cpp)
target_link_libraries(${PROJECT_NAME} ${CONAN_LIBS})
<<<<<<< HEAD

enable_testing()
add_test(NAME test-all
         COMMAND ${PROJECT_NAME}
			   WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
=======
>>>>>>> testing/0.2.5
