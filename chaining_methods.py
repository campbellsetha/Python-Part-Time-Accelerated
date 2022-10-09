class User:
    def __init__(self):
        self.first_name = "Edward"
        self.last_name = "Blakely"
        self.email = "blakele_SS314@blakelybehemoths.com"
        self.age = 42
        self.is_rewards_member = False
        self.gold_card_points = 250

    def display_info(self):
        print(self.first_name, self.last_name, self.email, self.age, "Is rewards member: ", self.is_rewards_member, "Points available: ", self.gold_card_points)
        return self

    def enroll(self):
        if(self.is_rewards_member == True):
            print("User already a member")
            return self
        else:
            self.is_rewards_member = True
        return self

    def spend_points(self, amount):
        if((self.gold_card_points - amount ) < 0):
            print("Not enough points available!")
        else:
            self.gold_card_points = self.gold_card_points - amount
        return self

new_co = User()
new_co.display_info().enroll().display_info().spend_points(50).display_info().enroll()

new_xo = User()
new_cob = User()

new_xo.enroll().spend_points(80).display_info()
new_cob.display_info().spend_points(300)
