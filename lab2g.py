#!/usr/bin/env python3

# Author: Himay Shah

# Author ID: 118541234

# Date Created: 2025/05/23



import sys

timer = int(sys.argv[1]) if len(sys.argv) == 2 else 3



while timer > 0:

    print(timer)

    timer -= 1

print("blast off!")
