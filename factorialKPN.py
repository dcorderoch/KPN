from queue import Queue
from threading import Thread
from time import sleep

# Señales


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


# SEPARACIONES-*---

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


if __name__ == "__main__":
    an = Queue()
    bn = Queue()
    cn = Queue()
    dn = Queue()
    en = Queue()
    fn = Queue()
    gn = Queue()
    hn = Queue()

    Delay1 = Thread(target=delay1).start()
    Delay2 = Thread(target=delay2).start()
    Split1 = Thread(target=split1).start()
    Split2 = Thread(target=split2).start()

    Add = Thread(target=add).start()
    Mul = Thread(target=mul).start()

    while True:
        print(str(en.get()))
        sleep(0.1)
