import pytest
from serial import Serial
from serialComms import write_coordinates
def test_write_coords_serial():
    portName = 'COM3' #check port of connected board and change as needed
    arduino = Serial(port=portName,   baudrate=115200, timeout=.1) #initiate communication with board on com3
    yaws   = [1, 10, 45, 370, 20, 35]
    pitches   = [68, 3.2, 95, -10, 50, 34]
    for i in range(len(yaws)):
        assert write_coordinates(arduino,yaws[i],pitches[i]) == f"Position({yaws[i]},{pitches[i]})"

def test_error():
    portName = 'COM3' #check port of connected board and change as needed
    arduino = Serial(port=portName,   baudrate=115200, timeout=.1) #initiate communication with board on com3
    with pytest.raises(TypeError):
        write_coordinates(arduino,"cat","dog")

