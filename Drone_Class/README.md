**This is a documentation page on how to use the Drone class, provided in this folder**

**Opening Notes:**
* Connecting to the Tello drone with a laptop:
  * Press the button on the side of the drone quickly, and if the drone has power, its light on the side should blink red, then shortly after flash multiple different colors.
  * While the light is blinking multiple different colors, look at your networks options for something similar to TELLO...
  * After you see the correct option, connect to it after the light starts rappidly flashing yellow, signaling proper connection.
  * Now, you should be able to run your code!
* Disconnecting from the Tello and running another test (IMPORTANT):
  * In order to set the Tello to run another test, you MUST disconnect the drone by pressing the power button located on the side of the tello and repeating the steps to connect.
  * A red light will appear if you fail to do this (signalling a disconnect of the socket) and you will NOT be able to run your code until you restart.
* In order to use this class, the drone.py file must be in your working folder, and the beginning of your code must include the following line:
  * from drone import *
* Creation of a new drone object:
  * In order to create a drone object, the drone object must be provided with a valid IP and Port.
    * In the format of this: test = Drone("exampleIP"(String),1111(Int))
    * Example: test = Drone("192.168.10.1", 8889)
    
**General Notes on Python Objects**
* All objects are created in the form: test = Object(parameter1, parameter2, etc...)
* All functions of objects are called in the form: test.function(parameter1, parameter2, etc...)

**Drone Methods/Functions**
* (Hidden) drone.__init__(ip,port)
  * @Param: ip (valid IP adress, String), port (Valid port, int)
  * @Output: None
  * @Errors: None
  * Desc: This is a hidden function for the creation  of new drone objects and preps the IP and Port for their socket connections done in drone.connect()

* (IMPORTANT!) drone.connect()
  * @Param: None
  * @Output: None
  * @Errors: If this function runs into an error, connecting to the drone, then it will print out the message "Oops, something went wrong connecting the socket" and end the program. 
  * Desc: This must be called in order to create a connection to the drone, if it is not called, then no other function will work.
  
* (IMPORTANT!) drone.disconnect()
  * @Param: None
  * @Output: None
  * @Errors: If this function is called, and no drone is already connected, then it will print the message "You are not connected to a drone yet"
  * Desc: This must be called after you are done using the current drone. While it is not required, if not done, other errors may occur with the drone.
  
* (Hidden) drone.send_command(command)
  * @Param: Command (String)
  * @Output: Drone_Response (String)
  * @Errors: View **(Reference 1)** This function will fail if a "non-command" function is sent when a drone is not sent to command. Also, if the function does not receive the response "Ok" from the drone, then it forces the drone to land as a safety precaution for the drone itself.
  * Desc: This function is the function through which all other functions are sent. It essentially takes the String command sent by each individual command, encodes that command, sends the command to the drone, recieves a response back from the drone (if given), then returns back the response that the drone gave.
  
* (IMPORTANT!) drone.command()
  * @Param: None
  * @Output: None
  * @Errors: If you are already setting the drone object to connect to the same/another drone, then it will print "You are already commanding a drone" and exit.
  * Desc: This function must be called in order to send commands to the drone, like "takeoff", "land", etc... **(Reference 1)** If this is not called before, any command will print "The drone is not set to command", and then exit.

* drone.takeoff()
  * @Param: None
  * @Output: None
  * @Errors: View **(Reference 1)**
  * Desc: This command causes the drone to takeoff, generally hovering around 2-3 feet about the ground.
  
* drone.land()
  * @Param: None
  * @Output: None
  * @Errors: View **(Reference 1)**
  * Desc: This command causes the drone to land. While this is not required at the end of a program (because the drone will land itself after disconnecting), it should still be used for good programming practice purposes.
  
* drone.forward(distance)
  * @Param: distance (20cm - 500cm)
  * @Output: None
  * @Errors: View **(Reference 1)** Also, **(Reference 2)** if something is sent to the drone that is not an "int" or it is not between 20 and 500, a response will be given back as "Please enter an integer for the distance" or "The distance entered must be between 20 and 500" respectively and exit.
  * Desc: This command causes the drone to go forwards a specified number of centimeters relative to its current location.
  
* drone.back(distance)
  * @Param: distance (20cm - 500cm)
  * @Output: None
  * @Errors: View **(Reference 1)** and **(Reference 2)**
  * Desc: This command causes the drone to go backwards a specified number of centimeters relative to its current location.

* drone.left(distance)
  * @Param: distance (20cm - 500cm)
  * @Output: None
  * @Errors: View **(Reference 1)** and **(Reference 2)**
  * Desc: This command causes the drone to go left a specified number of centimeters relative to its current location.
  
* drone.right(distance)
  * @Param: distance (20cm - 500cm)
  * @Output: None
  * @Errors: View **(Reference 1)** and **(Reference 2)**
  * Desc: This command causes the drone to go right a specified number of centimeters relative to its current location.
  
* drone.up(distance)
  * @Param: distance (20cm - 500cm)
  * @Output: None
  * @Errors: View **(Reference 1)** and **(Reference 2)**
  * Desc: This command causes the drone to go upwards a specified number of centimeters relative to its current location.  
  
* drone.down(distance)
  * @Param: distance (20cm - 500cm)
  * @Output: None
  * @Errors: View **(Reference 1)** and **(Reference 2)**
  * Desc: This command causes the drone to go downwards a specified number of centimeters relative to its current location.
  
* drone.cw(degrees)
  * @Param: degrees
  * @Output: None
  * @Errors: View **(Reference 1)**, also **(Reference 3)** if something is sent to the drone that is not an "int" or it is not between 1 and 3600, a response will be given back as "Please enter an integer for the degrees" or "The degrees entered must be between 1 and 3600" respectively and exit.
  * Desc: This command causes the drone to turn clockwise relative to its current heading.

* drone.cw(degrees)
  * @Param: degrees
  * @Output: None
  * @Errors: View **(Reference 1)** and **(Reference 3)**
  * Desc: This command causes the drone to turn counter-clockwise relative to its current heading.

* drone.get_height() **(WIP)**
  * @Param: None
  * @Output: Height
  * @Errors: View **(Reference 1)**
  * Desc: This command gets information from the drone about how high it is, relative to it's current "ground"
