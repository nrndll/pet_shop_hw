# WRITE YOUR FUNCTIONS HERE

# given a dict, this will return the value at "name"
def get_pet_shop_name(given_dict):
    return given_dict["name"]

# given a dict, this will return the value within "admin" dict at "total_cash"
def get_total_cash(given_dict):
    return given_dict["admin"]["total_cash"]

# value of cash will be added to total_cash. 
def add_or_remove_cash(given_dict, cash):
    given_dict["admin"]["total_cash"] += cash