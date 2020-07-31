For my drone.py class, I mainly based the program off of the information provided on this message board:
https://steemit.com/python/@makerhacks/programming-the-ryze-dji-tello-with-python

* This helped TREMENDOUSLY, and for anyone learning how to connect to the drone originally I highly consider starting their code based off of this.
* Essentially it presents the information of how to create a socket to connect to the drone originally, as well as how to receive information (like errors and what not) and also how to send basic commands.

Another good resource is the Tello SDK 2.0 User Guide:
https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf

* This helps show what kind of information needs to be sent to the drone (essentially the style in which the commands need to be written)
* Note: In order to connect to the drone you need to create a connection (obviously). However, before you can send any commands to the drone (like "takeoff","land", etc...) you need to first send the drone the "command" command. Then you are able to send whatever other commands you like. (detailed in the Tello SDK 2.0 User Guide)

Also, for more information on creating sockets and threading, I reccomend reading the python3 documents for both.
https://docs.python.org/3/library/socket.html
https://docs.python.org/3/library/threading.html

General notes on my python class:
* So, the main purpose of my python class is to create a simple "import" that students could potentially use to send commands to drones easily.
* It is fairly easy to use and I even got to try it out on my little brother who really liked it! (I list the notes that I made from running the test with him on a second document titled: "Brother_Test")
* I really tried to reduce the amount of code that I used so that students (if they are interested) could look at the source code and figure out how it works!
* My class also runs a check 0.3 seconds after sending a command to the drone to make sure that it responds with "ok". If it does not respond with "ok", the program is shut down due to non-responsivity of the drone.
