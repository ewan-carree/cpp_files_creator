import lib

class Main_cpp():
	def __init__(self, name):
		self.name_ = name+".cpp"

	def create_main_cpp(self, userName, time, headerName):
		content = """
		#################
		prog.cpp
		time
		userName
		#################

		include "header.hpp"

		int main(int argc, char const *argv[])
		{
			/* code */
			return 0;
		}

		"""
		content.replace("prog.cpp",self.name_)
		content.replace("time", time)
		content.replace("userName", userName)
		content.replace("header.hpp", headerName+".hpp")
		with open(self.name_, 'w') as file:
			file.write(content)

class Header_cpp():
	def __init__(self, name, namespace):
		self.name_ = name+".cpp"
		self.namespace_ = namespace

	def create_header_cpp(self, headerName):
		content = """
		include "header.hpp"

		namespace exam
		{
			
		} //exam		
		"""
		content.replace("header.hpp", headerName+".hpp")
		content.replace("exam", self.namespace_)
		with open(self.name_, 'w') as file:
			file.write(content)

class Header_hpp():
	def __init__(self, name, namespace):
		self.name_ = name+".hpp"	
		self.namespace_ = namespace	

	def create_header_hpp(self):
		content="""
		#ifndef NURSERY_HPP
		#define NURSERY_HPP

		#include <vector>
		#include <string>
		#include <stdexcept> //runtime_error
		#include <iostream>
		#include <utility> // std::move()


		namespace exam{


		} // exam

		#endif //NURSERY_HPP
		"""
		content.replace("NURSERY_HPP", self.name_.upper())
		content.replace('.', '_')
		content.replace("exam", self.namespace_)
		with open(self.name_, 'w') as file:
			file.write(content)
