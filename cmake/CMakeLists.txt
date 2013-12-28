cmake_minimum_required (VERSION 2.8)
project (Example)


include_directories("${PROJECT_BINARY_DIR}")

# Get all the library .c and .h files
file(GLOB lib_files
	"c/*/*.h"
	"c/*/*.c"
)

# add the executable
add_executable(main ${lib_files} c/main.c )

