#!/usr/bin/env python

import sys
import argparse

parser=argparse.ArgumentParser(
    description="Decrypt strings encrypted with iETSolutions Enterprise Password Encryption.",
    epilog="Never roll your own encryption!")
parser.add_argument('string', type=str, help='Encrypted password string!')
args=parser.parse_args()

encPos = [191, 45, 67, 110, 189, 172, 62, 90, 131, 162, 111, 57, 74, 181, 139, 129, 31, 77, 166, 143, 124, 58, 99, 147, 125]


encryptedText = sys.argv[1]
print sys.argv[1]

index1 = ord( encryptedText[0] ) - 97 + 1


num = ord( encryptedText[index1] ) - 97
if num > 25:
    num = 25
if num < 25:
    raise ValueError('Wrong cipher')
for i in xrange(num):
   ch = chr( (encryptedText[encPos[i]] & 240) + (encryptedText[encPos[i] + 1] & 15) )
print ch
