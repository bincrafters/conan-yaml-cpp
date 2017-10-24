"""Conan recipe for YAML Cpp
"""
from os import path
from conans import ConanFile, CMake, tools


class YAMLCppConan(ConanFile):
    """Download YAML Cpp, build and create package
    """
    name = "yaml-cpp"
    version = "0.2.5"
    generators = "cmake", "txt"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    url = "https://github.com/uilianries/conan-yaml-cpp"
    author = "Uilian Ries <uilianries@gmail.com>"
    license = "MIT"
    description = "A YAML parser and emitter in C++"
    release_name = "%s-release-%s" % (name, version)

    def configure(self):
        if self.settings.os == "Windows" and self.settings.compiler == "Visual Studio" and self.options.shared:
            raise Exception("YAML Cpp 0.2.5 is only supported as -static for MSVC")

    def source(self):
        tools.get("https://github.com/jbeder/yaml-cpp/archive/release-0.2.5.tar.gz")

    def build(self):
        self._inject_conan()
        self._build()

    def _build(self):
        cmake = CMake(self)
        cmake.definitions["YAML_CPP_BUILD_TOOLS"] = False
        if self.settings.os == "Windows" and self.options.shared:
            cmake.definitions["CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS"] = True
        cmake.configure(source_dir=self.release_name)
        cmake.build()

    def _inject_conan(self):
        conan_magic_lines = '''
        project (YAML_CPP)
        include(../conanbuildinfo.cmake)
        conan_basic_setup()
        '''
        tools.replace_in_file("%s/CMakeLists.txt" % self.release_name,
                        "project (YAML_CPP)", conan_magic_lines)

    def package(self):
        self.copy(
            pattern="*.h",
            dst="include",
            src=path.join(self.release_name, "include"))
        self.copy(
            pattern="lib%s.a" % self.name,
            dst="lib",
            src="lib",
            keep_path=False)
        self.copy(pattern="lib%s.so*" % self.name, dst="lib", keep_path=False)
        self.copy(
            pattern="lib%s*.dylib" % self.name, dst="lib", keep_path=False)
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
