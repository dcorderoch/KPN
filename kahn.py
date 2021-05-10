"""
an attempt to make Kahn Process networks
"""

from threading import Thread
from queue import Queue

class KPNThread(Thread):
    def __init__(self, *, fn, name, i_q, o_q):
        super().__init__()
        self.fn = fn
        self.name = name
        self.i_queues = i_q
        self.o_queues = o_q

    def run(self):
        while True:
            # tuple of tuples
            inputs = [q.get(True) for q in self.i_queues]
            _next, _sum, able = self.fn(inputs[0])
            if able:
                for q in self.o_queues:
                    q.put((_next, _sum, able))
            else:
                print(f'result of {self.name}: {_sum}')
                return

if __name__ == '__main__':
    fac = lambda t: (t[0] - 1, t[0] * t[1], t[0] > 1)

    seed_no = int(input('initial number: '))

    print("")

    a_q = Queue()
    # (seed number, multiplicative identity for factorial, still going)
    # once "still going" is false, calculation is done, and thread will stop
    seed = (seed_no, 1, True)
    a_q.put(seed)

    factorializer = KPNThread(fn=fac, name="factorial", i_q=(a_q,), o_q=(a_q,))

    factorializer.start()
