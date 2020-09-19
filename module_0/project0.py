#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 18:59:52 2020

@author: salnykov
"""

import numpy as np

#-----------------------------------------------------------------------------

#Function counting number of attepts to guess a number: Original version
def game_core_v1(number):
    count = 0
    while True:
        count+=1
        predict = np.random.randint(1,101) # guessing the number
        if number == predict: 
            return(count) # exit loop if number is guessed
        
#-----------------------------------------------------------------------------
            
#Function counting number of attepts to guess a number: Improved version
def game_core_v2(number):
    count = 0
    lb = 0 #Set initial prediction lower bound
    ub = 100 #Set initial prediction upper bound
    while True:
        count+=1
        predict = np.round(lb+ub) / 2 #predict average between ub and lb
        if number == predict: 
            return(count) # exit loop if guessed
        elif number > predict:
            lb = predict #if number above prediction,prediction becomes new lb
        else:
            ub = predict #if number below prediction,prediction becomes new ub
        
#-----------------------------------------------------------------------------
            
#Function tests performance of two game algorythms against random number set
#Function arguments are assumed to be a list consisting of 2 functions
def score_game(game_core):
    
    np.random.seed(101)  #fix RANDOMSEED to ensure replicability
    random_array = np.random.randint(1,101, size=(1000))
    alg_name=["Оригинальный","Улучшенный"] #Give algorythms "human" names
    
    #For each algorythm calculate mean number of attempts and print it
    for i, algorythm in enumerate(game_core):
        count_ls = []
        
        for number in random_array:
            count_ls.append(algorythm(number))
            
        print("{} алгоритм угадывает число в среднем за {} попыток"
             .format(alg_name[i], 
                     int(np.mean(count_ls))))
    
    return

#-----------------------------------------------------------------------------

# Run game with original and improved algorythm
score_game([game_core_v1, game_core_v2])