"""Recipe validation for yaml-cpp-0.3.0
"""
from os import environ
from os import getenv
from conans import ConanFile, CMake


class TestYAMLCppConan(ConanFile):
    """Build test using target package and execute all tests
    """
    target = "yaml-cpp"
    name = "%s-test" % target
    version = "0.3.0"
    author = "Uilian Ries <uilianries@gmail.com>"
    license = "MIT"
    settings = "os", "compiler", "build_type", "arch"
    channel = getenv("CONAN_CHANNEL", "testing")
    user = getenv("CONAN_USERNAME", "uilianries")
    requires = "%s/%s@%s/%s" % (target, version, user, channel)
    generators = "cmake"

    def build(self):
        cmake = CMake(self.settings)
        cmake.configure(
            self, source_dir=self.conanfile_directory, build_dir="./")
        cmake.build(self)

    def imports(self):
        self.copy(pattern="lib%s.so*" % self.target, dst="bin", src="lib")
        self.copy(pattern="%s.dll" % self.target, dst="bin", src="bin")
        self.copy(pattern="lib%s*.dylib" % self.target, dst="bin", src="lib")

    def test(self):
        cmake = CMake(self.settings)
        cmake.configure(
            self, source_dir=self.conanfile_directory, build_dir="./")
        environ["CTEST_OUTPUT_ON_FAILURE"] = "TRUE"
        target = "RUN_TESTS" if self.settings.os == "Windows" else "test"
        cmake.build(self, target=target)
