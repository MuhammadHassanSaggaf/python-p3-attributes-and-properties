#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    #any scope outside of any method is an attribute
    # getattr() retrieves the value of an attribute.
    # setattr() changes the value of an attribute, just as you would with dot notation.
    # hasattr() checks for the presence of an attribute.
    # delattr() removes an attribute from a class or object.
    # NOTE: getattr() also allows us to provide an optional third argument as a default value if the attribute does not exist.
    # Python's attr() functions comes in their ability to create, retrieve, update, and delete attributes for which the names are unknown.
    # Properties in Python are attributes that are controlled by methods.
    # name must be of type `str` and between 1 and 25 characters
    def __init__(self, name="Aubrey", breed="Mastiff"):
        self.set_name(name)
        self.set_breed(breed)

    def get_name(self):
        return self.name

    def get_breed(self):
        return self.breed
    
    def set_name(self, name):
        if (type(name) is str and 1 <= len(name) <= 25):
            self.name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self.breed = breed
        else:
            print("Breed must be in list of approved breeds.")