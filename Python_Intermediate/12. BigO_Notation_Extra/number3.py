def print_all_pairs(my_dict):
    # O(n)
    for key1 in my_dict:
        # O(n^2)
        for key2 in my_dict:
            print(f"{key1}-{key2}")


# ¿Cuál es la complejidad temporal?
# O(n^2) 

# ¿Cuanto dura si hay 1 millón de claves?
# Like 1 trillion operations, basically hours or days to complete
# print() in python is really slow, that is the complicate part