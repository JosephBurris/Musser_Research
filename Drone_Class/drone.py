import socket
import time

class Drone:
    __tello = None
    __commanding = False
    __connection = None
    #WIP
    #__abort = None
    
    def __init__(self,ip,port):
        self.__tello = (ip,port)

    def connect(self):
        try:
            self.__connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            print(self.__connection)
    
        except socket.error:
            print("Oops, something went wrong connecting the socket")
            exit()
        print("connected!")

    def disconnect(self):
        if(self.__connection != None):
            try:
                self.__connection.close()
            except socket.error:
                print("Oops, something went wrong disconnecting the socket")
                exit()
        else:
            print("You are not connected to a drone yet")
            
            exit()

    #WIP
    #def set_abort_flag(self):
    #    self.__abort = True

    def send_command(self,command):
        if (self.__commanding == False):
            print("The drone is not set to command")
            self.disconnect()
            exit()
        try:
            message = command
            encoded = message.encode()

            self.__connection.sendto(encoded, self.__tello)
            
            data, ip = self.__connection.recvfrom(1024)

            self.__abort = False


            time.sleep(0.3)
            if(data.decode() != "ok"):
                self.land()

            #Code that I could not get to work in time, but will continue to try and work on
            #timer = threading.Timer(0.3, self.set_abort_flag())

            #timer.start()
            #while data.decode() is None:
                #if self.__abort is True:
                    #break
            #timer.cancel()

            #if(self.__abort == True):
                #self.land()

            print("{}: {}".format(ip, data.decode()))
            print("Command Sent!")
            return data.decode()
            
        except:
            print("Error! {}".format(socket.error))
            exit()

    def command(self):
        if(self.__commanding == True):
            print("You are already commanding a drone")
            exit()
        self.__commanding = True
        self.send_command("command")

    def takeoff(self):
        self.send_command("takeoff")

    def land(self):
        self.send_command("land")

    def forward(self,distance):
        try:
            val = int(distance)
        except ValueError:
            print("Please enter an integer for the distance.")
            exit()
        if(val>500 or val<20):
            print("The distance entered must be between 20 and 500")
            exit()
        sendString = "forward " + str(val)
        print(sendString)
        self.send_command(sendString)

    def back(self,distance):
        try:
            val = int(distance)
        except ValueError:
            print("Please enter an integer for the distance.")
            exit()
        if(val>500 or val<20):
            print("The distance entered must be between 20 and 500")
            exit()
        sendString = "back " + str(val)
        print(sendString)
        self.send_command(sendString)

    def left(self,distance):
        try:
            val = int(distance)
        except ValueError:
            print("Please enter an integer for the distance.")
            exit()
        if(val>500 or val<20):
            print("The distance entered must be between 20 and 500")
            exit()
        sendString = "left " + str(val)
        print(sendString)
        self.send_command(sendString)

    def right(self,distance):
        try:
            val = int(distance)
        except ValueError:
            print("Please enter an integer for the distance.")
            exit()
        if(val>500 or val<20):
            print("The distance entered must be between 20 and 500")
            exit()
        sendString = "right " + str(val)
        print(sendString)
        self.send_command(sendString)

    def up(self,distance):
        try:
            val = int(distance)
        except ValueError:
            print("Please enter an integer for the distance.")
            exit()
        if(val>500 or val<20):
            print("The distance entered must be between 20 and 500")
            exit()
        sendString = "up " + str(val)
        print(sendString)
        self.send_command(sendString)


    #Note: WIP
    def down(self,distance):
        try:
            val = int(distance)
        except ValueError:
            print("Please enter an integer for the distance.")
            exit()
        if(val>500 or val<20):
            print("The distance entered must be between 20 and 500")
            exit()
        sendString = "down " + str(val)
        print(sendString)
        self.send_command(sendString)

    def cw(self,degrees):
        try:
            val = int(degrees)
        except ValueError:
            print("Please enter an integer for the degrees.")
            exit()
        if(val>3600 or val<1):
            print("The degrees entered must be between 1 and 3600")
            exit()
        sendString = "cw " + str(val)
        print(sendString)
        self.send_command(sendString)

    def ccw(self,degrees):
        try:
            val = int(degrees)
        except ValueError:
            print("Please enter an integer for the degrees.")
            exit()
        if(val>3600 or val<1):
            print("The degrees entered must be between 1 and 3600")
            exit()
        sendString = "ccw " + str(val)
        print(sendString)
        self.send_command(sendString)

    def get_height(self):
        height = self.send_command("height?")
        height = str(height)
        print(height)
        return height
        try:
            height = int(height)
        except:
            print("error, height was not returned properly")
            exit()
        return height
