# -*- coding: utf-8 -*-
"""Definindo Tempo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e0yvoIRUb87LuLkvBLy6FEQpMQBKNF06
"""

import threading

def fim():
  print('Acabou o tempo')

timer = threading.Timer(5.0, fim)

timer.start()