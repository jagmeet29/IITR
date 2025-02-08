class Drone:
    def __init__(self):
        self.status = "Initialized"

    def initialize(self):
        print("Drone systems initializing...")
        self.status = "Ready"
    
    def takeoff(self):
        if self.status == "Ready":
            print("Drone taking off...")
            self.status = "In Flight"
        else:
            print("Drone not ready for takeoff.")
    
    def navigate_to(self, coordinates):
        print("Navigating to coordinates:", coordinates)

    def plant_seed(self):
        if self.status == "In Flight":
            print("Planting seed at current location...")
        else:
            print("Drone not in flight. Cannot plant seed.")

    def land(self):
        if self.status == "In Flight":
            print("Drone landing...")
            self.status = "Landed"
        else:
            print("Drone already landed or not in flight.")
