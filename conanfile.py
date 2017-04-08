"""Conan recipe for YAML Cpp
"""
from os import unlink
from os.path import join
from conans import ConanFile
from conans import CMake
from conans.tools import download
from conans.tools import unzip
from conans.tools import check_md5
from conans.tools import replace_in_file


class YAMLCppConan(ConanFile):
    """Download YAML Cpp, build and create package
    """
    name = "yaml-cpp"
    version = "0.3.0"
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
            raise Exception("YAML Cpp 0.3.0 is only supported as -static for MSVC")

    def source(self):
        tar_name = "release-%s.tar.gz" % self.version
        download("https://github.com/jbeder/yaml-cpp/archive/%s" % tar_name,
                 tar_name)
        check_md5(tar_name, "0c0496b195299e956056430444e237b9")
        unzip(tar_name)
        unlink(tar_name)

    def build(self):
        self.__inject_conan()
        self.__disable_warnings()
        definitions = {
            "BUILD_SHARED_LIBS": self.options.shared,
            "YAML_CPP_BUILD_CONTRIB": True,
            "YAML_CPP_BUILD_TOOLS": False
        }
        if self.settings.os == "Windows" and self.options.shared:
            definitions["CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS"] = True
        cmake = CMake(self.settings)
        cmake.configure(self, source_dir=self.release_name, defs=definitions)
        cmake.build(self)

    def __inject_conan(self):
        conan_magic_lines = '''
        project(YAML_CPP)
        include(../conanbuildinfo.cmake)
        conan_basic_setup()
        '''
        replace_in_file("%s/CMakeLists.txt" % self.release_name,
                        "project(YAML_CPP)", conan_magic_lines)

    def __disable_warnings(self):
        conan_magic_lines = '''
        set(GCC_EXTRA_OPTIONS "")
        set(CMAKE_CXX_FLAGS "-Wno-deprecated-declarations ${CMAKE_CXX_FLAGS}")
        '''
        replace_in_file("%s/CMakeLists.txt" % self.release_name,
                        'set(GCC_EXTRA_OPTIONS "")', conan_magic_lines)

    def package(self):
        self.copy(
            pattern="*.h",
            dst="include",
            src=join(self.release_name, "include"))
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
        lib_name = self.name
        if self.settings.os == "Windows" and not self.options.shared:
            lib_name = "lib%smd" % self.name
            if self.settings.build_type == "Debug":
                lib_name += "d"
        self.cpp_info.libs = [lib_name]
