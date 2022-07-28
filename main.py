import random


class Cub:
    cube_facet = 6
    def throw (self):
        num = random.randint(1, 6)
        return num

cub_1 = Cub()
cub_2 = Cub()

def throw_cubs (one, two):
    one_cub = random.randint(1, 6)
    two_cub = random.randint(1, 6)
    return one_cub, two_cub

print(throw_cubs(cub_1, cub_2))




