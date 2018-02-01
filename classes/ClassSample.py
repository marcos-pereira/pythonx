class ClassSample(object):
	"""This is an example of a class which have its attributes and methods
		Attributes:
			classname: name of the class object
			classnumber: number of the class object
	"""

	is_class_sample = True	# Indicate this is a class sample and holds for every class instance

	def __init__(self, classname, classnumber):
		"""Return a class object whose name is *classname* and starting
		number is *classnumber*."""
		self.name = classname
		self.number = classnumber

	@staticmethod
	def what_is_this_object():
		print "This is an example of a class in python."

	def change_number(self, new_number):
		self.number = new_number

	def change_name(self, new_name):
		self.name = new_name

	def print_class_status(self):		
		print "\nClass attributes:"
		print "name = " + str(self.name)
		print "number = " + str(self.number)


