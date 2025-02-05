"""
Cesar Matt Gaviria Sepulveda
student id: 101521980
Assignment 1
"""

gym_member = "Alex Alliton"  # string
preferred_weight_kg = 20.5  # float
highest_reps = 25  # int
membership_active = True  # boolean

# This dictionary is called workout_stats, it includes the names and the time (tuple values) spent on each activity
workout_stats = {
    "Alex": (20, 20, 20), #yoga, running, weightlifting
    "Jamie": (50, 50, 45), #yoga, running, weightlifting
    "Taylor": (35, 25, 40) #yoga, running, weightlifting
}

totals = {}  # A dictionary to store total workout minutes for each friend

#loop to calculate total workout minutes per person
for member, workouts in workout_stats.items():
    total_workout = sum(workouts)  # Sum the values in the tuple for each friend
    totals[member] = total_workout  # Store the total in the totals dictionary

#Nested list from workout minutes
workout_list = []  # This will hold the nested list

for workouts in workout_stats.values():
    workout_list.append(list(workouts))  # Convert the tuple to a list

#Slicing the workout_list to extract yoga and running minutes for all friends
yoga_running_minutes = []
for workout in workout_list:
    yoga_running_minutes.append(workout[:2])  # Take the first two values for Yoga and Running

print("Yoga and Running minutes for all friends:", yoga_running_minutes)



#slicing to extract the weightlifting minutes for the last two friends
weightlifting_minutes = []
for workout in workout_list[1:]:  # Skip the first friend to get the last two
    weightlifting_minutes.append(workout[2])  # Take the third value for Weightlifting

print("Weightlifting minutes for the last two friends:", weightlifting_minutes)



# loop with if statement to check whos workout time is >= than 120
for member, total in totals.items():
    if total >= 120:  # If the total workout minutes are greater than or equal to 120
        print("Great job staying active, " + member + "!")


#User inputs to check friends workout records based on the name
name = input("Please enter the name of the person you want to check: ")
if name in workout_stats:
    workouts = workout_stats[name]
    total_minutes = totals[name]

    print(f"\nWorkout stats for {name}:")
    print(f"Yoga: {workouts[0]} min, Running: {workouts[1]} min, Weightlifting: {workouts[2]} min")
    print(f"Total workout minutes: {total_minutes} min")
else:
    print(f"Friend {name} not found in the records.")

#finds the maximum value inside the dictionary and returns the key
highest = max(totals, key=totals.get)

print(f"The person with the highest workout time is {highest} with {totals[highest]} minutes.")

#finds the mim value and returns the key
lowest = min(totals, key=totals.get)
print(f"The person with the lowest workout time is {lowest} with {totals[lowest]} minutes.")





