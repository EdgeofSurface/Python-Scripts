import os, random, string

length = 13
chars = string.ascii_letters + string.digits + '!@#$%^&*()-=+'
random.seed = (os.urandom(2000))

print ''.join(random.choice(chars) for i in range (length))
