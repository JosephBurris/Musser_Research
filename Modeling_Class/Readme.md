**Opening Notes:**
* In order to use this class:
  * You MUST have the Panda3D SDK installed: https://www.panda3d.org/
  * You MUST have the files in this folder be in your working folder, and the beginning of your code must include the following line:
    * from Modeler import *
    
    
* Creation of a new MyApp object:
  * In order to create a new Modeler object, the "model" must be provided with a valid/invalid IP and Port.
    * In the format of this: test = MyApp("example ip"(String),1111(int))
    * Example: test = MyApp("192.168.10.1", 8889)
    
* Running new MyApp scenarios:
  * In order for new MyApp scenarios to be run, the user must include the "test.startTest()" and "test.run()" commands, otherwise the animations will not be loaded properly.
  * Example:
  
app = MyApp("ip placeholder","port placeholder")
(Some kind of commands telling the MyApp object what to do)
app.startTest()
app.run()
    
* **Important notes:**
  * For this class, it is assumed that the "fake drone" will connect, disconnect, and receive commands properly from the user.
  * Also, this class creates 2 3d objects, the user is able to control the "drone" object in this 3d environment, and not the "platform" object
    
**MyApp Methods/Functions**

* (Hidden) app.__init__(ip,port)
  * @Param: ip (valid IP adress, String), port (Valid port, int)
  * @Output: None
  * @Errors: None
  * Desc: This is set up to be similar to the drone class in the way that drones are initialized. Besides that, the main purpose of this function is to load the drone/platform models. Then, it sets both to be constructed on top of the other and reparents them to the base node of the world. Also, it sets the x,y,z,heading, overall_sequence, and tello attributes. Essentially, it preps the "world" that the drone and platform will be set into.
  
* (IMPORTANT!) app.startTest()
  * @Param: None
  * @Output: None
  * @Errors: None
  * Desc: So, for panda3d, animations are set up sequentially in objects called "sequences" these sequences can be added to. So, this function calls the overall Sequence object that all commands (with their own separate sequences) are added to.
  
* (Hidden) app.get_linenumber()
  * @Param: None
  * @Output: None
  * @Errors: None
  * Desc: This is a hidden funciton primarily used for dev purposes in order to report specific line numbers for error reports.

* (IMPORTANT!) drone.connect()
  * @Param: None
  * @Output: None
  * @Errors: If a connection has already been created, then this function will print out the message "Oops, something went wrong connecting the socket" and end the program. 
  * Desc: This must be called in order to create a connection to the drone, if it is not called, then no other function will work.
  
* (IMPORTANT!) app.disconnect()
  * @Param: None
  * @Output: None
  * @Errors: If this function is called, and no app is already connected, then it will print the message "You are not connected to a drone yet"
  * Desc: This must be called after you are done using the current drone. While it is not required, if not done, other errors may occur with the drone in a real test with a real drone.
  
* (IMPORTANT!) app.command()
  * @Param: None
  * @Output: None
  * @Errors: If you are already setting the drone object to connect to the same/another drone, then it will print "You are already commanding a drone" and exit.
  * Desc: This function must be called in order to send commands to the drone, like "takeoff", "land", etc... **(Reference 1)** If this is not called before, any command will print "The drone is not set to command", and then exit.
  
* (Hidden) app.commandCheck()
  * @Param: None
  * @Output: None
  * @Errors: If a drone is not set to command and this is called, then it will print "The drone is not set to command" and exit
  * Desc: This function is called in every other command to make sure that a drone has already been set to command, if it is not, then this check will fail and the program will exit
  
* app.wait()
  * @Param: None
  * @Output: None
  * @Errors: View **(Reference 1)**
  * Desc: This function is just causes the drone to wait in its current position before going to the next command (useful for testing purposes)
  
* app.takeoff()
  * @Param: None
  * @Output: None
  * @Errors: View **(Reference 1)** Also, if the drone has already taken off, it will print "The drone has already taken off" and exit.
  * Desc: This command causes the drone to takeoff, generally hovering around 1-2 feet about the ground.
  
* app.land()
  * @Param: None
  * @Output: None
  * @Errors: View **(Reference 1)** Also, if the drone has already landed, it will print "The drone has already landed" and exit.
  * Desc: This command causes the drone to land. While this is not required at the end of a program (because the drone will land itself after disconnecting), it should still be used for good programming practice purposes.
  
* app.cw(degrees)
  * @Param: degrees
  * @Output: None
  * @Errors: View **(Reference 1)**, also **(Reference 2)** if something is sent to the drone that is not an "int" or it is not between 1 and 3600, a response will be given back as "Please enter an integer for the degrees" or "The degrees entered must be between 1 and 3600" respectively and exit.
  * Desc: This command causes the drone to turn clockwise relative to its current heading, then update its heading.
  
* (WIP) app.ccw(degrees)
  * This is an unfinished function that is still a WIP...
  
* app.forward(distance)
  * @Param: distance (20 - 500... approximately cm)
  * @Output: None
  * @Errors: View **(Reference 1)** Also, **(Reference 2)** if something is sent to the drone that is not an "int" or it is not between 20 and 500, a response will be given back as "Please enter an integer for the distance" or "The distance entered must be between 20 and 500" respectively and exit.
  * Desc: This command causes the drone to go forwards a specified number of centimeters relative to its current location, then update its x,y, and z postion.
  
* app.left(distance)
  * @Param: distance (20 - 500... approximately cm)
  * @Output: None
  * @Errors: View **(Reference 1)** and **(Reference 2)**
  * Desc: This command causes the drone to go left a specified number of centimeters relative to its current location, then update its x,y, and z postion.
  
* app.right(distance)
  * @Param: distance (20 - 500... approximately cm)
  * @Output: None
  * @Errors: View **(Reference 1)** and **(Reference 2)**
  * Desc: This command causes the drone to go right a specified number of centimeters relative to its current location, then update its x,y, and z postion.
  
* app.back(distance)
  * @Param: distance (20 - 500... approximately cm)
  * @Output: None
  * @Errors: View **(Reference 1)** and **(Reference 2)**
  * Desc: This command causes the drone to go back a specified number of centimeters relative to its current location, then update its x,y, and z postion.
  
* app.up(distance)
  * @Param: distance (20 - 500... approximately cm)
  * @Output: None
  * @Errors: View **(Reference 1)** and **(Reference 2)**
  * Desc: This command causes the drone to go up a specified number of centimeters relative to its current location, then update its x,y, and z postion.
  
* app.down(distance)
  * @Param: distance (20 - 500... approximately cm)
  * @Output: None
  * @Errors: View **(Reference 1)** and **(Reference 2)** Also, if the new height that the drone will be at is lower than its takeoff amount (its lowest possible postition), then it will print "Error: You cannot go lower than takeoff distance " then exit
  * Desc: This command causes the drone to go down a specified number of centimeters relative to its current location, then update its x,y, and z postion.
  
**Primarly dev functions**
* app.get_height()
  * @Param: None
  * @Output: None
  * @Errors: None
  * Desc: This function just simply prints out the current height (z) value of the drone object

* app.printX()
  * @Param: None
  * @Output: None
  * @Errors: None
  * Desc: This function just simply prints out the current x value of the drone object

* app.printY()
  * @Param: None
  * @Output: None
  * @Errors: None
  * Desc: This function just simply prints out the current y value of the drone object
  
* app.printHeading()
  * @Param: None
  * @Output: None
  * @Errors: None
  * Desc: This function just simply prints out the current heading value of the drone object
