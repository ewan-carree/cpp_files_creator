#alias cpp='python3 ~/Workspace_ubuntu/C++/cpp_files_creator/main.py'

import lib
import files

global userName
global time
userName = lib.get_userName()
time = lib.get_time()

def main():
	main, header, namespace = lib.extract_args()
	lib.create_file(header)
	lib.set_path(lib.get_path(), header)
	lib.add_GNU()

	mainFile= files.Main_cpp(main)
	mainFile.create_main_cpp(userName, time, header)
	
	headercppFile = files.Header_cpp(header, namespace)
	headercppFile.create_header_cpp(header)

	headerhppFile = files.Header_hpp(header, namespace)
	headerhppFile.create_header_hpp()



if __name__ == '__main__':
	main()
