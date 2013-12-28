import sys, os
import shutil

DIR_COUNT = 100
LIB_COUNT = 100


def rmdir(name):
	if os.path.exists(name):
		shutil.rmtree(name)

# Make code dir
rmdir('c')
os.mkdir('c')

# Move to code dir
os.chdir('c')

# Make the C headers and libraries
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
rmdir('cmake/c')
rmdir('make/c')
rmdir('raise/c')
rmdir('waf/c')

# Copy the code to each build directory
shutil.copytree('c', 'cmake/c')
shutil.copytree('c', 'make/c')
shutil.copytree('c', 'raise/c')
shutil.copytree('c', 'waf/c')

# Remove generated code
rmdir('c')


