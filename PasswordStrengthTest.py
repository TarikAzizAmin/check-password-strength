import string

password = input("Enter your password...\n")
complexityVector = 0

upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special_character = any([1 if c in string.punctuation else 0 for c in password])
digit = any([1 if c in string.digits else 0 for c in password])

characters = [upper_case, lower_case, special_character, digit]
print(characters)

length = len(password)
if length > 8:
    complexityVector += 1
if length > 12:
    complexityVector += 1
if length > 17:
    complexityVector += 1
if length > 20:
    complexityVector += 1

print(complexityVector)
print(f"password has length of {str(length)} adding points {str(complexityVector)}")

with open('1million.txt', 'r') as file:
    common_list = file.read().splitlines()

if password in common_list:
    score = 0
    print("This is a common password please create a different one")
    exit()

if sum(characters) > 1:
    complexityVector += 1
if sum(characters) > 2:
    complexityVector += 1
if sum(characters) > 3:
    complexityVector += 1

print(f"the string has a {str(sum(characters))} different characters types adding {str(sum(characters) - 1)} points")

if complexityVector < 4:
    print(f'weak, {str(complexityVector)}/7')
elif complexityVector == 4:
    print(f'decent str{complexityVector}/7')
elif 4 < complexityVector < 6:
    print(f'good {str(complexityVector)}/7')
elif complexityVector > 6:
    print(f"strong {str(complexityVector)}/7")
