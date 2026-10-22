input("Bit difference shows the bits that differ after XOR, press enter. ")
print("5^3: ", 5 ^ 3, "binary of 5 ^ 3: ", bin(5 ^ 3)[2:], "bits difer at: ", bin(5^3).count('1'))
print("9 ^ 5: ", 9 ^ 5, "binary of 9 ^ 5: ", bin(9 ^ 5)[2:], "bits difer at: ", bin(9 ^ 5).count('1'))

n = int(input("Enter a number like 4 or 6: "))
guess = input("guess the amount of bits that differ between " + str(n) + " and 7: ")
input("XOr will mark the differing bits and counts the 1s, press enter. ")
diff = bin(n ^ 7).count('1')
print("n is: ", n, "binary of n^7 = ", bin(n ^ 7)[2:], "Bits that differ: ", diff, "  your guess was: ", guess)