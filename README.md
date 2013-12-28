Build Systems Benchmarks
===========================================

Build system speed tests. 10,000 C files spread over 100 directories.

Build systems tested:
===========================================
* GNU Make
* CMake
* Raise

Comming soon:
===========================================
* Ninja
* Waf
* Tup
* Redo
* Rake
* SCons
* Maven


* * *


Results:
===========================================
GNU Make:
------------------------------------------
    first build: 51m25.352s, 8GB Ram
    second build: 115m4.830s, 5 GB Ram
    notes: 1 core only. And obviously should not use so much ram.


CMake:
------------------------------------------
    first build: 2m39.384s, 69 MB Ram
    second build: 0m53.025s, 53 MB Ram
    notes: 4 cores


Raise:
------------------------------------------
    first build: 5m6.383s, 22.5 MB Ram
    second build: 0m2.553s, 22.5 MB Ram
    notes: 4 cores


* * *


Instructions:
===========================================
GNU Make:
------------------------------------------
    # Run generate_code.py to make the 10,000 files
    python generate_code.py

    # Move to the dir
    cd make

    # Build the files and get the time
    time make -j4


CMake:
------------------------------------------
    # Run generate_code.py to make the 10,000 files
    python generate_code.py

    # Move to the dir
    cd cmake

    # Setup
    cmake .

    # Build the files and get the time
    time make -j4


Raise:
------------------------------------------
    # Run generate_code.py to make the 10,000 files
    python generate_code.py

    # Move to the dir
    cd raise

    # Setup
    ./raise update

    # Build the files and get the time
    time ./raise build

