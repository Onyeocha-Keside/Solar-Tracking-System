class LogEntry:
    def __init__(self, timestamp, optimal_azimuth, optimal_elevation, verified_azimuth, verified_elevation):
        self.timestamp = timestamp
        self.optimal_azimuth = optimal_azimuth
        self.optimal_elevation = optimal_elevation
        self.verified_azimuth = verified_azimuth
        self.verified_elevation = verified_elevation