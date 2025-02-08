import random

class SensorSuite:
    def __init__(self):
        self.required_params = ['temperature', 'air_quality', 'soil_moisture', 'soil_nutrients']

    def scan_environment(self):
        print("Scanning environment...")
        # Simulate sensor data with random values
        sensor_data = {
            'temperature': random.uniform(15, 35),   # °C
            'air_quality': random.uniform(50, 150),    # Air quality index
            'soil_moisture': random.uniform(10, 40),   # Percentage
            'soil_nutrients': random.uniform(1, 10)    # Arbitrary nutrient units
        }
        print("Sensor data acquired:", sensor_data)
        return sensor_data

    def data_complete(self, sensor_data):
        # Check that all required sensor values are present
        for param in self.required_params:
            if param not in sensor_data or sensor_data[param] is None:
                return False
        return True
