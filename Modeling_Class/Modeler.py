import math

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import *

from direct.directnotify.DirectNotify import DirectNotify

from inspect import currentframe

class MyApp(ShowBase):
	__x = None
	__y = None
	__z = None
	__heading = None
	__overall_sequence = None

	#"fake" tello information
	__tello = None
	__commanding = False
	__connection = None

	def __init__(self,ip,port):
		ShowBase.__init__(self)

		# Disable the camera trackball controls (for dev purposes).
		#self.disableMouse()

		self.__tello=(ip,port)

		# Load the environment model.
		self.scene = self.loader.loadModel("/Users/josephburris/Desktop/Local_Drone_Files/3D_Stuff/test.bam")
        # Reparent the model to render.
		self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.

		self.scene.setScale(1, 1, 1)
		self.scene.setPos(-8, 42, 0)

		self.__x = -8
		self.__y = 42
		self.__z = 0

		self.__heading = 0

		self.droneActor = self.loader.loadModel("/Users/josephburris/Desktop/Local_Drone_Files/3D_Stuff/drone.bam")

		self.droneActor.setScale(1, 1, 1)
		self.droneActor.reparentTo(self.render)
		self.droneActor.setPos(-8,42,1)

		self.__overallSequence = Sequence()

	def __get_linenumber():
		cf = currentframe()
		cf.f_back.f_lineno

	def startTest(self):
		self.__overallSequence.start()

	def connect(self):
		if(self.__connection == None):
			notify = DirectNotify().newCategory("")
			notify.warning("(Connection placeholder)")
			self.__connection = "placeholder"
			notify = DirectNotify().newCategory("")
			notify.warning("Connected!")
			#Note: Connecting to the drone will be considered successful for tests
		else:
			notify = DirectNotify().newCategory("")
			notify.warning("Oops, something went wrong connecting the socket")
			exit()

	def disconnect(self):
		if(self.__connection != None):
			__tello = None
			__commanding = False
			__connection = None
			notify = DirectNotify().newCategory("")
			notify.warning("Disonnected!")
		else:
			notify = DirectNotify().newCategory("")
			notify.warning("You are not connected to a drone yet")
			exit()

	def command(self):
		if(self.__commanding == True):
			notify = DirectNotify().newCategory("")
			notify.warning("You are already commanding a drone")
			exit()
		self.__commanding = True

	def __commandCheck(self):
		if (self.__commanding == False):
			notify = DirectNotify().newCategory("")
			notify.warning("The drone is not set to command")
			self.disconnect()
			exit()

	def wait(self,amount):
		self.__commandCheck()
		seq = self.droneActor.posInterval(amount,Point3(self.__x,self.__y,self.__z))
		self.__overallSequence.append(seq)

	def takeoff(self):
		if(self.__z!=0):
			notify = DirectNotify().newCategory("")
			notify.warning("The drone has already taken off")
			exit()
		self.__commandCheck()
		seq = self.droneActor.posInterval(2,Point3(self.__x,self.__y,self.__z+10))
		self.__z = self.__z + 10
		self.__overallSequence.append(seq)

	def land(self):
		if(self.__z==0):
			notify = DirectNotify().newCategory("")
			notify.warning("The drone has already landed")
			exit()
		self.__commandCheck()
		seq = self.droneActor.posInterval(self.__z/5,Point3(self.__x,self.__y,0))
		self.__z = 0
		self.__overallSequence.append(seq)

	def cw(self,amount):
		self.__commandCheck()
		if(amount>3600 or amount<1):
			#print("Error Line ",self.__get_linenumber,": Please enter amount between 1 and 3600 ")
			notify = DirectNotify().newCategory("MyCategory")
			notify.warning("Error: For 'cw' please enter amount between 1 and 3600 ")
			exit()
		seq = self.droneActor.hprInterval(amount/45,Vec3(amount, 0, 0))
		self.__heading = self.__heading + amount
		while(self.__heading > 360):
			self.__heading = self.__heading - 360
		self.__overallSequence.append(seq)

	#not functioning
	#def ccw(self,amount):
		#self.__commandCheck()
		#if(amount>3600 or amount<1):
			#print("Error Line ",self.__get_linenumber,": Please enter amount between 1 and 3600 ")
			#notify = DirectNotify().newCategory("MyCategory")
			#notify.warning("Error: For 'ccw' please enter amount between 1 and 3600 ")
			#exit()
		#amount = amount * -1
		#seq = self.droneActor.hprInterval(amount/45,Vec3(0, 0, amount))
		#self.__heading = self.__heading + amount
		#while(self.__heading < 0):
			#self.__heading = self.__heading + 360
		#self.__overallSequence.append(seq)

	#primarily for dev purposes
	def get_height(self):
		self.__commandCheck()
		notify = DirectNotify().newCategory("")
		notify.warning(self.__heading)

	def printX(self):
		notify = DirectNotify().newCategory("")
		notify.warning(self.__x)

	def printY(self):
		notify = DirectNotify().newCategory("")
		notify.warning(self.__y)

	#primarily for dev purposes
	def printHeading(self):
		notify = DirectNotify().newCategory("")
		notify.warning(self.__heading)

	def forward(self,distance):
		self.__commandCheck()
		if(distance>500 or distance<20):
			#print("Error Line ",self.__get_linenumber,": Please enter amount between 1 and 3600 ")
			notify = DirectNotify().newCategory("")
			notify.warning("Error: For 'forwards' please enter amount between 20 and 500 ")
			exit()
		distance = distance/10
		newx = (distance * math.cos(self.__heading))+self.__x
		newy = (distance * math.sin(self.__heading))+self.__y
		seq = self.droneActor.posInterval(distance/5,Point3(newx,newy,self.__z))
		self.__x = newx
		self.__y = newy
		self.__overallSequence.append(seq)

	def back(self,distance):
		self.__commandCheck()
		if(distance>500 or distance<20):
			#print("Error Line ",self.__get_linenumber,": Please enter amount between 1 and 3600 ")
			notify = DirectNotify().newCategory("")
			notify.warning("Error: For 'back' please enter amount between 20 and 500 ")
			exit()
		distance = distance/10
		newAngle = self.__heading+180
		while(newAngle>360):
			newAngle = newAngle-360
		newx = (distance * math.cos(newAngle))+self.__x
		newy = (distance * math.sin(newAngle))+self.__y
		seq = self.droneActor.posInterval(distance/5,Point3(newx,newy,self.__z))
		self.__x = newx
		self.__y = newy
		self.__overallSequence.append(seq)

	def right(self,distance):
		self.__commandCheck()
		if(distance>500 or distance<20):
			#print("Error Line ",self.__get_linenumber,": Please enter amount between 1 and 3600 ")
			notify = DirectNotify().newCategory("")
			notify.warning("Error: For 'right' please enter amount between 20 and 500 ")
			exit()
		distance = distance/10
		newAngle = self.__heading+90
		while(newAngle>360):
			newAngle = newAngle-360
		newx = (distance * math.cos(newAngle))+self.__x
		newy = (distance * math.sin(newAngle))+self.__y
		seq = self.droneActor.posInterval(distance/5,Point3(newx,newy,self.__z))
		self.__x = newx
		self.__y = newy
		self.__overallSequence.append(seq)

	def left(self,distance):
		self.__commandCheck()
		if(distance>500 or distance<20):
			#print("Error Line ",self.__get_linenumber,": Please enter amount between 1 and 3600 ")
			notify = DirectNotify().newCategory("")
			notify.warning("Error: For 'left' please enter amount between 20 and 500 ")
			exit()
		distance = distance/10
		newAngle = self.__heading+270
		while(newAngle>360):
			newAngle = newAngle-360
		newx = (distance * math.cos(newAngle))+self.__x
		newy = (distance * math.sin(newAngle))+self.__y
		seq = self.droneActor.posInterval(distance/5,Point3(newx,newy,self.__z))
		self.__x = newx
		self.__y = newy
		self.__overallSequence.append(seq)

	def up(self,distance):
		self.__commandCheck()
		if(distance>500 or distance<20):
			#print("Error Line ",self.__get_linenumber,": Please enter amount between 1 and 3600 ")
			notify = DirectNotify().newCategory("")
			notify.warning("Error: For 'up' please enter amount between 20 and 500 ")
			exit()
		distance = distance/10
		newz = self.__z+distance
		seq = self.droneActor.posInterval(distance/5,Point3(self.__x,self.__y,newz))
		self.__z = newz
		self.__overallSequence.append(seq)

	def down(self,distance):
		self.__commandCheck()
		if(distance>500 or distance<20):
			#print("Error Line ",self.__get_linenumber,": Please enter amount between 1 and 3600 ")
			notify = DirectNotify().newCategory("")
			notify.warning("Error: For 'down' please enter amount between 20 and 500 ")
			exit()
		distance = distance/10
		newz = self.__z-distance
		if(newz<10):
			notify = DirectNotify().newCategory("")
			notify.warning("Error: You cannot go lower than takeoff distance ")
			exit()
		seq = self.droneActor.posInterval(distance/5,Point3(self.__x,self.__y,newz))
		self.__z = newz
		self.__overallSequence.append(seq)