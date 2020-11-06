from lib import *
from templates import *

def main():
	args = parseArguments()

	if not args.add:
		if args.folder:
			create_folder(args.header_file_name)
			set_path(get_path(), args.header_file_name)

		addGNU(args.GNUversion, args.main_file_name)

		create_main_cpp(args.main_file_name, get_userName(), get_time(), args.header_file_name)
		create_header_cpp(args.header_file_name, args.namespace_name)
		create_header_hpp(args.header_file_name, args.namespace_name)

	elif args.add:
		create_header_cpp(args.header_file_name, args.namespace_name)
		create_header_hpp(args.header_file_name, args.namespace_name)



if __name__ == '__main__':
	main()