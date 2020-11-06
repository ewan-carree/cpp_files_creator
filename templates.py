def create_main_cpp(main_file_name, userName, time, headerName):
	with open(main_file_name+".cpp", 'w') as file:
		file.write("//////////////////////////////////\n")
		file.write('//\t'+main_file_name+".cpp"+'\n')
		file.write('//\t'+time+'\n')
		file.write('//\t'+userName+'\n')
		file.write("//////////////////////////////////\n\n")

		file.write("#include &".replace("&", '"')+headerName+".hpp&\n\n".replace("&", '"'))

		file.write("int main(int argc, char const *argv[])\n")
		file.write("{\n")
		file.write("\t/* code */\n")
		file.write("\treturn 0;\n")
		file.write("}\n")


def create_header_cpp(header_file_name, namespace_name):
	with open(header_file_name+".cpp", 'w') as file:
		file.write("#include &".replace("&", '"')+header_file_name+".hpp&\n\n".replace("&", '"'))
		file.write("namespace "+namespace_name+"\n")
		file.write("{\n")
		file.write("\n")
		file.write("} //"+namespace_name+"\n")


def create_header_hpp(header_file_name, namespace_name):
	with open(header_file_name+".hpp", 'w') as file:
		file.write("#ifndef "+header_file_name.upper()+"_HPP\n")
		file.write("#define "+header_file_name.upper()+"_HPP\n\n")
		file.write("#include <vector>\n")
		file.write("#include <string>\n")
		file.write("#include <stdexcept> //runtime_error\n")
		file.write("#include <iostream>\n")
		file.write("#include <utility> // std::move()\n\n")
		file.write("namespace "+namespace_name+"\n")
		file.write("{\n")
		file.write("\tclass "+header_file_name+"\n")
		file.write("\t{\n")
		file.write("\t\t/* attributes */")
		file.write("\n\n")
		file.write("\t\t"+header_file_name+"() : "+header_file_name+"(/* parameters */) { }\n")
		file.write("\t\t"+header_file_name+"(/* parameters */) : /* complete */ { }\n")
		file.write("\n")
		file.write("\t\t"+header_file_name+"(const "+header_file_name+" &) = default; //constructeur par recopie\n")
		file.write("\t\t"+header_file_name+"("+header_file_name+" &&) = default; //constructeur par déplacement\n")
		file.write("\t\t"+header_file_name+"& operator=(const "+header_file_name+" &) = default; //affectation par recopie\n")
		file.write("\t\t"+header_file_name+"& operator=("+header_file_name+" &&) = default; //affectation par déplacement\n")
		file.write("\t\t~"+header_file_name+"() = default; //destructeur\n")
		file.write("\t};\n\n")
		file.write("\tstd::ostream& operator<<(std::ostream& os, const "+header_file_name+"& "+header_file_name[0].lower()+")\n")
		file.write("\t{\n")
		file.write("\t\tos << /* complete */;\n")
		file.write("\t\treturn os;\n")
		file.write("\t}\n")
		file.write("} //"+namespace_name+"\n")
		file.write("#endif //"+header_file_name.upper()+"_HPP")