#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 17:24:41 2021

@author: camilazumaeta
"""
import random 
# function that prints the board for the user
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
  
# function that changes the values that the user can see when picking a card         
def change_board(row,column,user_b):
    change=board[row][column]
    user_b[row][column]=change
    print_board(user_b)
    return change

# function that asks for the coordinates of the cards to turn over and 
#evaluates whether it is a oair or not          
def play():
    print_board(user_board)
    coordenates1= input("Enter your coordenates row,column separeted by ',' \n")
    coordenates1=coordenates1.split(",")
    value1=change_board(int(coordenates1[0]),int(coordenates1[1]),user_board)
    coordenates2= input("Enter your coordenates row,column separeted by ',' \n")
    coordenates2=coordenates2.split(",")
    value2=change_board(int(coordenates2[0]),int(coordenates2[1]),user_board)
    
    if value1==value2:
        print("You have found a pair!\n")
        return "pair"
    else: 
        print("You failed \n")
        user_board[int(coordenates1[0])][int(coordenates1[1])]="*"
        user_board[int(coordenates2[0])][int(coordenates2[1])]="*"
        return "fail"

# We ask the user for a number of pairs to play with     
number_pairs=int(input("Enter number of pairs to play with \n"))

# we create a board that holds all the values (shuffled)
# and another board that the user can see while turning cards over
pair_list=[]
for i in range (number_pairs):
    pair_list.append(i+1)
    pair_list.append(i+1)

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


#in the following menu we let the players take turns
# while keeping track of who picked a pair so they can play again
#the cicle ends when all the pairs have been found
player1=0
player2=0
   
while player1+player2 !=number_pairs:
    #player 1 turn 
    print("Player 1 plays \n")
    result=play()
    while result!= "fail":
        player1+=1
        if player1+player2==number_pairs:
            break
        print("Player 1 plays again")
        result=play()
    if player1 +player2==number_pairs:
        break
    
    #player 2 turn
    print("Player 2 plays \n")
    result=play()
    while result!= "fail":
        player2+=1
        if player1+player2==number_pairs:
            break
        print("Player 2 plays again")
        result=play()
        
  
    
# We annouce the winner of the match 
if player1>player2:
    print("Player 1 you won!!")
elif player2>player1:
    print("Player 2 you won!!")
else:
    print("It's a Tie!!")

