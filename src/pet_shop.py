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
    
# takes index position of a list as parameter and returns value from the "cash" key for that item.
def get_customer_cash(customer_index):
    return customer_index["cash"]

# takes 2 parameters, index position of a list and an int, then updates value at "cash" key for item at given index position. 
def remove_customer_cash(customer_index, cash):
    customer_index["cash"] -= cash

# takes index position and returns the length of the value in the "pets" key which should be a list.
def get_customer_pet_count(customer_index):
    return len(customer_index["pets"])

# takes 2 parameters, index position of a list and an object to add to a list. Appends the given object to the list at the "pets" key of the dictionary at the given index position which is a list.
def add_pet_to_customer(customer_index, pet_to_add):
    customer_index["pets"].append(pet_to_add)

# compares the value of "cash" at given index position parameter with "price" value of new_pet parameter. If customer "cash" is greater than or equal to new_pet "price" then evaluate to True, otherwise False.
def customer_can_afford_pet(customer_index, new_pet):
    can_afford_pet = False
    if customer_index["cash"] >= new_pet["price"]:
        can_afford_pet = True
    return can_afford_pet

# this will first check customer can afford the pet, if true then a series od functions runs to add the pet to dict in customers list, update total no. of pets sold in admin dict of petshop dict, subtract cash from dict in customers list and finally update the total cash in the admin dict. Only one pet can be sold at a time using this function as defined by pets_sold variable.
def sell_pet_to_customer(given_dict, pet, customer):
    pets_sold = 1
    if customer_can_afford_pet(customer, pet):
        add_pet_to_customer(customer, pet)
        remove_pet_by_name(given_dict, pet["name"])
        increase_pets_sold(given_dict, pets_sold)
        remove_customer_cash(customer, pet["price"])
        add_or_remove_cash(given_dict, pet["price"])

