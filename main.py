'''
 created on: 19-dec-2018
 @author : Abhijeet Saraf
'''

import sys
import os

inp = sys.stdin
out = sys.stdout

def main():
    local = os.getenv('KANGOONIE', 0)
    if local:
        global inp, out
        inp = sys.stdin = open('in.txt', 'r')
        out = sys.stdout = open('out.txt', 'w')

    run()

    if local:
        inp.close()
        out.flush()
        out.close()

def run():
    #TODO put your code here
    print('Hello world')

main()
sys.exit(0)