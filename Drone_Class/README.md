**This is a documentation page on how to use the Drone class, provided in this folder**

**Opening Notes:**
* Connecting to the Tello drone with a laptop:
  * Press the button on the side of the drone quickly, and if the drone has power, its light on the side should blink red, then shortly after flash multiple different colors.
  * While the light is blinking multiple different colors, look at your networks options for something similar to TELLO...
  * After you see the correct option, connect to it after the light starts rappidly flashing yellow, signaling proper connection.
  * Now, you should be able to run your code!
* In order to use this class, the drone.py file must be in your working folder, and the beginning of your code must include the following line:
  * from drone import *
* Creation of a new drone object:
  * In order to create a drone object, the drone object must be provided with a valid IP and Port.
    * In the format of this: test = new Drone("exampleIP"(String),1111(Int))
    * Example: test = new Drone("192.168.10.1", 8889)
    
**General Notes on Python Objects**
* All objects are created in the form: test = Object(parameter1, parameter2, etc...)
* All functions of objects are called in the form: test.function(parameter1, parameter2, etc...)

**Drone Methods/Functions**
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
