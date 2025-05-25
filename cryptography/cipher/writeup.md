# Details
- Title: Cipher
- Category: Cryptography
- Date Solved: September 19, 2024
- Author: Jaden Lee
- Time Required: 30 min

# Problem
The problem was to decode a series of strings given in the 'problem.txt' file. 

# Solution
As the easiest cryptography problem, I figured it would be a Caesar Cipher, so I wrote a Python script to apply all 26 shifts to each of the strings and print the results to the console. From there, it was clear that the strings were decoded when you use a shift of 20.

As an update, I have rewritten my script to parse the strings from the file, apply frequency analysis, and use a chi-squared test to determine the precise shift used. The decoded text is then outputted to the file titled 'output.txt'.

# Recommended Measures
Don't use an ancient cryptography scheme...