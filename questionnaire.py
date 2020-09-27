#First Question
print("Hey there! I'm your virtual assitant. May I know your name?")
name = str(input())
print("Hey, " + name + "." + " It's awesome to meet you.")
print("Let me ask you a few questions to help you out.")
rain = str(input("Is it raining outside?"))
if rain in ['yes', 'yup', 'Yes', 'YES']:
    print("You'll need an umbrella")
    
if rain in ['no', 'nope', 'nah', 'No', 'NO']:
     print("You can go without an umbrella.")
     
cold = str(input("Is it cold outside?"))

if cold in ['yes', 'yup', 'Yes', 'YES']:
    print("Take a jacket!")

if cold in ['no', 'nope', 'nah', 'No', 'NO']:
    print("You won't need a coat")    
    
driving = str(input("Are you going to be driving?"))

if driving in ['yes', 'yup', 'Yes', 'YES']:
    print("Okay.")
    eligibility = str(input("Are you below 18?"))

    if eligibility in ['yes', 'yup', 'Yes', 'YES']:
        print("Don't drive!")
    
    elif eligibility in ['no', 'nope', 'nah', 'No', 'NO']:
        print("Go ahead. Have a great day!")
    
elif driving in ['no', 'nope', 'nah', 'No', 'NO']:
    print("You're not polluting the environment. Good job! Have an awesome day.")

else :
    print("That's not an answer")

