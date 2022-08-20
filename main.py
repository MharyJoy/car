
# Example of Class
# class Car:
#       ATTRIBUTES
#     def __init__(self, seats): # initialise attributes
#         self.seats = seats
#
#         # it is the same as
#         my_car = Car(5) # -- Inside the paranthesis is the paramaters self is always included
#         my_car.seats = 5

# METHOD
# class Car:
#     def enter_race_mode():
#         self.seats = 2
#
# my_car.enter_race_mode()

class User:
    # All objects created using the class will have followers equal to the value of 0, along with user_id and username
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0  # default values  instead of having another parameters called 'followers' we can just set a value equal to 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "angela") # if you check to see what 'User' type is you'll get a class
user_2 = User("002", "jack")

