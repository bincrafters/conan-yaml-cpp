#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class YAMLCppConan(ConanFile):
    name = "yaml-cpp"
    version = "0.6.2"
    url = "https://github.com/uilianries/conan-yaml-cpp"
    homepage = "https://github.com/jbeder/yaml-cpp"
    description = "A YAML parser and emitter in C++"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "MIT"
    exports = "LICENSE.md"
    exports_sources = "CMakeLists.txt"
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = "shared=False", "fPIC=True"
    source_subfolder = "source_subfolder"

    def source(self):
        tools.get("{0}/archive/{1}-{2}.tar.gz".format(self.homepage, self.name, self.version))
        extracted_dir = self.name + "-" + self.name + "-" + self.version
        os.rename(extracted_dir, self.source_subfolder)

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["YAML_CPP_BUILD_TESTS"] = False
        cmake.definitions["YAML_CPP_BUILD_CONTRIB"] = True
        cmake.definitions["YAML_CPP_BUILD_TOOLS"] = False
        if self.settings.compiler == "Visual Studio":
            cmake.definitions["MSVC_SHARED_RT"] = "MT" in self.settings.compiler.runtime
        cmake.configure()
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self.source_subfolder)
        cmake = self.configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.includedirs = ["yaml-cpp", ]
        self.cpp_info.libs = tools.collect_libs(self)
        self.cpp_info.stdcpp = 11
