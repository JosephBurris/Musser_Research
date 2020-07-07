**This is a documentation page on how to use the Drone class, provided in this folder**

**Opening Notes:**
* Connecting to the Tello drone with a laptop:
  * Press the button on the side of the drone quickly, and if the drone has power, its light on the side should blink red, then shortly after flash multiple different colors.
  * While the light is blinking multiple different colors, look at your networks options for something similar to TELLO...
  * After you see the correct option, connect to it and the button should start rappidly flashing yellow, signaling proper connection.
* In order to use this class, the drone.py file must be in your working folder, and the beginning of your code must include the following line:
  * from drone import *
* Creation of a new drone object:
  * In order to create a drone object, the drone object must be provided with a valid IP and Port.
    * In the format of this: test = new Drone("exampleIP"(String),1111(Int))
    * Example: test = new Drone("192.168.10.1", 8889)
    
**General Notes on Python Objects**
* All objects are created in the form: test = Object(parameter1, parameter2, etc...)
* All functions 

**Drone Methods/Functions**
* 
