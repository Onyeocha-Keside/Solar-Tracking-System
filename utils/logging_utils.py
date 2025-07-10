from database.db_manager import log_entry

def log_data(time_and_date, optimal_position, verified_position):
    log_entry(time_and_date, optimal_position, verified_position)