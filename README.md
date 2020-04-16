# CPP_FILES_CREATOR
This python script creates the three necessary files to code in C++

## Template
### First file template
//////////////////////////////////
//	Prog.cpp
//	2020-04-16 17:17:32.772289
//	ewan
//////////////////////////////////

#include "test.hpp"

int main(int argc, char const *argv[])
{
	std::cout << "hello" << std::endl;
	return 0;
}

### Second file template
#include "test.hpp"

namespace exam
{

} //exam

### Third file template
#ifndef TEST_HPP
#define TEST_HPP

#include <vector>
#include <string>
#include <stdexcept> //runtime_error
#include <iostream>
#include <utility> // std::move()

namespace exam
{

} //exam
#endif //TEST_HPP

## Use of cpp_files_creator
you have to use your main.py with tree arguments, no more, no less ord it won't work
template : main.py mainProgName headersProgName nameSpaceName

### Tip
you can create an alias as I did on your console:
alias cpp='python3 ~/Workspace_ubuntu/C++/cpp_files_creator/main.py' in the .bashrc file

### Command
then go to the directory you want to use for coding and use this new command:
cpp ### ### ###

Done !
