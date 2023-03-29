
from pyfirmata import *
board = Arduino('COM3')
board.servo_config(9, min_pulse=544, max_pulse=2400, angle=0)
print("Unlocked")