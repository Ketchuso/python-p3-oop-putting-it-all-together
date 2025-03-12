#!/usr/bin/env python3

class Shoe:
    def __init__(shoe, brand, size):
        shoe.brand = brand
        shoe.size = size
    
    @property
    def size(shoe):
        return shoe._size
    
    @size.setter
    def size(shoe, value):
        if not isinstance(value, int):
            print("size must be an integer")
        shoe._size = value
    
    def cobble(shoe):
        shoe.condition = "New"
        print("Your shoe is as good as new!")