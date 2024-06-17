import cowsay
import sys
'''
if len(sys.argv) == 2:
    cowsay.cow("hello," + sys.argv[1])
    cowsay.trex("oi," + sys.argv[1])
'''

from sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])

