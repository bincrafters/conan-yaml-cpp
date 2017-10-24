"""This script build Conan.io package to multiple platforms."""
from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds(shared_option_name="yaml-cpp:shared", pure_c=False)
    builder.run()
