"""This script build Conan.io package to multiple platforms."""
from platform import system
from os import getenv
from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.password = getenv("CONAN_PASSWORD")
    builder.add_common_builds(shared_option_name="yaml-cpp:shared", pure_c=False)
    if system() == "Linux":
        stdlibcpp11_builds = []
        for settings, options in builder.builds:
            settings["compiler.libcxx"] = "libstdc++"
            if settings["compiler.version"] > "4.9":
                _settings = dict(settings)
                _settings["compiler.libcxx"] = "libstdc++11"
                stdlibcpp11_builds.append([_settings, options])
        builder.builds = builder.builds + stdlibcpp11_builds
    elif system() == "Windows":
        windows_builds = []
        for settings, options in builder.builds:
            if not options["yaml-cpp:shared"] or not settings["compiler"] == "Visual Studio":
                windows_builds.append([settings, options])
        builder.builds = windows_builds
    builder.run()
