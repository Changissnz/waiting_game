import time
import argparse

parser = argparse.ArgumentParser(description='Time is not your slave.')
parser.add_argument('seconds', metavar='s', type=int, nargs=1,\
    help='your time.')

def wait_secs(t):
    x = time.sleep(t)
    print("Happy?")
	
if __name__ == "__main__":
    args = parser.parse_args()
    wait_secs(args.seconds[0])

