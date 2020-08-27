
# Make

## Concepts

* The command of the rule is executed by shell
* Make prints the command before executing (if not desired put @ before the command)
* Put '-' before command if stderr of command is not desired.
    * example: -rm $(TARGET)
* wildcards are '*' , '?', [...]. They're meaning is exactly like in shell.
* wildcard are expended automatically in targets and prerequisites. 
* In commands the shell is responsible for expansion
* In other contexts the expansion will happen only explicitly by calling  `wildcard` function
    * example: `objects := $(wildcard *.o)` will be expanded during `objects` variable definition
* `$@` automatic variable for target of the rule
* `$?` automatic variable that contains only prerequisites that have been changed
* `$^` all prerequisites
* `$<` only first prerequisite
* `$>` only last prerequisite
* `$*` the stem of target filename. stem is a filename without suffix
* `:=` variables that are defined this way are exapnded when they defined rather when used

## Makefile example

```sh
SRC = .
OBJ = obj

HEADERS = $(wildcard $(SRC)/*.h)
OBJECTS = $(patsubst $(SRC)/%.cpp, $(OBJ)/%.o, $(wildcard $(SRC)/*.cpp))

CXX = g++
ARCH = -m64
CXXFLAGS = -g -std=c++11 -Wall -pedantic $(ARCH)

TARGET = prime
INCLUDE = -I./include
LIBDIR = -L./lib
LIBS = -lpthread

default: $(TARGET)

all: default

$(OBJECTS): | $(OBJ)

$(OBJ):
	mkdir -p $@

$(OBJ)/%.o: $(SRC)/%.cpp $(HEADERS)
	$(CXX) -c -o $@ $< $(CXXFLAGS)

$(TARGET): $(OBJECTS)
	$(CXX) -o $@ $^ $(CXXFLAGS) $(LIBDIR) $(LIBS)

.PHONY: all clean

clean:
	rm -f $(OBJ)/*.o $(TARGET) core

```

--------------------------------
## Make links

* GNU make documentation                <https://www.gnu.org/software/make/manual/html_node/index.html>
* Advanced auto-dependency generation   <http://make.mad-scientist.net/papers/advanced-auto-dependency-generation/>
* things you should know about make     <http://www.alexeyshmalko.com/2014/7-things-you-should-know-about-make>
* GNU automake                          <https://www.gnu.org/software/automake/manual/html_node/index.html>
* subdirs in makefile <https://stackoverflow.com/questions/4036191/sources-from-subdirectories-in-makefile>

