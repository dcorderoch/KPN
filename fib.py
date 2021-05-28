"""
this program simulates factorial through a KPN, see diagramaFibKPN.pdf
"""

from queue import Queue
from threading import Thread
from time import sleep

import sys

def add():
  a = 0
  b = 0
  c = 0
  while True:
    a = ck.get()
    b = fk.get()
    c = a + b
    ak.put(c)
  
def delay1():
  while True:
    a = ak.get()
    bk.put(a)

def delay0():
  while True:
    a = ek.get()
    fk.put(a)

def split():
  while True:
    a = bk.get()
    ck.put(a)
    ek.put(a)
    dk.put(a)

if __name__ == "__main__":
    ak = Queue()
    bk = Queue()
    ck = Queue()
    dk = Queue()
    ek = Queue()
    fk = Queue()
    
    bk.put(1)
    fk.put(0)
    
    Delay1 = Thread(target=delay1).start()
    Delay0 = Thread(target=delay0).start()
    
    Add = Thread(target=add).start()
    Split = Thread(target=split).start()

    while True:
        print(str(dk.get()))
        sleep(1)
