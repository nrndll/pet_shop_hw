# WRITE YOUR FUNCTIONS HERE

# given a dict, this will return the value at "name"
def get_pet_shop_name(given_dict):
    return given_dict["name"]

# given a dict, this will return the value within "admin" dict at "total_cash"
def get_total_cash(given_dict):
    return given_dict["admin"]["total_cash"]

# value of "cash" parameter will be added to "total_cash". 
def add_or_remove_cash(given_dict, cash):
    given_dict["admin"]["total_cash"] += cash

# given a dict, this will return the value within "admin" dict at "pets_sold"
def get_pets_sold(given_dict):
    return given_dict["admin"]["pets_sold"]

# update "pets_sold" by value of "number_of_pets_sold" parameter
def increase_pets_sold(given_dict, number_of_pets_sold):
    given_dict["admin"]["pets_sold"] += number_of_pets_sold

# get number of items from the "pets" list, i.e. the total stock of the petshop.
def get_stock_count(given_dict):
    return len(given_dict["pets"])

# for each item in "pets" list, compare "breed" with "given_breed" parameter and if they are eqaul, add it to "pets_of_given_breed" list.
def get_pets_by_breed(given_dict, given_breed):
    # total_pets_by_breed = 0
    pets_of_given_breed = []
    for pet in given_dict["pets"]:
        if pet["breed"] == given_breed:
    #         total_pets_by_breed += 1
            pets_of_given_breed.append(pet)
    return pets_of_given_breed

# for each item in "pets" list, compare "name" with "given_name" and if equal, return the dict for that pet.
def find_pet_by_name(given_dict, given_name):
    # pets_of_given_name = []
    for pet in given_dict["pets"]:
        if pet["name"] == given_name:
            return pet
    #         pets_of_given_name.append(pet)
    # return pets_of_given_name

# for each item in "pets" list, compare "name" with "given_name" and if equal, remove the dict for that pet.
def remove_pet_by_name(given_dict, given_name):
    for pet in given_dict["pets"]:
        if pet["name"] == given_name:
            given_dict["pets"].remove(pet)

#  in "pets" list in "given_dict", add "new_pet_entry" to end of list.
def add_pet_to_stock(given_dict, new_pet_entry):
    given_dict["pets"].append(new_pet_entry)
    
