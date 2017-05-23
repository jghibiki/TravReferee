import random

debugger = False

# returns roll
def roll_dice(quantity, dice_type, modification):
    total = 0
    if debugger:
        print("\nrolling " + str(quantity) + "d" + str(dice_type) + " + " + str(modification))
    for i in range(quantity):
        roll = random.randint(0, dice_type)
        if debugger:
            print("| -> " + str(roll))
        total += roll

    if debugger:
        print("Roll: " + str(total + modification))
    return total + modification


def check_bounded_value(input_value, minimum_value, maximimum_value):
    """
    This is for making sure values lie within a range
    """
    if input_value < minimum_value:
        if debugger:
            print("\nValue Below Minimum")
        return minimum_value
    else:

        if input_value > maximimum_value:
            if debugger:
                print("\nValue Above Maximum")
            return maximimum_value

        else:
            return input_value


class World(object):
    def __init__(self, manual=None, size=None, starport_quality=None, atmosphere_type=None,
                 hydrographic_percentage=None, population=None, government_type=None,
                 law_level=None, tech_level=None, list_of_bases=None, trade_codes=None,
                 travel_code=None):
        if manual is not None:
            self.size = size
            self.starport_quality = starport_quality
            self.atmosphere_type = atmosphere_type
            self.hydrographic_percentage = hydrographic_percentage
            self.population = population
            self.government_type = government_type
            self.law_level = law_level
            self.tech_level = tech_level
            self.list_of_bases = list_of_bases
            self.trade_codes = trade_codes
            self.travel_code = travel_code
        else:
            self.size = roll_dice(1, 10, 0)
            self.starport_quality = ""
            self.atmosphere_type = check_bounded_value(roll_dice(2, 6, -7) + self.size, 0, 10)
            self.hydrographic_percentage = 0
            self.population = 0
            self.government_type = 0
            self.law_level = 0
            self.tech_level = 0
            self.list_of_bases = []
            self.trade_codes = []
            self.travel_code = ""

    def __str__(self):
        return "\nsize: " + str(self.size) \
               + "\nAtmosphere Type: " + str(self.atmosphere_type)

# temp testing code
# x = World()
# print(x)
