name=input("What is your name:")
print("Hello",name)

Stop=False
while(Stop is False ):
  try:
    val1 = int(input("Please enter an integer: "))
    val2 = int(input("Please enter another integer: "))
    Stop=True
  except ValueError: 
      print("You did not enter a valid integer, please try again.")


