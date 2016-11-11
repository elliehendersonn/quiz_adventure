# Our quiz!

name = ""

def quiz():
     global score
     global name

     # Question1()
     # Question2()
     # Question3()
     # Question4()
     # Question5()
     # Question6()
     # Question7()
     # Question8()
     # Question9()
     # Question10()
     
   

  
     score = 0
     name = input("Enter your name here: ")
     

     print("What is my cat called?")
     print ("A - Bundles")
     print ("B - Buster")
     print ("C - Bean")
     answer = input("Select an option!")

     if answer.upper() == "B":           #Adding to the score.
         score = score + 10
     
     print("Score:", score)              #Printing 1 to the score.

     print("How many dogs do I have?")
     print ("A - Two")
     print ("B - Four")
     print ("C - One")
     answer = input("Select an option!")

     if answer.upper() == "A":
         score = score + 10

     print("Score:", score)

     print("What other pet do I own?")
     print ("A - Hamster")
     print ("B - Chinchilla")
     print ("C - Rabbit")
     answer = input("Select an option!")

     if answer.upper() == "B":
         score = score + 10

     print("Score:", score)

     print("Which band have I seen live?")
     print ("A - Panic! At the disco")
     print ("B - Twenty one pilots")
     print ("C - Fall out boy")
     answer = input("Select an option!")

     if answer.upper()== "C":
         score = score + 10

     print("Score:", score)
     

     print("Who is the lead singer of Panic! At the disco?")
     print ("A - Brendon Urie")
     print ("B - Patrick Stump")
     print ("C - Alex turner")
     answer = input("Select an option")

     if answer.upper()=="A":
         score = score + 10

     print("Score:", score)

     print("What colour is my cat?")
     print ("A - Black")
     print ("B - Ginger")
     print ("C - Mixed")
     answer = input("Select an option")

     if answer.upper()=="C":
         score = score + 10

     print("Score:", score)

     print("What are my two dogs called?")
     print("A - Jack&Harley")
     print("B - Pete&Joe")
     print("C - Max&Harley")
     answer = input("Select an option")

     if answer.upper()=="A":
          score = score + 10

     print("Score:", score)

     print("What dog does my gran own?")
     print("A - Doesnt have one")
     print("B - Jack russel")
     print("C - Husky")
     answer = input("Select an option")

     if answer.upper()=="C":
          score = score + 10

     print("Score:", score)
     
           
     print("How many sisters do I have?")
     print("A - Three")
     print("B - None")
     print("C - One")
     answer = input("Select an option ")

     if answer.upper()=="B":
          score = score + 10

     print("Score:", score)
     
     print("Where does my uncle live")
     print("A - Spain")
     print("B - USA")
     print("C - Russia")
     answer = input("Select an option")

     if answer.upper()=="A":
          score = score + 10

     print("Score:", score)
      



# Leave this at the bottom - it makes quiz run automatically when you
# run your code.
if __name__ == "__main__":
    quiz()
