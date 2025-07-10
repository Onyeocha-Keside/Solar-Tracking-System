from utils.motor_utils import rotate_motor

def adjust_tracker(position):
    rotate_motor(position[0])  # Adjust azimuth
    rotate_motor(position[1])  # Adjust elevation