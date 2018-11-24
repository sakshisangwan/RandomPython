

from atexit import register
from random import randrange
from threading import BoundedSemaphore, Lock, Thread
from time import sleep, ctime

lock = Lock()
MAX = 5
candytray = BoundedSemaphore(MAX)

def refill():
	lock.acquire()
	print('Refilling Candy...')
	try:
		candytray.release()
	except ValueError:
		print('Full, skipping')
	else:
		print('OK')
	lock.release()

def buy():
	lock.acquire()
	print('Buying Candy...')
	if candytray.acquire(False):
		print('OK')
	else:
		print('Empty, skipping')
	lock.release()

def producer(loops):
	for i in range(loops):
		refill()
		sleep(randrange(3))

def consumer(loops):
	for i in range(loops):
		buy()
		sleep(randrange(3))

def main():
	print('Starting at:', ctime())
	nloops = randrange(2, 6)
	print('The Candy Machine(full with {0} bars)!'.format(MAX))
	Thread(target=consumer, args=(randrange(nloops, nloops+MAX+2),)).start()
	Thread(target=producer, args=(nloops,)).start()

@register
def _atexit():
	print('all DONE at:', ctime())

if __name__ == '__main__':
	main()