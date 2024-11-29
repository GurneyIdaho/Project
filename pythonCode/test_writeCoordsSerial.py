import pytest
from serial import Serial
from serialComms import write_coordinates
def test_write_coords_serial():
    portName = 'COM3' #check port of connected board and change as needed
    arduino = Serial(port=portName,   baudrate=115200, timeout=.1) #initiate communication with board on com3=
    assert write_coordinates(arduino,1,68) == "Position(1,68)"
    assert write_coordinates(arduino,10,3.2) == "Position(10,3)"
    assert write_coordinates(arduino,370,-95) == "Position(8,95)"

def test_error():
    portName = 'COM3' #check port of connected board and change as needed
    arduino = Serial(port=portName,   baudrate=115200, timeout=.1) #initiate communication with board on com3
    with pytest.raises(TypeError):
        write_coordinates(arduino,"cat","dog")

test_write_coords_serial()
test_error()

