Build Systems Benchmarks
===========================================

Build system speed tests. 1,000 C files spread over 10 directories.

Please notify/fork if you find any bugs or misinformation. Please add
more tests for other build systems.

Build systems tested:
===========================================
* [GNU Make](http://www.gnu.org/software/make/)
* [CMake](http://www.cmake.org/)
* [Raise](https://launchpad.net/raise)
* [Waf](http://code.google.com/p/waf/)

Coming soon?:
===========================================
* [Ninja](http://martine.github.io/ninja/)
* [Tup](http://gittup.org/tup/)
* [Redo](https://github.com/apenwarr/redo)
* [Rake](http://rake.rubyforge.org/)
* [SCons](http://www.scons.org/)
* [Maven](http://maven.apache.org/)
* [Gradle](http://www.gradle.org/)
* [GYP](https://code.google.com/p/gyp/)

* * *

Instructions:
===========================================
In the generate_code.py file:

DIR_COUNT - Number of directories to generate.

LIB_COUNT - Number of libraries to generate in each directory.

TOOLS_TO_TEST - List of tools to benchmark.

* * *


Results:
===========================================
    Starting benchmark with 10 directories containing 100 files each ...
    Generating code ...
    CMake benchmark ...
        clean time      : 0:00:55
        incremental time: 0:00:03
    Waf benchmark ...
        clean time      : 0:00:49
        incremental time: 0:00:05
    Raise benchmark ...
        clean time      : 0:01:02
        incremental time: 0:00:02
    Make benchmark ...
        clean time      : 0:00:39
        incremental time: 0:00:05



