#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 17:24:41 2021

@author: camilazumaeta
"""
import random 

def print_board(user_b):
    string=" "
    for i in range (number_pairs):
        string= string + "  " +str(i)
    print(string)
    
    counter=0
    for row in user_b:
        row_printed=str(counter)
        for element in row:
            row_printed= row_printed+"  "+str(element)
        print(row_printed)
        counter+=1
            
def change_board(row,column,user_b):
    change=board[row][column]
    user_b[row][column]=change
    print_board(user_b)
    return change
            

number_pairs=int(input("Ingrese nº de pares con los que queremos trabajar \n"))

#vamos a crear dos tableros uno que almacene todos los valores
# y e otro es el tablero que vera el usuario al que le iremos cambiando 
# los valores a medida que los descubra
#y otro con valores ocultos 
pair_list=[]
for i in range (number_pairs):
    pair_list.append(i)
    pair_list.append(i)

random.shuffle(pair_list)
middle_of_list=(number_pairs *2)//2
a= pair_list[0:middle_of_list]
b= pair_list[middle_of_list:]

board= [a,b]
user_board=[]
for i in range (2):
    list_temp=[]
    for m in range(number_pairs):
        list_temp.append("*")
    user_board.append(list_temp)

print_board(user_board)
change_board(0,1,user_board)

no_winner=True     
while no_winner:
    continuar=input("desea continuar?")
    if continuar =="no":
        no_winner=False

    
