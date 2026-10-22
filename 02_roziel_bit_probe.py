input("Bit probe is used to check if bit j is on. Press enter. ")
print("binary of 12: ", bin(12)[2:], "bit 2 of 12: ", (12>>2) & 1, "bit 1 of 12: ", (12>>1) & 1)
print("binary of 7: ", bin(7)[2:], "bit 2 of 7: ", (7>>2) & 1, "bit 1 of 7: ", (7>>1) & 1)

n = int(input("Enter a number like 9 or 6: "))
guess = input("Guess if position 2 of " + str(n) + " is on or off: ")
input("n>>2 & 1 will check position 2 of n in binary, press enter. ")
print("n is: ", n, "bit 2 of n is: ", n>>2 & 1, "  your guess was: ", guess)