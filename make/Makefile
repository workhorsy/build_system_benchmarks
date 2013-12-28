CC=gcc
CFLAGS=-I.
DEPS:=$(wildcard c/*/*.h)
OBJ:=$(subst .h,.o,$(DEPS)) c/main.o

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

hellomake: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)

