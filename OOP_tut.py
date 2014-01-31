##################################################
# Python Module
##################################################


class pet:
	#class variables [public, shared by all instances of class pet]
	num_of_legs = 0


	#class constructor
	def __init__(self,name):
		self.name = name  #instance variables, accessed only by its own instance

	#class methods	
	#always include 'self' in class methods
	#this ensures we are passing in the instance object information
	def sleep(self):
		print 'zzz'

	def count_legs(self):
		print "I have %s legs." % self.num_of_legs

#class inheritance
class dog(pet):

	def bark(self):
		print "woof"

if __name__ == '__main__':
 
	doug = pet('mike')
	print doug.name
	
