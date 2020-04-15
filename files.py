import lib

class Main_cpp():
	def __init__(self, name):
		self.name_ = name+".cpp"

class Header_cpp():
	def __init__(self, name, namespace):
		self.name_ = name+".cpp"
		self.namespace_ = namespace

class Header_hpp():
	def __init__(self, name, namespace):
		self.name_ = name+".hpp"	
		self.namespace_ = namespace	