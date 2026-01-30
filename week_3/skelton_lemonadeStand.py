"""
    Title: skelton_lemonadeStand.py
    Author: Nicholas Skelton
    Date: 29 January 2026
    Description: Hands-On 2.1: Functions
"""

def calculate_cost(lemons_cost, sugar_cost):
    return lemons_cost + sugar_cost

def calculate_profit(lemons_cost, sugar_cost, selling_price):
    return selling_price - (lemons_cost + sugar_cost)

lemons_cost = 3
sugar_cost = 2
selling_price = 7

total_cost = calculate_cost(lemons_cost, sugar_cost)

total_profit = calculate_profit(lemons_cost, sugar_cost, selling_price)

output = f"With lemons costing ${lemons_cost} and sugar costing ${sugar_cost} these days, I had to raise the price for a cup of lemonade to ${selling_price} - just to make a measly ${total_profit} on every sale. Oh, and just in case you can't do simple arithmetic, I have to spend ${total_cost} to make 1 cup."

print(output)