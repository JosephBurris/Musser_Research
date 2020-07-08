import socket

class Drone:
    __tello = None
    __commanding = False
    __connection = None
    
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

    def send_command(self,command):
        if (self.__commanding == False):
            print("The drone is not set to command")
            self.disconnect()
            exit()
        try:
            message = command
            encoded = message.encode()

            self.__connection.sendto(encoded, self.__tello)
            #socket.sendto(encoded, tello)

            #print("made it past sendto")
            
            data, ip = self.__connection.recvfrom(1024)
            #data, ip = socket.recvfrom(1024)

            #print("made it past recvfrom")
                
            print("{}: {}".format(ip, data.decode()))
            print("Command Sent!")
            
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

    
