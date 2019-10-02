# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 20:39:58 2019

@author: CTA
"""


from typing import List
from tranvia.marquesinas import obtener_marquesinas, marquesina

def main():
    my_marquesina = obtener_marquesinas("688")
    print(my_marquesina.title)
    print(my_marquesina.llegadas)
    
if __name__ == "__main__":
    print("Arrancamos ...")
    main()
    