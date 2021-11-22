# import tkinter
# print(tkinter.TkVersion)
# print(tkinter.TclVersion)
#
# mainWindow = tkinter.Tk()
#
#

# from turtle import *
# import turtle
# import time

# turtle.forward(250)
# turtle.left(90)
# turtle.forward(250)
# turtle.left(90)
# turtle.forward(250)
# turtle.left(90)
# turtle.forward(250)

# turtle.forward(400)
# turtle.left(135)
# turtle.forward(283)
# turtle.left(90)
# turtle.forward(283)
# turtle.left(135)
# turtle.forward(250)
# turtle.right(250)
# turtle.forward(150)
# turtle.forward(250)
# turtle.right(250)
# turtle.forward(150)
# turtle.forward(250)
# turtle.right(250)
# turtle.forward(150)
# turtle.forward(250)
# turtle.right(250)
# turtle.forward(150)
# turtle.forward(250)
# turtle.right(250)
# turtle.forward(150)
# turtle.forward(250)
# turtle.right(250)
# turtle.forward(250)
# turtle.forward(250)
# turtle.right(250)
# turtle.forward(150)
# turtle.forward(250)
# turtle.right(250)
# turtle.forward(150)
# turtle.forward(250)
# turtle.right(250)
# turtle.forward(150)
# turtle.forward(250)
# turtle.right(250)
# turtle.forward(150)
# turtle.forward(250)
# turtle.right(250)
# turtle.forward(150)
# turtle.forward(250)
# turtle.right(250)
# turtle.forward(250)
#
# time.sleep(20)

# print("j")

# print("enter the number: ")
# def mul(x : string, y : string)  -> bool:
#     result = x * y
#     return result
#
# k = mul(str(input()), str(input()))
# print(k)
# def fibonacci(n):
#     if 0 <= n <= 1:
#         return n
#
#     nminus1, nminus2 = 1, 0
#
#     result = None
#     for f in range(n - 1):
#         result = nminus2 + nminus1
#         nminus2 = nminus1
#         nminus1 = result
#
#     return result
#
#
# for i in range(36):
#     print(i, fibonacci(i))

# print(" *********\n",
#       "**     **\n",
#       "*   A   *\n",
#       "**     **\n",
#       "*********\n"
#       )
# print("-" * 80)
# def text_A(text):
#       screen_width = 9
#       if len(text) > screen_width - 4:
#             print("eek")
#
#       if text == "*"
#             print("*" * screen_width)
#


# banner.py
# def banner_text(text):
#     screen_width = 80
#     if len(text) > screen_width - 4:
#         print("EEK!!")
#         print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH")
#
#     if text == "*":
#         print("*" * screen_width)
#     else:
#         centred_text = text.center(screen_width - 4)
#         output_string = "**{0}**".format(centred_text)
#         print(output_string)
#         return
#
#
# banner_text("*")
# banner_text("Always look on the bright side of life...")
# banner_text("If life seems jolly rotten,")
# banner_text("There's something you've forgotten!")
# banner_text("And that's to laugh and smile and dance and sing,")
# banner_text(" ")
# banner_text("When you're feeling in the dumps,")
# banner_text("Don't be silly chumps,")
# banner_text("Just purse your lips and whistle - that's the thing!")
# banner_text("And... always look on the bright side of life...")
# banner_text("*")
#
# result = banner_text("Nothing is returned")
# print(result)
#
# numbers = [4, 2, 7, 5, 8, 3, 9, 6, 1]
# print(numbers.sort())


#      def get_integer(prompt):
#     while True:
#         temp = input(prompt)
#         if temp.isnumeric():
#             return int(temp)
#
#
# number = int(input("enter number: "))
# temperature = get_integer(number)
# print(temperature)
# a = input(ajay)
# print(a)

# def palindrome(string):
#     return string[::-1] == string
#
#
# word = input("enter the word: ").casefold()
# if palindrome(word):
#     print("yes")
# else:
#     print("no")

# def mul(x, y):
#     result = x * y
#     return result
#
#
# ajay = mul(2, 3)
# print(ajay)

