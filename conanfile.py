#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class YAMLCppConan(ConanFile):
    name = "yaml-cpp"
    version = "0.2.5"
    url = "https://github.com/bincrafters/conan-yaml-cpp"
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
    build_subfolder = "build_subfolder"

    def source(self):
        tools.get("{0}/archive/release-{1}.tar.gz".format(self.homepage, self.version))
        extracted_dir = self.name + "-release-" + self.version
        os.rename(extracted_dir, self.source_subfolder)

    def config_options(self):
        if self.settings.os == "Windows":
            self.options.remove("fPIC")

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["YAML_CPP_BUILD_TOOLS"] = False
        if self.settings.os == "Windows":
            cmake.definitions["CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS"] = self.options.shared
        cmake.configure(build_folder=self.build_subfolder)
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="license.txt", dst="licenses", src=self.source_subfolder)
        cmake = self.configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        self.cpp_info.includedirs.append(os.path.join("include", "yaml-cpp"))
