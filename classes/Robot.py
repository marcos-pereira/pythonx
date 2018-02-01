from abc import ABCMeta, abstractmethod

class Robot(object):
	"""	This is an example of a robot class which have its attributes and methods. 
		This class was created to test object oriented programming in Python
		Attributes:
			name: name of the robot
			maker: maker of the robot
			degrees_of_freedom: number of degrees of freedom of robot
			color: color of robot

	"""

	__metaclass__ = ABCMeta

	is_robot = True	# Indicate this is a class sample and holds for every class instance

	def __init__(self, name, maker, color):
		"""Return a class object whose name is *classname* and starting
		number is *classnumber*."""
		self.name = name
		self.maker = maker
		self.color = color

	@staticmethod
	def what_is_this_object():
		print "This is an example of a class in python."

	def print_robot_specifications(self):		
		""" Print all the robot specifications """
		print "\nRobot specifications:"
		print "Name = " + str(self.name)
		print "Maker = " + str(self.maker)
		print "Color = " + str(self.color)
		pass

	@abstractmethod	
	# This is a virtual method to make class an abstract base classe (ABC)
	# The method must exist in child class but not be implemented in the child class
	# Since this method is an abstractmethod, it is not possible to instantiate Robot
	# Only the child classes of Robot
	def print_robot_type(self):
		""" Print the robot type """
		pass


class Manipulator(Robot):
	def __init__(self, name, maker, color, degrees_of_freedom, payload, gripper_type, configuration):
		Robot.__init__(self, name, maker, color)
		self.degrees_of_freedom = degrees_of_freedom
		self.payload = payload
		self.gripper_type = gripper_type
		self.configuration = configuration

	def print_manipulator_specifications(self):
		print "Payload (Kg) = " + str(self.payload)
		print "Gripper type = " + str(self.gripper_type)
		print "Robot configuration = " + str(self.configuration)

	def print_robot_type(self):
		print "\nRobot type = Manipulator"

class Wheeled(Robot):
	def __init__(self, name, maker, color, wheel_type):
		Robot.__init__(self, name, maker, color)
		self.wheel_type = wheel_type

	def print_wheeled_specifications(self):
		print "Wheeled type = " + str(self.wheel_type)		

	def print_robot_type(self):
		print "\nRobot type = Wheeled"		





