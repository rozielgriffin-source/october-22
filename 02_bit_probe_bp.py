"""
1) Add the file and topic details.
   a) Mention the file name as `02-bit-probe.py`.
   b) Mention the topic as "Bit Probe - Checking the j-th Bit".
   c) Introduce the program as a way to check whether a specific bit is ON.

2) Explain bit probing.
   a) Pause the program before showing examples.
   b) Explain that `(n >> j) & 1` checks if bit `j` is ON.
   c) Use right shift to move the selected bit to the last position.
   d) Use `& 1` to read the bit value.

3) Show fixed examples.
   a) Print the binary form of 12.
   b) Check bit 2 and bit 1 of 12.
   c) Print the binary form of 7.
   d) Check bit 2 and bit 1 of 7.

4) Ask for a number.
   a) Ask the user to enter a number.
   b) Suggest example values like 9 or 6.
   c) Convert the input into an integer.

5) Show the number in binary.
   a) Use `bin(n)[2:]` to print the binary form.
   b) Help the user see the bit positions.

6) Ask for a prediction.
   a) Ask what bit 2 of the number is.
   b) Store the user's guess.

7) Check bit 2.
   a) Pause before showing the answer.
   b) Use `(n >> 2) & 1` to get bit 2.
   c) Print the bit value.
   d) Show the user's original guess.
"""