#!/usr/bin/env python3

# Created by: Ntare Katarebe
# Created on: May 2021
# This program prints the volume of a cylinder
#   user inputs number

import math


def calculate_surface_area(side):
    # This function prints the volume of a cylinder

    # process
    surface_area = 6 * side ** 2

    return surface_area


def main():
    # this function just calls other functions

    side_from_user = input("Enter the side of a cube: ")

    try:
        side_integer = float(side_from_user)
        surface_area_of_cube = calculate_surface_area(side_integer)
        print("The surface area of cube is {}".format(surface_area_of_cube))
    except Exception:
        print("{} is invalid, but please try again".format(side_from_user))


if __name__ == "__main__":
    main()
