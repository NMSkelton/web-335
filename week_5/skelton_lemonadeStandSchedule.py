"""
    Title: skelton_lemonadeStandSchedule.py
    Author: Nicholas Skelton
    Date: 14 February 2026
    Description: Hands-On 3.1: Conditionals, Lists, and Loops
"""


tasks = ["Squeeze Lemons", "Add Sugar", "Add Ice Cubes", "Stir", "Pour Lemonade"]

for taskList in tasks:
    print(taskList)

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for schedule in days:
    if schedule == "Sunday" or schedule == "Saturday":
      print("Day off. Please rest.")
    elif schedule == "Monday":
      print(tasks[0])
    elif schedule == "Tuesday":
      print(tasks[1])
    elif schedule == "Wednesday":
      print(tasks[2])
    elif schedule == "Thursday":
      print(tasks[3])
    elif schedule == "Friday":
      print(tasks[4])
