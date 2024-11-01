# Base class
class MobilePhone:
    def __init__(self, screen_type="Touch Screen", network_type="4G/5G", dual_sim=False, 
                 front_camera="12MP", rear_camera="48MP", ram="4GB", storage="64GB"):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def display_specs(self):
        print("Screen Type:", self.screen_type)
        print("Network Type:", self.network_type)
        print("Dual SIM:", "Yes" if self.dual_sim else "No")
        print("Front Camera:", self.front_camera)
        print("Rear Camera:", self.rear_camera)
        print("RAM:", self.ram)
        print("Storage:", self.storage)

    def make_call(self, number):
        print(f"Calling {number}...")

    def receive_call(self, number):
        print(f"Receiving a call from {number}...")

    def take_a_picture(self):
        print("Taking a picture using the camera...")

    def send_message(self, number, message):
        print(f"Sending message to {number}: '{message}'")


# Child class: Apple
class Apple(MobilePhone):
    def __init__(self, model, dual_sim=False, front_camera="12MP", rear_camera="48MP", ram="4GB", storage="64GB"):
        # Call the parent class constructor using super()
        super().__init__(screen_type="Touch Screen", network_type="4G/5G", 
                         dual_sim=dual_sim, front_camera=front_camera, 
                         rear_camera=rear_camera, ram=ram, storage=storage)
        self.model = model

    def display_specs(self):
        print(f"Apple {self.model} Specifications:")
        super().display_specs()
        print()


# Child class: Samsung
class Samsung(MobilePhone):
    def __init__(self, model, dual_sim=True, front_camera="16MP", rear_camera="48MP", ram="4GB", storage="64GB"):
        # Call the parent class constructor using super()
        super().__init__(screen_type="Touch Screen", network_type="4G/5G", 
                         dual_sim=dual_sim, front_camera=front_camera, 
                         rear_camera=rear_camera, ram=ram, storage=storage)
        self.model = model

    def display_specs(self):
        print(f"Samsung {self.model} Specifications:")
        super().display_specs()
        print()


# Create instances of Apple and Samsung phones and demonstrate their functionalities
iphone = Apple(model="iPhone 13", dual_sim=False, front_camera="12MP", rear_camera="48MP", ram="4GB", storage="128GB")
samsung_galaxy = Samsung(model="Galaxy S21", dual_sim=True, front_camera="16MP", rear_camera="48MP", ram="8GB", storage="128GB")

# Display specifications for each phone
iphone.display_specs()
samsung_galaxy.display_specs()

# Demonstrate functionalities
iphone.make_call("123-456-7890")
iphone.receive_call("098-765-4321")
iphone.take_a_picture()
iphone.send_message("123-456-7890", "Hello from iPhone!")

samsung_galaxy.make_call("321-654-0987")
samsung_galaxy.receive_call("789-012-3456")
samsung_galaxy.take_a_picture()
samsung_galaxy.send_message("321-654-0987", "Hello from Samsung Galaxy!")
