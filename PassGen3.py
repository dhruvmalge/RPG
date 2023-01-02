#Password generating by its length and number of samples

import string
import random as random
length = int(input("Choose Password Length :"))
samples = int(input("Choose Number of samples : "))
passwords = []
randchoic = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
for i in range(length):
    randchoice = random.choice(randchoic)
    appended = passwords.append(randchoice)
for x in range(samples):
    passwords = random.choices(randchoic, k=length)
    passwords = "".join(passwords)
    #passwords = passwords.splitlines()
    print(passwords)