import time

class Waiting:
    states = ('/', '-', '\\', '|')
    step = 0

    def __init__(self):
        self.next()

    def next(self):
        print('Work in progess ... {}'.format(Waiting.states[Waiting.step % 4]), end='\r')
        Waiting.step += 1

if __name__ == '__main__':
    progressbar = Waiting()
    for i in range(10):
        progressbar.next()
        time.sleep(1) # Do your own job !

    print()
