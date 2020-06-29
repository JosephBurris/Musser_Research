Actual program: https://github.com/dji-sdk/Tello-Python/tree/master/Single_Tello_Test

Notes on program:
* Program Testing:
  * The program is able to successfully connect to the drone.
  * The program is able to successfully send commands to the drone, which are then carried out.
  * The program does have error-handling, and it is able to detect things such as:
    * The drone not responding to connection. (tested by not connecting via wifi to the drone)
    * Handling incorrect commands, and returning an error, then ending the program. (tested by sending improper commands to the drone, using the program)
    * Handling errors provided by the drone (like the inability to perform a command). (Tested by trying to command the drone to land after it already landed)
  
* Connecting to program:
  * The original connection to the drone itself is accomplished in the tello.py document.
  * It appears to connect to the drone itself using the socket and threading python libraries to connect to the drone.
  * 
