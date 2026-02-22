from utils import *

def main():
    """
    The main function of the program. Outputting the result.
    """
    print("\nThis program creates symbols array and calculates number of elements.\n")

    print(f'The first array: {first_arr()}\n')

    print(f'The second array: {second_arr()}\n')

    print(f'The third array, where elements are less than 67: {third_arr()}\n')

    print(f'Characters translated from ASCII code: {ascii_to_symbol()}')

if __name__ == '__main__':
    main()