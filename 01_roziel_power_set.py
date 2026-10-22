input("Power set 2 - Power sets will increase the exponent by one. Press enter.")
print("3 elements, 2^3: ", 2**3)
print("Binary of mask 5: ", bin(5)[2:], "The 0 and 2 positions are on.")

n = int(input("Enter a number like 4 or 5: "))
guess = input("Guess how many subsets will be in " + str(n) + ": ")
input("Each element can be in or out of the set, Press enter. ")
print("n is: ", n , "n has: ", 2**n, " subsets,   your guess was, ", guess)