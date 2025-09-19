#!/usr/bin/env python3
# Author: Himay Shah
# Author ID: 118541234
# Date Created: 2025/09/19

import sys

if len(sys.argv) == 2:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer != 0:
    print(timer)
    timer = timer - 1
print('blast off!')