# def palindrome(string):
#     return string[::-1] == string
#
#
# def palindrome_sentence(sentence):
#     string = ""
#     for char in sentence:
#         if char.isalnum():
#             string += char
#             print(string)
#
#     return string[::-1] == string
#
#
# word = input("enter a word: ").casefold()
# if palindrome(word):
#     print("yes, its a palindrome")
# else:
#     print("no, its not a palindrome")
# def mul(x, y):
#     result = x * y
#     return result
#
#
# answer = mul(23, 45)
# print(answer)
# print()
#
# for val in range(1, 10):
#     crux = mul(2, val)
#     print(crux)
#
# print(answer)

# def ajay():
#     kumar_s = "he is a " + "nice  guy"
#     return kumar_s
#
#
# name = ajay()
# print(name)

# print("hello")
# data = [3,4,4,4,4,4,57,7,6,7,7,68,7,34,24234,346,57,6,8,78,79,8,7,9876]
# # del data[0:2]
# # print(data)
# # del data[16:]
# # print(data)
# min_valid = 100
# max_valid = 500
# stop = 0
# for index, value in enumerate(data):
#     if (value >= min_valid):
#         stop = index
#         break
# print(stop)
# del data[:stop]
# print(data)
# start = 0
# for index in range(len(data) - 1, -1, -1):
#       if data[index] <= max_valid:
#         start = index + 1
#         break
#
# print(start)
# del data[start:]
# print(data)
# print(index)
# data = [3,4,4,4,4,4,57,7,6,7,7,68,7,34,24234,346,57,6,8,78,79,8,7,9876]
# del data[0:2]
# print(data)
# del data[16:]
# print(data)

# min_valid = 100
# max_valid = 500
# for index, value in enumerate(data):
#     if ((value < min_valid) or (value > max_valid)):
#         del data[index]
#         index -= 1
#
# print(data)
# computer_parts = ["computer",
#                   "monitor",
#                   "mouse",
#                   "keyboard",
#                   "mouse mat"
#                   ]
# print(computer_parts)
# computer_parts[4] = "usb cable"
# print(computer_parts)
# computer_parts[4] = "usb cable"
# print(computer_parts)
# computer_parts[4:] = ["usb cable"]
# print(computer_parts)
# computer_parts[4:] = "usb cable"
# print(computer_parts)
# empty_list = []
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
# numbers = even + odd
# print(numbers)
# numbers.sort()
# print(numbers)
# digits = sorted("3827r8379490")
# print(digits)
# aha = list("3827r8379490")
# print(aha)
# # sorted digits is not equal to list aha
# digits = list(aha)
# print(digits)
# print(digits is aha)
# print(digits == aha)
# kya = aha.copy()
# print(kya)

# pangram = "The quick brown fox jump over the lazy dog "
#
# letters = sorted(pangram .casefold())
# print(letters)
# name = [5, 5554, 5, 43, 34, 33]  # for letters use sorted , and for numbers use variable.sort()
# name.sort()
# pangram.sort()
# print(name)
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# even.extend(odd)
# print(even)
#
# even.sort(reverse=True)
# print(even)
# computer_parts = "_"
# chose = 0
# while chose == 0:
#     print("computer parts are: ")
#     print("mouse\n", "keyboard\n", "hdmi cable\n", "mouse mat\n", "usb cable\n")
#     if chose ==
#     chose += 1

# first_5_numb = [1, 2, 3, 4, 5]
# second_5_numb = [6, 7, 8, 9, 10]
# print(len(first_5_numb))
# print(first_5_numb[3])
# print(first_5_numb)

# words = "iasiisisiasiiasiasiiasiaisiis"
# print("words".count("s"))
# print("iasiisisiasiiasiasiiasiaisiis".count("ias"))

# face =["eyes", "nose", "lips", "forehead", "ears", "mouth"]
#
# for parts in face:
#     print("body part: {}".format(parts))
# print(face[1])

# print("h")

# import random
# guess = 0
# n = 10
# guessed = (n * random.random() + 1)
# if guess != guessed:
#     int(input())
#     for guess in guessed:
#         print("no")
# else:
#     print("you guessed it: ")

# colour = ["red", "blue", "green", "yellow", "pink"]
# favorite = int(input("enter colour: "))
# for favorite in colour:
#     print("s its my favorite colour {}".format(favorite))

# i = 1
# while i < 10:
#     name = str(input("enter u r name: "))
#     print("{0} {1}".format(i, name))
#     i += 1

