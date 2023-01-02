#Generate Password by pre-defined length of Password

import string
import random
length = 25
passwords = []
randchoic = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
for i in range(length):
    randchoice = random.choice(randchoic)
    passwords.append(randchoice)
passwords = "".join(passwords)
print(passwords)