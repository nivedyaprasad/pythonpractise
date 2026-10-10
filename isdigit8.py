'''● Problem Statement: Given a string, check whether it consists entirely of
numeric digit characters (0-9). Return true if all characters are digits,
otherwise return false.
● Input: "12345" / "12a45" ● Output: true / false '''

s = input('Enter a string: ')

if s.isdigit():
    print(True)
else:
    print(False)
