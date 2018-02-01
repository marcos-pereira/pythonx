import ClassSample as cls

def main():
	
	# Initialize class
	classObject1 = cls.ClassSample('Object1',3147)
	
	# Check class attributes
	print "classObject1 name = " + str(classObject1.name)
	print "classObject1 number = " + str(classObject1.number)

	# Change class attributes with class methods
	classObject1.change_name('Object1 v1')
	classObject1.change_number(3.1415)
	classObject1.print_class_status()

	# Test to call static method
	cls.ClassSample.what_is_this_object()
	print "Is class sample? " + str(cls.ClassSample.is_class_sample)


if __name__ == '__main__':
	try:
		main()
	except Exception:		
		raise RuntimeError('Main function not found!')