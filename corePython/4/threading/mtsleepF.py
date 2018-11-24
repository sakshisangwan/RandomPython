

from atexit import register
from random import randrange
from threading import Thread, Lock, current_thread
from time import sleep, ctime

class CleanOutputSet(set):
	def __str__(self):
		return ', '.join(x for x in self)

lock = Lock()
loops = (randrange(2,5) for x in range(randrange(3,7)))
remaining = CleanOutputSet()

def loop(nsec):
	myname = current_thread().name
	lock.acquire()
	remaining.add(myname)
	print('[{0}] Started {1}'.format(ctime(), myname))
	lock.release()
	sleep(nsec)
	lock.acquire()
	remaining.remove(myname)
	print('[{0}] Completed {1} ({2} secs)'.format(ctime(), myname, nsec))
	print('	(remaining: {0})'.format(remaining or 'NONE'))
	lock.release()

def main():
	for pause in loops:
		Thread(target=loop, args=(pause,)).start()

@register
def _atexit():
	print('all Done at:', ctime())

if __name__ == '__main__':
	main()