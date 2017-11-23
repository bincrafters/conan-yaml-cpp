"""Conan recipe for YAML Cpp
"""
import os
from conans import ConanFile, CMake, tools


class YAMLCppConan(ConanFile):
    """Download YAML Cpp, build and create package
    """
    name = "yaml-cpp"
    version = "0.2.5"
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    url = "https://github.com/uilianries/conan-yaml-cpp"
    author = "Uilian Ries <uilianries@gmail.com>"
    license = "https://github.com/jbeder/yaml-cpp/blob/master/LICENSE"
    description = "A YAML parser and emitter in C++"
    exports_sources = "CMakeLists.txt"
    exports = "LICENSE"
    release_name = "%s-release-%s" % (name, version)

    def configure(self):
        if self.settings.os == "Windows" and self.settings.compiler == "Visual Studio" and self.options.shared:
            raise Exception("YAML Cpp 0.2.5 is only supported as -static for MSVC")

    def source(self):
        source_url = "https://github.com/jbeder/yaml-cpp"
        tools.get("{0}/archive/release-{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-release-" + self.version
        os.rename(extracted_dir, "sources")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["YAML_CPP_BUILD_TOOLS"] = False
        if self.settings.os == "Windows" and self.options.shared:
            cmake.definitions["CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS"] = True
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE", dst=".", src=os.path.join("source", "LICENSE"))
        self.copy(
            pattern="*.h",
            dst="include",
            src=os.path.join("sources", "include"))
        self.copy(
            pattern="lib%s.a" % self.name,
            dst="lib",
            src="lib",
            keep_path=False)
        self.copy(
            pattern="lib%s.so*" % self.name,
            dst="lib",
            src="lib",
            keep_path=False)
        self.copy(
            pattern="lib%s*.dylib" % self.name,
            dst="lib",
            src="lib",
            keep_path=False)
        self.copy(
            pattern="*%s*.lib" % self.name,
            dst="lib",
            src="lib")
        self.copy(
            pattern="%s.dll" % self.name,
            dst="bin",
            src="bin")

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
