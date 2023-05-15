print("Multiplication Game")
print()
Your_multiple = int(input("Input your desired multiples: "))
print()

counter = 0
for i in range (11):
  answer =  i * Your_multiple 
  print("Give me the value of", i , "x", Your_multiple)
  Your_answer = int(input("What is the answer? "))
  if answer == Your_answer:
    print("You are correct!")
    counter += 1
  else:
    print("You are wrong, make the calculation again")

if counter == 10:
  print("YOu got everything right. You deserve a candy")
else:
  print("Your score is,", counter, "out of 10")
  