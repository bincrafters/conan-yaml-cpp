#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class YAMLCppConan(ConanFile):
    name = "yaml-cpp"
    version = "0.6.2"
    url = "https://github.com/uilianries/conan-yaml-cpp"
    description = "A YAML parser and emitter in C++"
    author = "Uilian Ries <uilianries@gmail.com>"
    license = "MIT"
    exports = "LICENSE.md"
    exports_sources = "CMakeLists.txt"
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = "shared=False"

    def source(self):
        source_url = "https://github.com/jbeder/yaml-cpp"
        tools.get("{0}/archive/yaml-cpp-{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-" + self.name + "-" + self.version
        os.rename(extracted_dir, "sources")

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["YAML_CPP_BUILD_TESTS"] = False
        cmake.definitions["YAML_CPP_BUILD_CONTRIB"] = True
        cmake.definitions["YAML_CPP_BUILD_TOOLS"] = False
        cmake.definitions["BUILD_SHARED_LIBS"] = self.options.shared
        if self.settings.compiler == "Visual Studio":
            cmake.definitions["MSVC_SHARED_RT"] = "MT" in self.settings.compiler.runtime
        cmake.configure()
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def install(self):
        cmake = self.configure_cmake()
        cmake.install()

    def package(self):
        self.copy(pattern="LICENSE", dst=".", src="sources")
        self.copy(pattern="*.h", dst="include", src=os.path.join("sources", "include"))
        self.copy(pattern="lib%s.a" % self.name, dst="lib", src="lib", keep_path=False)
        self.copy(pattern="lib%s.so*" % self.name, dst="lib", src="lib", keep_path=False)
        self.copy(pattern="lib%s*.dylib" % self.name, dst="lib", src="lib", keep_path=False)
        self.copy(pattern="*%s*.lib" % self.name, dst="lib", src="lib", keep_path=False)
        self.copy(pattern="%s.dll" % self.name, dst="bin", src="bin", keep_path=False)

    def package_info(self):
        self.cpp_info.includedirs = ["yaml-cpp", ]
        self.cpp_info.libs = tools.collect_libs(self)
        self.cpp_info.stdcpp = 11
