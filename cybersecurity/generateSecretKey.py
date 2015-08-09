#!/usr/bin/env python3

import string
import random
import os

length = 50

random.seed()

SECRET_KEY = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))

with open(os.path.expanduser("~/.djangoSecretKey"), "w") as f:
	f.write(SECRET_KEY)
