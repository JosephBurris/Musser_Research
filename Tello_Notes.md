To begin with learning tello drones, I would first recommend looking at the Tello manual here: https://dl-cdn.ryzerobotics.com/downloads/Tello/20180212/Tello+User+Manual+v1.0_EN_2.12.pdf
* This helps you get aquainted with the Tello, flying it and what proper connection to it looks like (plus it's just fun to fly the drone).

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
* I used these to figure out how to both send and receive messages to and from the drones. (This was something that I really had no idea of how to do before this research, and was very good practice)
* Also, this gives information on how "decode()" works.

General notes on my python class:
* So, the main purpose of my python class is to create a simple "import" that students could potentially use to send commands to drones easily.
* It is fairly easy to use and I even got to try it out on my little brother who really liked it! (I list the notes that I made from running the test with him on a second document titled: "Brother_Test")
* I really tried to reduce the amount of code that I used so that students (if they are interested) could look at the source code and figure out how it works!
* My class also runs a check 0.3 seconds after sending a command to the drone to make sure that it responds with "ok". If it does not respond with "ok", the program is shut down due to non-responsivity of the drone.

Another good resource that I found on tello drones was this github repo: https://github.com/dji-sdk/Tello-Python
* This provides an example (a fairly complicated one) of prepping, sending, and receiving information to Tello drones.
* Note: This is also a VERY good place to start if you are looking at providing video from tello drones, this is GOOD place to start (I will continue to look at this on my own time)
* Also, I wanted to note that the way that this program handles sending commands from the user is not my favorite way. I kind of dislike how you have to import  a file with simply written commands. I decided to stray away from this style for my class because I wanted to create a simple object for students to interact with (similar to something like the python turtle class)

This repo that I found also helped with receiving information from the tello drones: https://github.com/dji-sdk/Tello-Python/blob/master/Tello_Video_With_Pose_Recognition/tello.py
* It details a little into how to properly receive information back from tellos, as well as the kind of information they do give back (Strings).
* I found this fairly late into my research, and it also appears to be a really good resource for 

Particular struggles with programming the drone:
* 
