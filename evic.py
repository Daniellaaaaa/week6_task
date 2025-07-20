#QUESTION 1
print("QUESTION 1")

user_bio=input("Please Enter Your Bio:\n")
print(len(user_bio))
user_first_20=user_bio[0:21]

print(user_first_20)
user_last_20=user_bio[-20:]
print(user_last_20)
print(len(user_last_20))

#QUESTION 2
print("\n QUESTION 2")

total_bill=float(input("What is the total bill amount: \n N"))
print(total_bill)
num_of_people=int(input("What is the total number of people: \n "))
print(num_of_people)
total=total_bill/num_of_people
print(f"The total bill is N{total_bill:.2f} amongst {num_of_people} friends, Each person should pay N{total:.2f}")

#QUESTION 3
print("\n QUESTION 3")

fav_movie=input("Please enter the name of your movie: \n")
times_of_watch=int(input("How many times have you watched it: \n"))
print(f"I've watched {fav_movie} {times_of_watch} times.")

print(fav_movie.upper())
print(fav_movie[-3:])

#QUESTION 4
print("\n QUESTION 4")

monday_steps=int(input("How many steps did you take on Monday: \n"))
tuesday_steps=int(input("How many steps did you take on Tuesday: \n"))
wednesday_steps=int(input("How many steps did you take on Wednesday: \n"))

total_steps=monday_steps + tuesday_steps + wednesday_steps
print(total_steps)

average_steps= (monday_steps + tuesday_steps + wednesday_steps) / 3
print(average_steps)

print(f"You walked a total of {total_steps:,} steps in 3 days. That's an average of {average_steps} steps per day.")

#QUESTION 5
print("\n QUESTION 5")

password=input("Please enter your password: \n")
print(password)
length=len(password)
first_char=password[0]
other_char=length-2
num_stars="*"*other_char
last_char=password[-1]

print(first_char+num_stars+last_char)
print(len(password))
