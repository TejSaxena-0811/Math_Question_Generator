# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 21:01:13 2023

@author: jaigurudev
"""

import random
import math
import time
    

input("""Press enter to start :)
************************""")

x = input("Basic Maths (b) or Advanced Math (a)?: ")

correct = 0

def basic():
    start_time = time.time()
    
    total_questions = int(input("How many questions do you want?: "))
    
    operators = ["+" , "-" , "*"]
    mini = 3
    maxi = 15
    
    for i in range(1 , total_questions + 1):
        a = random.randint(mini,maxi)
        b = random.randint(mini,maxi)
        choices = random.choice(operators)
        
        final = str(a) + str(choices) + str(b)
        print("Question" , i , ":" , final)
        guess = int(input("Enter answer: "))
        answer = eval(final)
        
        if guess == answer:
            print("Correct!")
            global correct
            correct += 1
        else:
            print("Incorrect")
            
    end_time = time.time()

    total_time = round(end_time - start_time , 2)
    your_score = correct / total_questions

    print("Your score: " , correct , "/" , total_questions)
    print("You took" , total_time , "seconds")
    
    if your_score == 1:
        print("You did amazing!")
    elif your_score == 0.9:
        print("you did great!")
    elif your_score == 0.8:
        print("You did good!")
    elif your_score == 0.7:
        print("You did decent.")
    elif your_score == 0.6:
        print("You need a little more practice.")
    elif your_score == 0.5:
        print("You need practice.")
    elif your_score < 0.5:
        print("You should take this test once more.")
    

def advanced():
    start_time2 = time.time()
    
    mini2 = 3
    maxi2 = 15
    trigo = [0.55 , -0.55 , 0 , 1 , -1]
    squaring = [4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100 , 121 , 144 , 169 , 196 , 225]
    
    total_questions2 = int(input("How many questions do you want?: "))
    
    correct2 = 0
    
    for o in range(1 , total_questions2 + 1):
        
        m = random.randint(mini2 , maxi2)
        n = random.randint(mini2 , maxi2)
        h = random.choice(trigo)
        q = random.choice(squaring)
        
        opt = ["%" , "fact" , "sqrt" , "sin" , "cos" , "tan"]
        
        r = random.choice(opt)
        
        if r == "%":
            real = "Remainder of" , m , "/" , n , "is: "
            print("Question" , o , ":" , real)
            answer2 = m%n
            guess2 = int(input("Enter answer: "))
            if answer2 == guess2:
                print("Correct!")
                correct2 += 1
            else:
                print("Incorrect")
                
        elif r == "fact":
            realing = "Factorial of" , m , "is: "
            print("Question" , o , ":" , realing)
            answer3 = math.factorial(m)
            guess3 = int(input("Enter answer: "))
            if answer3 == guess3:
                print("Correct!")
                correct2 += 1
            else:
                print("Incorrect")
        
        elif r == "sin":
            realest = "Sine of" , h , "is: "
            print("Question" , o , ":" , realest)
            answer4 = math.asin(h)
            guess4 = float(input("Enter answer: "))
            if answer4 == guess4:
                print("Correct!")
                correct2 += 1
            else:
                print("Incorrect")
                
        elif r == "cos":
            rizz = "Cosine of" , h , "is: "
            print("Question" , o , ":" , rizz)
            answer5 = math.acos(h)
            guess5 = float(input("Enter answer: "))
            if answer5 == guess5:
                print("Correct!")
                correct2 += 1
            else:
                print("Incorrect")
                
        elif r == "tan":
            rizzler = "Tangent of" , h , "is: "
            print("Question" , o , ":" , rizzler)
            answer6 = math.atan(h)
            guess6 = float(input("Enter answer: "))
            if answer6 == guess6:
                print("Correct!")
                correct2 += 1
            else:
                print("Incorrect")
                
        elif r == "sqrt":
            rizzlering = "Square root of" , q , "is: "
            print("Question" , o , ":" , rizzlering)
            answer7 = math.sqrt(q)
            guess7 = int(input("Enter answer: "))
            if answer7 == guess7:
                print("Correct!")
                correct2 += 1
            else:
                print("Incorrect")
            
            
    end_time2 = time.time()

    total_time2 = round(end_time2 - start_time2 , 2)
    your_score2 = correct2 / total_questions2

    print("Your score: " , correct2 , "/" , total_questions2)
    print("You took" , total_time2 , "seconds")
    
    if your_score2 == 1:
        print("You did amazing!")
    elif your_score2 == 0.9:
        print("you did great!")
    elif your_score2 == 0.8:
        print("You did good!")
    elif your_score2 == 0.7:
        print("You did decent.")
    elif your_score2 == 0.6:
        print("You need a little more practice.")
    elif your_score2 == 0.5:
        print("You need practice.")
    elif your_score2 < 0.5:
        print("You should take this test once more.")


if x.lower() == "b":
    basic()
elif x.lower() == "a":
    advanced()
            







    
    
    

































