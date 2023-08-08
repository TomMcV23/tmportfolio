from Pyro5.api import expose, behavior, serve, Daemon
#Pyro 5 stuff an creation of the rental class 
@expose
@behavior(instance_mode="single")
class rental(object): 
    def __init__(self):
        self.user_name = ["Zayne Flynt", "Sarah Ryder"]
        self.prev_rent_user = ["Zayne Flynt"]
        self.current_rent_user = ["Zayne Flynt"]
        self.user_number = [1, 2318]
        self.car_model = ["Mustang", "Focus", "Ranger", "Roadster", "Bugatti"]
        self.currently_rented = ["Bugatti"]
        self.not_currently_rented = []
        # manufacturers are stored in order and are not real ford is not from germany and so on but these are how they are meant to be ordered
        self.manufacturer_name = ["Ford", "Nissan", "Range Rover", "Dacia","Bugatti"]
        self.manufacturer_country = ["Germany", "England", "Italy", "America","Japan"]
        self.start_year = []
        self.start_month = []
        self.start_day = []
        self.end_year = []
        self.end_month = []
        self.end_day = []
        self.notrentedcar = {}
        self.rentedcar = {}
        self.completenotrented = []
        

    def add_user(self, user_name, user_number):
        # add user name and user number to the appropriate lists
        self.user_name.append(user_name), self.user_number.append(user_number)

    def return_users(self):
        #return all details related to users
        return "There are users with the names of: ",self.user_name, "with the numbers of :", self.user_number

    def add_manufacturer(self, manufacturer_name, manufacturer_country):
        #add manufacturers details such as name and their country of origin to the correct lists
        self.manufacturer_name.append(manufacturer_name)
        self.manufacturer_country.append(manufacturer_country)

    def return_manufacturers(self):
        #retun details about the manufacturers
        return "The manufacturers on file are :", self.manufacturer_name, "and they originate from these countries :", self.manufacturer_country

    def add_rental_car(self, manufacturer_name, car_model):
        #add rental car details with their related manufacturer and model
        #adds it to a dictionary to link manufacturers to car models 
        self.manufacturer_name.append(manufacturer_name)
        self.car_model.append(car_model)
        self.rentcar = dict(zip(self.manufacturer_name, self.car_model))
        if self.car_model not in self.currently_rented:
            self.not_currently_rented.append(car_model)
        

    def return_cars_not_rented(self):
        #look at the dictionary for rental cars and see which ones are not currently rented out
        for key, value in self.rentcar.items():
                if value not in self.currently_rented:
                    self.notrentedcar[key] = value
        return "These cars are not currently rented, Displayed as Car Manufacturer then Car model: ", self.notrentedcar

    def rent_car(self, user_name, car_model, year, month, day):
        #if the car is currentlty rented return 0 and displays a message saying why it failed
        if user_name not in self.user_name:
            return 0, "User does not Exist"
        elif car_model in self.rentedcar.items():
            return 0, "Car does not exist"
        #otherwise the car is available and the details are taken and saved
        #to ensure that the same car cannot be rented more than once if there are not more than one model, 
        #the car is removed from not currently rented and added to currently rented 
        #complete not rented is then updated to show what cars are available to rent
        else:
            #add rental to system only if the user exists and track the user name and what car the rented
            if user_name in self.user_name:
                self.rentals = {user_name:car_model}
                self.currently_rented.append(car_model)
                self.prev_rent_user.append(user_name)
                self.current_rent_user.append(user_name)
                self.start_year.append(year)
                self.start_month.append(month)
                self.start_day.append(day)
                self.not_currently_rented.remove(car_model)
            #update what cars are currently not rented for use in later functions
                for i in self.car_model:
                    self.completenotrented.append(i)
                for i in self.not_currently_rented:
                    self.completenotrented.append(i)
                return 1 #used to test the output, self.rentals self.currently_rented, self.prev_rent_user

    def return_cars_rented(self):
        #check the dictaionary for rental cars and compare them with the currently rented list
        #if the value is in the currently rented list then add them to the rented car dictionary then return that dictionary
            for key, value in self.rentcar.items():
                if value in self.currently_rented:
                    self.rentedcar[key] = value
            return "The cars currently rented are as follows Car Manufacturer then Car model: ", self.rentedcar, "They have been rented by the following users: ", self.current_rent_user                     
            
    def end_rental(self,user_name,car_model,year,month,day):
        #if the car model entered by the user is present in currently rented then return the car to not currently rented and remove the user and car model from both currently rented lists
        #add the date specified in the end date lists
        if user_name in self.user_name:
            self.checkrentals = {user_name:car_model}
            if self.checkrentals.keys() == self.rentals.keys():
                self.rentals.pop(user_name, None)
            if car_model in self.currently_rented:
                self.end_year.append(year)
                self.end_month.append(month)
                self.end_day.append(day)
                self.not_currently_rented.append(car_model)
                self.currently_rented.remove(car_model)
                self.current_rent_user.remove(user_name)
                #used to test fucntionality, return self.car_model, self.rentals

    def delete_car(self,car_model):
        #if the car isnt currently being rented and exists in the system delete the car 
        if car_model not in self.currently_rented:
            self.car_model.remove(car_model)
            self.not_currently_rented.remove(car_model)
            #used to test functionality, return "Car Deleted" , self.car_model, self.not_currently_rented

    def delete_user(self, user_name):
        #if the user has previously rented a car before do not delete them but if not delete them from the system
        if user_name in self.prev_rent_user:
           return 0
        else:
            self.user_name.remove(user_name)
            return 1
   
daemon = Daemon()
serve({rental: "example.rental"}, daemon=daemon, use_ns=True)

