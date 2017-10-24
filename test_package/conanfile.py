"""Recipe validation for yaml-cpp-0.2.5
"""
import os
from conans import ConanFile, CMake


class TestYAMLCppConan(ConanFile):
    """Build test using target package and execute all tests
    """
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure(build_dir=os.getcwd())
        cmake.build()

    def imports(self):
        self.copy(pattern="*.so*", dst="bin", src="lib")
        self.copy(pattern="*.dll", dst="bin", src="bin")
        self.copy(pattern="*.dylib*", dst="bin", src="lib")

    def test(self):
        cmake = CMake(self)
        cmake.configure(build_dir=os.getcwd())
        cmake.test()
