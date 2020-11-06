# CPP_FILES_CREATOR
This python script creates the three necessary files to code in C++ (.cpp / .hpp) with the appropriate makefile.


Here are the templates if I run this command :  cpp main GithubExample git --folder=True (cpp is my alias for "python3 /path/to/cpp_files_creator/main.py")

## Template
### First file template
	//////////////////////////////////
	//	main.cpp
	//	2020-11-06 20:27:23.337267
	//	carree
	//////////////////////////////////

	#include "GithubExample.hpp"

	int main(int argc, char const *argv[])
	{
		/* code */
		return 0;
	}

### Second file template

	#include "GithubExample.hpp"

	namespace git
	{

	} //git

### Third file template

	#ifndef GITHUBEXAMPLE_HPP
	#define GITHUBEXAMPLE_HPP

	#include <vector>
	#include <string>
	#include <stdexcept> //runtime_error
	#include <iostream>
	#include <utility> // std::move()

	namespace git
	{
		class GithubExample
		{
			/* attributes */

			GithubExample() : GithubExample(/* parameters */) { }
			GithubExample(/* parameters */) : /* complete */ { }

			GithubExample(const GithubExample &) = default; //constructeur par recopie
			GithubExample(GithubExample &&) = default; //constructeur par déplacement
			GithubExample& operator=(const GithubExample &) = default; //affectation par recopie
			GithubExample& operator=(GithubExample &&) = default; //affectation par déplacement
			~GithubExample() = default; //destructeur
		};

		std::ostream& operator<<(std::ostream& os, const GithubExample& g)
		{
			os << /* complete */;
			return os;
		}
	} //git
	#endif //GITHUBEXAMPLE_HPP

## Use of cpp_files_creator
You have to use your main.py with tree arguments, no more, no less ord it won't work

python3 main.py mainProgName headersProgName nameSpaceName --Folder=True

Then, if you want to add some files in relation with your project, you can run this command : python3 main.py mainProgName newHeadersProgName newNameSpaceName --add=True

### Tip
you can create an alias as I did on your console:
alias cpp='python3 ~/Workspace_ubuntu/C++/cpp_files_creator/main.py' in the ~/.bashrc file

You have other available options that you can see by using : python3 main.py--help
