from itertools import permutations

def print_permutations():
    input_string = input("Enter a string: ")
    perms = permutations(input_string)

    for perm in perms:
        print(''.join(perm))

print_permutations()