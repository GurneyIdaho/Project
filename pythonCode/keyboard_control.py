#stolen (copilot)
#created 3/12/2024
import keyboard
from serial import Serial
from position_class import Position
from serialComms import write_coordinates
class servo_position(Position): 
    def __init__(self, x: int, y: int, arduino): 
        super().__init__(x, y) 
        self.arduino = arduino
        self.send_position()
    def send_position(self): 
        write_coordinates(self.arduino,self.x,self.y)
    def yaw_left(self):
        self.updateX(+5)
        self.send_position()
    def yaw_right(self):
        self.updateX(-5)
        self.send_position()
    def pitch_up(self):
        self.updateY(+5)
        self.send_position()
    def pitch_down(self):
        self.updateY(-5)
        self.send_position()
        


portName = 'COM3' #check port of connected board and change as needed
arduino = Serial(port=portName,   baudrate=115200, timeout=.1) #initiate communication with board on com3 
print("Press the left arrow to decrease and the right arrow to increase the number. Press 'esc' to exit.")
position = servo_position(0,0,arduino)

# Bind the arrow keys to the respective functions
keyboard.on_press_key("left", lambda _: position.yaw_left())
keyboard.on_press_key("right", lambda _: position.yaw_right())
keyboard.on_press_key("up", lambda _: position.pitch_up())
keyboard.on_press_key("down", lambda _: position.pitch_down())
# Keep the program running to listen for key events
keyboard.wait('esc')
