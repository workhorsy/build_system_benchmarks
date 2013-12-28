Build system speed tests. 10,000 C files spread over 100 directories.

Build systems to test:
GNU Make
CMake
Raise

Ninja
Waf
Tup
Redo
Rake
SCons
Maven


GNU Make:
first build: 51m25.352s, 8GB Ram
second build: 115m4.830s, 5 GB Ram
notes: 1 core only. Obviously should not use so much ram.

CMake
first build: 2m39.384s, 69 MB Ram
second build: 0m53.025s, 53 MB Ram

Raise:
first build: 5m6.383s, 22.5 MB Ram
second build: 0m2.553s, 22.5 MB Ram




