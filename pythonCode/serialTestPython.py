#simple test to communicate coordinates to a connected arduino board
#created by Charlie Jones, based on an example in the pyserial docs
#date created: 26/11/24
#last edited: 28/11/24
from serial import Serial
import time
portName = 'COM3' #check port of connected board and change as needed
arduino = Serial(port=portName,   baudrate=115200, timeout=.1) #initiate communication with board on com3 



while True:
    message = "<"+input("Enter [yaw],[pitch]\n")+">"
    arduino.write(bytes(message,   'utf-8')) #writes info to the board in the form <yaw,pitch>, decoded and acted on at the other end
    time.sleep(0.05)
    reply =arduino.readline()
    print(reply) #prints the boards reply (including posigion)
