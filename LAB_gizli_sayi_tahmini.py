secret_number = 777
print(
"""

+================================+
| Welcome to my game, Muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So what is the secret number?  |
+================================+
"""
)

number = int(input("Enter a number: "))
if number == secret_number:
    print("Well done, Muggle! You are free now!")
while number != secret_number:
    print("ha ha! Yo're stuck in a loop!")
    number = int(input("Enter a number: "))
