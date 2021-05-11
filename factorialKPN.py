"""
this program simulates factorial through a KPN, see diagramaKPN.pdf

md5sum                            filename
f49200b962b289bb4c93f443f130d552  diagramaKPN.pdf

though instead of a "normal" factorial, which stops at 1, a
"""

from queue import Queue
from threading import Thread
from time import sleep

# Señales
an = Queue()
bn = Queue()
cn = Queue()
dn = Queue()
en = Queue()
fn = Queue()
gn = Queue()
hn = Queue()


# DELAYS
def delay1():
    cn.put(1)
    while True:
        a = cn.get()
        dn.put(a)


def delay2():
    fn.put(1)
    while True:
        a = fn.get()
        gn.put(a)


# SEPARACIONES-*---
def split1():
    while True:
        a = dn.get()
        en.put(a)
        bn.put(a)


def split2():
    while True:
        a = hn.get()
        an.put(a)
        fn.put(a)

# SUMA
def add():
    a = 0
    c = 0
    while True:
        a = gn.get()
        c = a + 1
        hn.put(c)


# multiplicacion
def mul():
    a = 0
    b = 0
    c = 0

    while True:
        a = an.get()
        b = bn.get()
        c = a * b
        cn.put(c)


# allow this file to be imported as a module from another file
if __name__ == "__main__":

    Delay1 = Thread(target=delay1).start()
    Delay2 = Thread(target=delay2).start()
    Split1 = Thread(target=split1).start()
    Split2 = Thread(target=split2).start()

    Add = Thread(target=add).start()
    Mul = Thread(target=mul).start()

    while True:
        print(str(en.get()))
        sleep(1)
