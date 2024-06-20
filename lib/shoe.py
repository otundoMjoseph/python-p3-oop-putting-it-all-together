#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand):
        self.brand = brand

    

    def get_size(self):
        try:
            return self._size
        except:
            return
    
    def set_size(self, size):
        if type(size) == int:
            self._size = size
        else:
            print("size must be an integer")
    
    size = property(get_size, set_size)

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

# Shoe in shoe.py gets initialized with a brand.
# Shoe in shoe.py has the brand passed to __init__.
# Shoe in shoe.py can be assigned a color.
# Shoe in shoe.py can be assigned a size.
# Shoe in shoe.py prints "size must be an integer" if size is not an integer.
# Shoe in shoe.py can be assigned a material.
# Shoe in shoe.py can be assigned a condition.
# Shoe in shoe.py says that the shoe has been repaired.
# Shoe in shoe.py has "New" condition after repair.