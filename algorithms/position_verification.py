from utils.sensor_utils import read_position_sensors
from config import ERROR_MARGIN

def verify_position(optimal_position):
    measured_position = read_position_sensors()
    if abs(optimal_position[0] - measured_position[0]) > ERROR_MARGIN or \
       abs(optimal_position[1] - measured_position[1]) > ERROR_MARGIN:
        # Trigger correction routine
        return optimal_position
    return measured_position