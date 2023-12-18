import string, random
letters_and_digits = string.ascii_letters + string.digits
random_string_and_digits=''.join(random.choice(letters_and_digits) for i in range(32))
print("Random String and Digits: ", random_string_and_digits)