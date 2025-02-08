class IoTTracker:
    def __init__(self, location):
        self.location = location
        self.status = "Inactive"

    def activate(self):
        print("Activating IoT tracker at location:", self.location)
        self.status = "Active"
        self.send_status()

    def send_status(self):
        print("Tracker status:", self.status, "at", self.location)
