"""This is a little script i made to randomly generate numbers. I am studding python with
problems and solutions at w3resource.com... rather than select a problem to solve, i created this script
that will give me random problems to solve"""


import random
num_1 = 1
num_2 = 100

Guess = input("\nType 'Guess' To Pick A Problem:")

while Guess == "guess":
  solution = random.randint(num_1,num_2)
  print(solution),
  input("\nDo you want another random number Aric?(Y/N)")
  if Guess == "y":
    solution_2 = random.randint(num_1,num_2)
    print(solution_2)
