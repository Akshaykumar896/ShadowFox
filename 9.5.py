class MobilePhone:
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def make_call(self, number):
        print(f"Calling {number}...")

    def receive_call(self, number):
        print(f"Receiving call from {number}...")

    def take_a_picture(self):
        print("Taking a picture...")

    def display_specs(self):
        print(f"{self.__class__.__name__} Specifications:")
        print(f"Screen Type: {self.screen_type}")
        print(f"Network Type: {self.network_type}")
        print(f"Dual SIM: {'Yes' if self.dual_sim else 'No'}")
        print(f"Front Camera: {self.front_camera}")
        print(f"Rear Camera: {self.rear_camera}")
        print(f"RAM: {self.ram}")
        print(f"Storage: {self.storage}")
        print()

class Apple(MobilePhone):
    def __init__(self, model, dual_sim, front_camera, rear_camera, ram, storage):
        super().__init__(screen_type="Touch Screen", network_type="4G/5G", dual_sim=dual_sim,
                         front_camera=front_camera, rear_camera=rear_camera, ram=ram, storage=storage)
        self.model = model

    def display_specs(self):
        super().display_specs()
        print(f"Model: {self.model}")

class Samsung(MobilePhone):
    def __init__(self, model, dual_sim, front_camera, rear_camera, ram, storage):
        super().__init__(screen_type="Touch Screen", network_type="4G/5G", dual_sim=dual_sim,
                         front_camera=front_camera, rear_camera=rear_camera, ram=ram, storage=storage)
        self.model = model

    def display_specs(self):
        super().display_specs()
        print(f"Model: {self.model}")

# Creating different objects of the Apple class
iphone_12 = Apple(model="iPhone 12", dual_sim=False, front_camera="12MP", rear_camera="12MP", ram="4GB", storage="64GB")
iphone_12_pro = Apple(model="iPhone 12 Pro", dual_sim=False, front_camera="12MP", rear_camera="12MP", ram="6GB", storage="128GB")
iphone_13 = Apple(model="iPhone 13", dual_sim=False, front_camera="12MP", rear_camera="48MP", ram="4GB", storage="128GB")
iphone_13_pro_max = Apple(model="iPhone 13 Pro Max", dual_sim=True, front_camera="12MP", rear_camera="12MP", ram="6GB", storage="256GB")

# Creating different objects of the Samsung class
samsung_galaxy_s21 = Samsung(model="Samsung Galaxy S21", dual_sim=True, front_camera="10MP", rear_camera="64MP", ram="8GB", storage="128GB")
samsung_galaxy_note20 = Samsung(model="Samsung Galaxy Note 20", dual_sim=True, front_camera="10MP", rear_camera="108MP", ram="8GB", storage="256GB")
samsung_galaxy_a52 = Samsung(model="Samsung Galaxy A52", dual_sim=False, front_camera="32MP", rear_camera="64MP", ram="6GB", storage="128GB")
samsung_galaxy_z_flip = Samsung(model="Samsung Galaxy Z Flip", dual_sim=False, front_camera="10MP", rear_camera="12MP", ram="8GB", storage="256GB")

# Displaying specifications for each Apple phone
iphone_12.display_specs()
iphone_12_pro.display_specs()
iphone_13.display_specs()
iphone_13_pro_max.display_specs()

# Displaying specifications for each Samsung phone
samsung_galaxy_s21.display_specs()
samsung_galaxy_note20.display_specs()
samsung_galaxy_a52.display_specs()
samsung_galaxy_z_flip.display_specs()
