# Parent class: Device
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"Device: {self.brand} {self.model}"

# Child class: Smartphone
class Smartphone(Device):
    def __init__(self, brand, model, os, storage, ram):
        super().__init__(brand, model)
        self.os = os
        self.storage = storage
        self.ram = ram

    def display_info(self):
        return (f"Smartphone: {self.brand} {self.model}\n"
                f"OS: {self.os}, Storage: {self.storage}GB, RAM: {self.ram}GB")

    def upgrade_storage(self, additional_storage):
        self.storage += additional_storage
        return f"Storage upgraded! New storage: {self.storage}GB"

# Example usage
my_phone = Smartphone("Apple", "iPhone 14", "iOS", 128, 6)
print(my_phone.display_info())
print(my_phone.upgrade_storage(64))
