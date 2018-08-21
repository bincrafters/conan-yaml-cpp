#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class YAMLCppConan(ConanFile):
    name = "yaml-cpp"
    version = "0.5.3"
    url = "https://github.com/uilianries/conan-yaml-cpp"
    homepage = "https://github.com/jbeder/yaml-cpp"
    author = "Bincrafters <bincrafters@gmail.com>"
    description = "A YAML parser and emitter in C++"
    author = "Uilian Ries <uilianries@gmail.com>"
    license = "MIT"
    exports = "LICENSE.md"
    exports_sources = "CMakeLists.txt"
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = "shared=False", "fPIC=True"
    requires = "boost/1.66.0@conan/stable"

    def config_options(self):
        if self.settings.os == 'Windows':
            self.options.remove("fPIC")

    def source(self):
        tools.get("{0}/archive/release-{1}.tar.gz".format(self.homepage, self.version))
        extracted_dir = self.name + "-release-" + self.version
        os.rename(extracted_dir, "sources")

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["YAML_CPP_BUILD_CONTRIB"] = True
        cmake.definitions["YAML_CPP_BUILD_TOOLS"] = False
        if self.settings.os == "Windows" and self.options.shared:
            cmake.definitions["BUILD_SHARED_LIBS"] = True
        cmake.configure()
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE", dst=".", src="sources")
        cmake = self.configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
