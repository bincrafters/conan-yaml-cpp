[![Build Status](https://travis-ci.org/bincrafters/conan-yaml-cpp.svg?branch=release/0.5.3)](https://travis-ci.org/bincrafters/conan-yaml-cpp)
[![Build status](https://ci.appveyor.com/api/projects/status/x0dv3a3l6koq8j3a/branch/release/0.5.3?svg=true)](https://ci.appveyor.com/project/bincrafters/conan-yaml-cpp/branch/release/0.5.3)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# A YAML parser and emitter in C++

[Conan.io](https://conan.io) package for [yaml-cpp](https://github.com/jbeder/yaml-cpp) project

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/bincrafters/public-conan/yaml-cpp%3Abincrafters).

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py

If your are in Windows you should run it from a VisualStudio console in order to get "mc.exe" in path.

## Upload packages to server

    $ conan upload yaml-cpp/0.5.3@bincrafters/stable --all

## Reuse the packages

### Basic setup

    $ conan install yaml-cpp/0.5.3@bincrafters/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    yaml-cpp/0.5.3@bincrafters/stable

    [options]
    yaml-cpp:shared=True # False

    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install .

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.

### License
[MIT](LICENSE)
