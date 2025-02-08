class AIEngine:
    def analyze_environment(self, sensor_data):
        print("AI analyzing environmental data...")
        optimal_sites = []
        base_lat, base_lon = 12.905, 77.505
        # Simple heuristic: high soil moisture and nutrient levels indicate favorable planting conditions
        if sensor_data['soil_moisture'] > 20 and sensor_data['soil_nutrients'] > 5:
            optimal_sites.append({'lat': base_lat, 'lon': base_lon})
            optimal_sites.append({'lat': base_lat + 0.001, 'lon': base_lon + 0.001})
        else:
            optimal_sites.append({'lat': base_lat - 0.001, 'lon': base_lon - 0.001})
        print("Optimal planting sites determined:", optimal_sites)
        return optimal_sites
