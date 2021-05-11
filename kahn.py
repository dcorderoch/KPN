"""
an attempt to make Kahn Process networks
"""

from threading import Thread
from queue import Queue

import time  # to simulate blocking


class KahnThread(Thread):
    """
    class to simulate a node, it runs the node (lambda function) that is passed to it
    """

    def __init__(self, fn):
        """
        class initialization dunder method
        """
        super().__init__()
        self.fn = fn
        self.in_queues = []
        self.out_queues = []

    def __setitem__(self, index, q):
        """
        class set dunder method
        """
        self.out_queues[index] = q

    def __getitem__(self, index):
        """
        class get dunder method
        """
        return self.in_queues[index]

    def run(self):
        """
        Thread loop
        """
        while True:
            # get the inputs in the queue
            inputs = [q.get(True) for q in self.in_queues]

            # simulate blocking # TODO: check if necessary, Queue.get() should block
            # time.sleep(0.25)

            # generate output of function
            results = self.fn(*inputs)

            # put output in the output queue
            if isinstance(results, tuple):
                for result, q in zip(results, self.out_queues):
                    q.put(result)
            elif len(self.out_queues):
                self.out_queues[0].put(results)


def connect(*connections):
    """
    make the producer-consumer connection between two blocks
    """
    processes = {}
    for producer, consumer in connections:
        if not producer in processes:
            processes[producer] = KahnThread(producer)
        if not consumer in processes:
            processes[consumer] = KahnThread(consumer)

        q = Queue()
        processes[producer].out_queues.append(q)
        processes[consumer].in_queues.append(q)

    for process in processes.values():
        process.start()


def printer(filename):
    """
    generate a function that will print to stdouot, and append to filename
    """
    return lambda content: (
        print(content),
        open(filename, "a").write(str(content) + "\n"),
    )


# generate the initial value to pass to factorial
seed = int(input("Number: "))


def update_seed(x):
    seed = x


# run if this is the program called, but not if it's imported from another
if __name__ == "__main__":
    # "generate" seed
    b = lambda: seed
    # generate a function that calcultes the factorial
    fact_aux = lambda x: 1 if x == 0 else x * fact_aux(x - 1)
    # generate a function that returns an argument to itself
    fact = lambda x: x

    connect(
        (b, fact),
        (fact, fact_aux),
        (fact_aux, printer("test.txt")),
        (fact_aux, lambda x: update_seed(x)),
    )