# shopping_list = ["milk", "egg", "spam"]
# item_to_find = "spam"
# found = None
#
# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found = index
# print("item fount at position {}".format(found))
# for i in range(1, 10):
#     for j in range(1, 10):
#         print("{0} multiplication {1} is {2}".format(i, j, i*j))
#     print("*" * 50)
#
# for chances in range(1, 4):
#     pin = int(input("enter u r ATM pin: "))
#     if pin != 1234:
#         print("no")
#     else:
#         print("s")
#         print("u can proceed with forther steps: ")
#         break
#
# print("welcome")
# for chances in range(1,4):
#     pin = int(input("enter u r pin: "))
#     if pin != 1234:
#         print("u entered wrongly")
# else:
#     print("you entered u r pin correctly")

# print("welcome to Ajay ATM")
#
# for chances in range(1,3):
#     print(" enter u r pin : ")
#     if chances
#             pin != 1234:
#         print("you enetred wrongly")
#         chances = chances + 1
#         break
# else:
#     print("you entered pin correctly")

# num = int(input("enter a number "))
# factorial = 1
# # # if num < 0:
# # #     print("the number should be +ve")
# # # elif num == 0:
# # #     print("1")
# # # else:
# # #     for i in range(2, num + 1):
# # #         factorial = factorial * i
# # #         print("factorial ", factorial)
# # # # number = int(input("enter number: "))
# # # n = 5
# # # factorial = n*(n-1)*(n-2)
# # # for factorial in 5:
# # #     print("factorial = ", factorial)
# # # print("thats it.......!")
# # # name = "AJAY KUMAR S"
# # #
# # # for letter in name:
# # #     print("letter is: ", letter)
# # # print("that's it.....!")
# # #
# #
# # # import random
# # # n = 10
# # # guess = 0
# # # number_to_be_guessed = int(n * random.random() + 1)
# # #
# # # while guess != number_to_be_guessed:
# # #     guess = int(input("enter the number: "))
# # #     if guess > 0:
# # #         if guess < number_to_be_guessed:
# # #             print("too low")
# # #         elif guess > number_to_be_guessed:
# # #             print("too higher")
# # #
# # #     else:
# # #         print("sorry wrong...!")
# # #         break
# # # else:
# # #     print("congragulations you guessed it.....")
# # # answer = ""
# # # guess = int(input("enter the number: "))
# # # while guess == answer:
# # #     if guess < answer:
# # #         print("the number is too small")
# # #     elif guess > answer:
# # #         print("the number is too high")
# # #         guess = int(input("enter the number: "))
# # # else:
# # #     print("you guessed it")
# # # count = 0
# # #
# # # while count < 5:
# # #     print("number ", count)
# # #     count = count + 1
# # # print("good bye.....!")
# #
# # # letter = A
# # #
# # # while letter < AAAA:
# # #     assert isinstance(letter, object)
# # #     print("letter", letter)
# # #     letter = letter * A
# # # print("yes i'm did it")
# #
# # # my_name = "A1JAY 5KU7MAR7 S9"
# # # name = ""
# # # while char in my_name:
# # #     print("number", name)
# # #     name = name + my_name
# # # print("thats it")
# # #
# #
# # # number = "9,23:46}"
# # # seperator = ""
# # # for ajay in number:
# # #     if not ajay.isnumeric():
# # #         seperator = seperator + ajay
# # #
# # # print(seperator)
# numb = 123456789
# for number in numb:
#     print(number + " " + (number * number))
# print("*"*30)
# # # #
# A = B = 2
# print(A ** B)
# name = "AJAY KUMAR S"
# for character in name:
#     print(character)

# name = "AJAY KUMAR S"
# print("type a letter: ")
# letter = str(input())
# if letter in name.casefold():
#     print("yes it's there")
# else:
#     print("it's not there")

# answer = 5
# print("guess the number: ")
# guess = int(input())
# if guess > answer:
#     print("guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("u guessed it")
#     else:
#         print("try next time")
# elif guess < answer:
#     print("guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("u guessed it")
#     else:
#         print("try next time")
# else:
#     print("u guessed it")
#
# name = input("please enter u r name: ")
# age = int(input("how old are you, {0}?".format(name)))
# print(age)
# if age > 18:
#     print("u r ready to vote")
# elif age == 18:
#     print("apply for voter card")
# else:
# print("come after {}".format(18 - age))