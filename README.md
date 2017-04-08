[![Build Status](https://travis-ci.org/uilianries/conan-yaml-cpp.svg?branch=release/0.3.0)](https://travis-ci.org/uilianries/conan-yaml-cpp) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# A YAML parser and emitter in C++

[Conan.io](https://conan.io) package for [yaml-cpp](https://github.com/jbeder/yaml-cpp) project

The packages generated with this **conanfile** can be found in [conan.io](https://conan.io/source/yaml-cpp/0.3.0/uilianries/stable).

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py

If your are in Windows you should run it from a VisualStudio console in order to get "mc.exe" in path.
    
## Upload packages to server

    $ conan upload yaml-cpp/0.3.0@uilianries/stable --all
    
## Reuse the packages

### Basic setup

    $ conan install yaml-cpp/0.3.0@uilianries/stable
    
### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*
    
    [requires]
    yaml-cpp/0.3.0@uilianries/stable

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
