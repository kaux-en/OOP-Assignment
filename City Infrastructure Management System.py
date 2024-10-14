#Task 1: Vehicle Registration System

class Vehicle:
    def __init__(self, reg_number, vehicle_type, owner):
        self.reg_number = reg_number
        self.vehicle.type = vehicle_type
        self.owner = owner

    def update_owner(self):
        owner = self.owner
        owner_name = input("Enter the updated owner name: ").lower()
        new_name = owner.replace(owner, owner_name)
        print(f"Vehicle 1's owner changed from {owner} to {new_name}")


vehicle1 = Vehicle(123, 'truck', 'Lisa Smith')

vehicle1.update_owner()


