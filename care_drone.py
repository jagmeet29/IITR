import random

class CareDrone:
    def __init__(self):
        self.status = "Idle"

    def initialize(self):
        print("Care drone initializing systems...")
        self.status = "Ready"

    def monitor_plants(self, sites):
        print("Monitoring plant health at sites:", sites)
        plant_health = {}
        for site in sites:
            # Simulate a health index between 0 and 1
            plant_health[str(site)] = {'health_index': random.uniform(0, 1)}
        print("Plant health data:", plant_health)
        return plant_health

    def analyze_health(self, plant_health):
        # If any plant's health index is below 0.5, care is needed
        for site, data in plant_health.items():
            if data['health_index'] < 0.5:
                print("Care needed at site:", site)
                return True
        return False

    def execute_care(self, plant_health):
        print("Executing care instructions...")
        for site, data in plant_health.items():
            if data['health_index'] < 0.5:
                print("Watering and applying nutrients at site:", site)
                # Improve health index after care (simulation)
                plant_health[site]['health_index'] += 0.3
        print("Updated plant health after care:", plant_health)
