import datetime
from A_in_B_mod_M import main_func as abm
from optparse import OptionParser


def main_func(k, n, t):
	return abm(k, n, 10 ** t)


if __name__ == '__main__':
    parser = OptionParser()
    (options, args) = parser.parse_args()
    if args:
        time = datetime.datetime.now()
        print 'result', main_func(*[int(a) for a in args])
        print 'time', datetime.datetime.now()-time
