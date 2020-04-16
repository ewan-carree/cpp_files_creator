import lib

class Main_cpp():
	def __init__(self, name):
		self.name_ = name+".cpp"

	def create_main_cpp(self, userName, time, headerName):
		with open(self.name_, 'w') as file:
			file.write("//////////////////////////////////\n")
			file.write('//\t'+self.name_.capitalize()+'\n')
			file.write('//\t'+time+'\n')
			file.write('//\t'+userName+'\n')
			file.write("//////////////////////////////////\n\n")

			file.write("#include &".replace("&", '"')+headerName+".hpp&\n\n".replace("&", '"'))

			file.write("int main(int argc, char const *argv[])\n")
			file.write("{\n")
			file.write("\t/* code */\n")
			file.write("\treturn 0;\n")
			file.write("}\n")

class Header_cpp():
	def __init__(self, name, namespace):
		self.name_ = name+".cpp"
		self.namespace_ = namespace

	def create_header_cpp(self, headerName):
		with open(self.name_, 'w') as file:
			file.write("#include &".replace("&", '"')+headerName+".hpp&\n\n".replace("&", '"'))
			file.write("namespace "+self.namespace_+"\n")
			file.write("{\n")
			file.write("\n")
			file.write("} //"+self.namespace_+"\n")

class Header_hpp():
	def __init__(self, name, namespace):
		self.name_ = name+"_hpp"	
		self.namespace_ = namespace	

	def create_header_hpp(self):
		with open(self.name_.replace('_', '.'), 'w') as file:
			file.write("#ifndef "+self.name_.upper()+"\n")
			file.write("#define "+self.name_.upper()+"\n\n")
			file.write("#include <vector>\n")
			file.write("#include <string>\n")
			file.write("#include <stdexcept> //runtime_error\n")
			file.write("#include <iostream>\n")
			file.write("#include <utility> // std::move()\n\n")
			file.write("namespace "+self.namespace_+"\n")
			file.write("{\n")
			file.write("\n")
			file.write("} //"+self.namespace_+"\n")
			file.write("#endif //"+self.name_.upper())
