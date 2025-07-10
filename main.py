from utils.time_utils import get_current_time_and_date
from algorithms.astronomical_algorithm import calculate_optimal_position
from algorithms.position_verification import verify_position
from controllers.tracker_controller import adjust_tracker
from utils.logging_utils import log_data
from database.db_manager import initialize_db

def main_control_loop():
    initialize_db()
    while True:
        time_and_date = get_current_time_and_date()
        optimal_position = calculate_optimal_position(time_and_date)
        verified_position = verify_position(optimal_position)
        adjust_tracker(verified_position)
        log_data(time_and_date, optimal_position, verified_position)

if __name__ == "__main__":
    main_control_loop()