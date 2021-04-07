# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 16:24:21 2021

@author: Teddie Karahalis
"""

class Package:
    def __init__(self, customer_name, recipient_name, customer_address, recipient_address, 
                 weight, tracking_number, location):
        self.customer_name = customer_name
        self.recipient_name = recipient_name
        self.customer_address = customer_address
        self.recipient_address = recipient_address
        self.weight = weight
        self.tracking_number = tracking_number
        self.status = "Dropped off"
        self.status_history = [self.status]
        self.location = location
        self.location_history = [self.location]
        
    # returns string of information that would be printed on package label
    def create_package_label(self):
        package_label = self.customer_name 
        package_label += "\nWeight: " + str(self.weight) 
        package_label += "\n" + self.customer_address
        package_label += "\nShip to:" + "\n" + self.recipient_name 
        package_label += "\n" + self.recipient_address
        package_label += "\nTracking Number: " + str(self.tracking_number)
        return package_label
    
    # returns string of list of corresponding statuses and histories of the package
    def get_package_history(self): 
        package_history = []
        for i in range(len(self.status_history)):
            package_history.append(self.status_history[i] + " in " + self.location_history[i])
        return package_history
    
    # changes status and location attributes of the package and adds them to the package history
    def update_status(self, new_status, new_location):
        self.status_history.append(new_status)
        self.status = new_status
        self.location_history.append(new_location)
        self.location = new_location
        
    # replaces existing package status history with new list of statuses
    def change_status_history(self, new_status_history):
        self.status_history = new_status_history
        
    # replaces existing package location history with new list of locations
    def change_location_history(self, new_location_history):
        self.location_history = new_location_history


###################################### FAKE DATA ######################################
"""
package1 = Package("Brenda Smith", "Karen Johnson", "143 Figtree Ln \nAuburn, AL 36832", 
                   "500 Griffin Place \nTuscaloosa, AL 35404", 5, 30012, "Auburn, Al")
package1.change_location_history(["Auburn, AL", "Alexander City, AL", "Birmingham, AL", "Tuscaloosa, AL"])
package1.change_status_history(["Dropped off", "In transit", "In holding", "Delivered"])
print("\nFake Data: \n" + package1.create_package_label())
print(package1.get_package_history())

package2 = Package("Dave Byrne", "Mike Michaels", "731 Princeton Ave \nCullman, AL 35057", 
                   "2509 Melbourne Dr \nMontgomery, AL 36121", 1, 54098, "Cullman, Al")
package2.change_location_history(["Cullman, AL", "Clanton, AL", "Birmingham, AL"])
package2.change_status_history(["Dropped of", "In transit", "In holding"])
print("\n" + package2.create_package_label())
print(package2.get_package_history())

package3 = Package("Monique Williams", "Joe Dill", "407 Toga St \nGadsden, AL 35906", 
                   "555 Pinkleton Cir \nMuscle Shoals, AL 35646", 2, 27350, "Gadsden, Al")
package3.change_location_history(["Gadsden, AL", "Cullman, AL"])
package3.change_status_history(["Dropped off", "In transit"])
print("\n" + package3.create_package_label())
print(package3.get_package_history())
"""