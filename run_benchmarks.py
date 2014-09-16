import sys, os
import time, datetime
import shutil
import subprocess


# Configuration
# The number of libraries and directories
DIR_COUNT = 10
LIB_COUNT = 100

# All tools in this list will be benchmarked
TOOLS_TO_TEST = [
	'cmake', 
	'waf', 
	'raise', 
	'make',
]


print('Starting benchmark with {0} directories containing {1} files each ...'.format(DIR_COUNT, LIB_COUNT))

def format_time(start, end):
	seconds = end - start
	m, s = divmod(seconds, 60)
	h, m = divmod(m, 60)
	return "%d:%02d:%02d" % (h, m, s)

def rmdir(name):
	if os.path.isdir(name):
		shutil.rmtree(name)

def run_and_get_stdall(command):
	# Start the process in a real shelll and pipe the std io
	p = subprocess.Popen(
		command, 
		stderr = subprocess.PIPE, 
		stdout = subprocess.PIPE, 
		shell = True, 
		env = os.environ
	)

	# Save the stdout and stderr
	out, err = p.communicate()
	if err:
		out += err

	# Get the return code
	rc = p.returncode
	if hasattr(os, 'WIFEXITED') and os.WIFEXITED(rc):
		rc = os.WEXITSTATUS(rc)

	# Throw if there was an error
	if rc != 0:
		raise Exception('Return not 0 on: ' + command + ', ' + out)

	return out

# Make code dir
rmdir('c')
os.mkdir('c')

# Move to code dir
os.chdir('c')

# Make the C headers and libraries
print('Generating code ...')
for d in range(DIR_COUNT):
	os.mkdir(str(d))
	os.chdir(str(d))
	for n in range(LIB_COUNT):
		code_name = 'l{0}.c'.format(n)
		with open(code_name, 'wb') as f:
			code = "int fn_" + str(d) + "_" + str(n) + "(int a, int b) { \r\n" + \
			"	return a + b;\r\n" + \
			"}\r\n\r\n"

			f.write(code)

		code_name = 'l{0}.h'.format(n)
		with open(code_name, 'wb') as f:
			code = "int fn_" + str(d) + "_" + str(n) + "(int a, int b);\r\n\r\n"

			f.write(code)
	os.chdir('..')

# Make the C main
with open('main.c', 'wb') as f:
	code = ""
	for d in range(DIR_COUNT):
		for n in range(LIB_COUNT):
			code += '#include "{0}/l{1}.h"\r\n'.format(d, n)

	code += "\r\nint main() { \r\n" 

	for d in range(DIR_COUNT):
		for n in range(LIB_COUNT):
			code += "fn_" + str(d) + "_" + str(n) + "(" + str(n) + ", " + str(n) + ");\r\n"

	code += "return 0;\r\n}\r\n\r\n"

	f.write(code)

# Move back to the orig dir
os.chdir('..')

# Remove old code
for tool in TOOLS_TO_TEST:
	rmdir('{0}/c'.format(tool))
	rmdir('{0}/build'.format(tool))

# Copy the code to each build directory
for tool in TOOLS_TO_TEST:
	shutil.copytree('c', '{0}/c'.format(tool))


# Remove generated code
rmdir('c')

if 'cmake' in TOOLS_TO_TEST:
	# CMake clean test
	os.mkdir('cmake/build')
	os.chdir('cmake/build')
	run_and_get_stdall('cmake ..')
	print('CMake benchmark ...')
	start = time.time()
	r = run_and_get_stdall('make -j2')
	#print(r)
	end = time.time()
	print('    clean time      : ' + format_time(start, end))

	# CMake incremental test
	run_and_get_stdall('touch ../c/{0}/l{1}.c'.format(DIR_COUNT / 2, LIB_COUNT / 2))
	start = time.time()
	r = run_and_get_stdall('make -j2')
	#print(r)
	end = time.time()
	print('    incremental time: ' + format_time(start, end))
	os.chdir('../..')

if 'waf' in TOOLS_TO_TEST:
	# Waf clean test
	os.chdir('waf')
	run_and_get_stdall('./waf configure')
	print('Waf benchmark ...')
	start = time.time()
	run_and_get_stdall('./waf build -j2')
	end = time.time()
	print('    clean time      : ' + format_time(start, end))

	# Waf incremental test
	run_and_get_stdall('touch c/{0}/l{1}.c'.format(DIR_COUNT / 2, LIB_COUNT / 2))
	start = time.time()
	run_and_get_stdall('./waf build -j2')
	end = time.time()
	print('    incremental time: ' + format_time(start, end))
	os.chdir('..')

if 'raise' in TOOLS_TO_TEST:
	# Raise clean test
	os.chdir('raise')
	run_and_get_stdall('./raise update')
	print('Raise benchmark ...')
	start = time.time()
	run_and_get_stdall('./raise build')
	end = time.time()
	print('    clean time      : ' + format_time(start, end))

	# Raise incremental test
	run_and_get_stdall('touch c/{0}/l{1}.c'.format(DIR_COUNT / 2, LIB_COUNT / 2))
	start = time.time()
	run_and_get_stdall('./raise build')
	end = time.time()
	print('    incremental time: ' + format_time(start, end))
	os.chdir('..')

if 'make' in TOOLS_TO_TEST:
	# Make clean test
	os.chdir('make')
	print('Make benchmark ...')
	start = time.time()
	r = run_and_get_stdall('make -j2')
	#print(r)
	end = time.time()
	print('    clean time      : ' + format_time(start, end))

	# Make incremental test
	run_and_get_stdall('touch c/{0}/l{1}.c'.format(DIR_COUNT / 2, LIB_COUNT / 2))
	start = time.time()
	r = run_and_get_stdall('make -j2')
	#print(r)
	end = time.time()
	print('    incremental time: ' + format_time(start, end))
	os.chdir('..')

