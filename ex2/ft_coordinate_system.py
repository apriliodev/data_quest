import math


def valid_cords(cords_str):
    lst_size = 0
    cords = cords_str.split(",")
    for cord in cords:
        cord = cord.strip()
        lst_size += 1
    if (lst_size != 3):
        print("Invalid Syntax")
        return False


def get_player_pos():
    cords = input("Enter new coordinates as floats in format ’x,y,z’: ")
    while (valid_cords == False):
        print("Enter new coordinates as floats in format ’x,y,z’: ")
    