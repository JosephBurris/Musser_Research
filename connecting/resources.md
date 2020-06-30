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
  * The socket and threading libraries both require the ip and port provided from the tello drone.
  * Socket then uses the socket sending command, and the bind method to connect to the drone.
  * Then, the threading library starts threading using the Thread method and then starting it.
 
* Sending commands to the drone:
  * Really, the only bit of code, after setup has been done to connect to the drone, to send information is with the socket -> send to <- function.
  * Note: The code I was looking at also has a system in place to create a log of the commands sent to the drone, as well as error handling.
 
* Notes on Tello Edu application:
  * I really do believe that, for a future class, this might be a good way to begin teaching programming.
    * However, it does depend on the level of programming expertise that the students will have. If they do have higher programming experience, then connecting to the dronce shouldn't be a problem.
  * I do have a couple of suggestions for possibly slowly introducing people to the basics of programming.
    * Since the base-level of programming provided by the app is not really... programming, the main idea that comes to mind is to provide the students with code that already connects them to the drone. Then, the main challenges at first would be to just send commands to the drone.
    * Also, for the beggining of the class, a separate class could be created for the students use. With functions built into it like: forwards(), left90(), etc...
    * This would just give students an idea of what they could do with the drone. (Perhaps provide them with a document with functions on it?)

* Notes on own application:
  * My program is a close approximation to this: https://steemit.com/python/@makerhacks/programming-the-ryze-dji-tello-with-python
  * The only thing that I did differently was to include multiple try/except clauses to run just a couple of commands.
  * Note: One confusing bit was having to send the "command" command to take control of the drone initially.
  * Question: How does the drone handle a chain of commands? Is it done through something like a stack? (A.K.A- pull off command to command) Or is there some sort of timing involved?

* Closing thoughts:
  * So, I really do believe that the best way to teach basic programming using drone tech is to provide a pre-written class that students could perform commands from.
  * One that I am working on on my local machine right now is my Drone class/document. When I'm done with this, I hope to be able to be able to both start a connection to the drone, and create several, premade functions that would allow students to pull from it. (Note: Still a work in progress)
