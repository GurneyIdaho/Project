#simple test to communicate coordinates to a connected arduino board
#created by Charlie Jones, based on an example in the pyserial docs
#copilot for regex
#date created: 26/11/24
#last edited: 28/11/24
from serial import Serial
import time
import re

def write_coordinates(arduino,yaw: int,pitch: int):
    yaw = round(float(yaw))%180 #ensure values of proper type and in proper range
    pitch = round(float(pitch))%180        
    message = f"<{yaw},{pitch}>"
    arduino.write(bytes(message,   'utf-8')) #writes info to the board in the form <yaw,pitch>, decoded and acted on at the other end
    time.sleep(0.05)
    reply = str(arduino.readline())
    match = re.search(r'<(.*?)>', reply)
    trimmedReply = match.group(1)
    return trimmedReply


if __name__=="__main__":
    portName = 'COM3' #check port of connected board and change as needed
    arduino = Serial(port=portName,   baudrate=115200, timeout=.1) #initiate communication with board on com3 
    while True:
        yaw,pitch = input("Enter [yaw],[pitch]\n").split(",")
        reply = write_coordinates(arduino,yaw,pitch)
        print(reply) #prints the boards reply (including position)
        
