import Robot as rbt

def main():
	
	# Initialize class
	Manipulator1 = rbt.Manipulator('A2 Arm','Meka Robotics','Gray', 7, 2, 'Servo-Electric', 'Articulated')
	Manipulator2 = rbt.Manipulator('KR Agilus','Kuka', 'Orange', 6, 6, 'Servo-Electric', 'Articulated')
	Manipulator3 = rbt.Manipulator('Baxter Arm - Vacuum Cup','Rethink Robotics', 'Red', 7, 2.2, 'Vacuum', 'Articulated')
	Wheeled1 = rbt.Wheeled('Pioneer 3 AT', 'Omron Mobile Robots', 'red', 'four wheeled')
	
	# Check class attributes
	# print "Manipulator1 name = " + str(Manipulator1.name)
	# print "Manipulator1 maker = " + str(Manipulator1.maker)

	Manipulator1.print_robot_type()				# Test to call abstractmethod
	Manipulator1.print_robot_specifications()
	Manipulator1.print_manipulator_specifications()
	rbt.Manipulator.what_is_this_object()		# Test to call static method

	Manipulator2.print_robot_type()				# Test to call abstractmethod
	Manipulator2.print_robot_specifications()
	Manipulator2.print_manipulator_specifications()
	rbt.Manipulator.what_is_this_object()		# Test to call static method

	Manipulator3.print_robot_type()				# Test to call abstractmethod
	Manipulator3.print_robot_specifications()
	Manipulator3.print_manipulator_specifications()
	rbt.Manipulator.what_is_this_object()		# Test to call static method

	Wheeled1.print_robot_type()				# Test to call abstractmethod
	Wheeled1.print_robot_specifications()
	Wheeled1.print_wheeled_specifications()
	rbt.Wheeled.what_is_this_object()		# Test to call static method


if __name__ == '__main__':	
	# try:
		main()
	# except Exception:		
	# 	raise RuntimeError('Main function not found!')