#generate by user defined length

import string
import random
length = int(input("Enter the length of password :"))
passwords = []
randchoic = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
for i in range(length):
    randchoice = random.choice(randchoic)
    passwords.append(randchoice)
passwords = "".join(passwords)
print(passwords)