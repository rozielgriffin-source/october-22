"""
1) Add the file and topic details.
   a) Mention the file name as `01-power-set.py`.
   b) Mention the topic as "Power Set, Binary Mask as a Subset Selector".
   c) Introduce the program as a way to understand how subsets are counted.

2) Explain the power set idea.
   a) Pause the program before showing the examples.
   b) Explain that a set with `n` elements has `2^n` subsets.
   c) Show that 3 elements create 8 subsets.

3) Explain binary masks.
   a) Show mask 5 in binary form.
   b) Explain that binary mask positions can select elements.
   c) Show that mask 5 selects positions 0 and 2.

4) Ask for the number of elements.
   a) Ask the user to enter the number of elements.
   b) Suggest example values like 4 or 5.
   c) Convert the input into an integer.

5) Ask for a prediction.
   a) Ask how many subsets the set will have.
   b) Store the user's guess.

6) Calculate the number of subsets.
   a) Pause before showing the answer.
   b) Use `2**n` to calculate the number of subsets.
   c) Explain that each element has two choices: in or out.

7) Display the final result.
   a) Print the number of elements.
   b) Print the total subsets.
   c) Show the user's original guess.
"""