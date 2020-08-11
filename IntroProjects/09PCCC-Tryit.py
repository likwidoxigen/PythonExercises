from random import randint

class Restaurant:
    """Resterrant class"""
    texture = "meaty"

    def __init__(self, name, food_type, texture):
        self.name = name
        self.food_type = food_type
        self.texture = texture
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.name} is a {self.food_type} restaurant.")

    def open_restaurant(self):
        print(f'{self.name} is now open')

    def __len__(self):
        return 6

    def get_restaurant(self):
        return f"{self.name} is a {self.food_type} restaurant. And has served {self.number_served} patrons."\

    def set_number_served(self, total_served):
        self.number_served = total_served
    
    def increment_number_served(self):
        self.number_served += 1
    
    def reset_nubmer_served(self):
        self.number_served = 0

    __str__ = get_restaurant


tacos = Restaurant("Tacoria", "Tacos", "1")
burgers = Restaurant("Burger Palace", "Meat Patty integrator", "2")
pizza = Restaurant("Pizza City", "Cheese dough sauce assembler", "3")

print(tacos)
tacos.set_number_served(68)
print(tacos)
tacos.increment_number_served()
print(tacos)
tacos.reset_nubmer_served()
print(tacos)
tacos.increment_number_served()
print(tacos)
burgers.describe_restaurant()
pizza.describe_restaurant()


print(len(tacos))
print(tacos)
print(tacos.texture)
print(Restaurant.texture)
print(burgers.__class__.texture)

class Ice_Cream_Stand(Restaurant): 
    """ Defines a frozen treat restaurant """
    def __init__(self, name, food_type, texture):
        super().__init__(name,food_type,texture)
        self.flavors = ["Vanilla", "Mint Chocolate Chip", "Pistachio"]
    
    def get_flavors(self):
        return self.flavors

ics = Ice_Cream_Stand("The Cold Spoon", "Frozen Treats", "Cold and Creamy")
print(ics)
print(ics.get_flavors())

class User:
    """Holds user Information"""
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.username = None
        self.email = None

    def setLoginInformation(self, username, email):
        self.username = username
        self.email = email

    def __str__(self):
        return f'{self.first_name} {self.last_name}\'s username is {self.username} and their email is {self.email}'


user1 = User("First", "Last")
user1.setLoginInformation("username", "email")
print(user1)
#python 3.8 print(f'{varName=}') for easy and convenient way to see what a variable is


class Privilege:
    def __init__(self, type):
        if (type == 'ADMIN'):
            self.privileges = ["Read","Write","Updtate","Delete"]
        else:
            self.privileges = ["Read","Update"]
    
    def show_privileges(self):
        print(self.privileges)

class Administrator(User):
    def __init__(self, first, last):
        super().__init__(first,last)
        self.privileges = Privilege("ADMIN")

adm = Administrator("Bryce","Smith")
print(adm)
adm.privileges.show_privileges()


print(randint(0,10))