'''
Scenario:
Problem Solving 1
Loss & Profit Calculation
A cake owner wants to make a program for his cake business. In this program, 
he wants to calculate profit and loss after selling a particular cake. 
For example, A cake owner sells five different flavors of cake in his website. 
The name of each cake is: black forest, Vanilla cake, Red Velvet, 
Lemon Sponge Cake, and Chocolate Cake. To make these cakes, 
the owner has to pay different types of inventory cost such as 
raw material cost (180, 150, 220, 165, 170 for each cake pound, respectively) 
transportation cost (150 for each pound), utility cost
(3% on material and transportation cost in total for each pound), 
space cost (50 for each pound) and staff cost (60 for each pound).
On the other hand, the selling price of the cach cake is 780, 600, 800, 650, and 660, 
respectively, per pound. Suddenly, the owner gives 5% discount on first 3 cakes and 
7% discount on rest of the cake. With the discount offer, 
Owner sells 5, 7, 10, 5, 9 pounds till today in total for cach cake. Now, owner wants to calculate the below business questions using Python programming language. To do it, owner hires a Python programmer who can make software to estimate the below queries:

1. Owner wants to visualize the each cake flavor types
2. Owner wants to visualize the total inventory cost for each cake per pound
'''

# 1. Owner wants to visualize the each cake flavor types.
cake_1 = "bf"
cake_2 = "vc"
cake_3 = "rv"
cake_4 = "ls"
cake_5 = "cc"

print(f"Flavor of the all cake flavors: {cake_1}, {cake_2}, {cake_3}, {cake_4}, {cake_5}")

# 2. Owner wants to visualize the total inventory cost for each cake per pound
# Each cake has costs such as raw material costs, transportation costs, utility costs,
# space costs, and staff costs.

# Raw material costs
material_cost_bf = 180
material_cost_vc = 150
material_cost_rv = 220
material_cost_ls = 165
material_cost_cc = 170

# Transportation costs
transporation_cost = 150

# Utility costs = 3% on material and transportation cost in total for each pound
material_transportation_cost_bf = material_cost_bf + transporation_cost
material_transportation_cost_vc = material_cost_vc + transporation_cost
material_transportation_cost_rv = material_cost_rv + transporation_cost
material_transportation_cost_ls = material_cost_ls + transporation_cost
material_transportation_cost_cc = material_cost_cc + transporation_cost

utility_cost_bf = (material_transportation_cost_bf * 0.03)
utility_cost_vc = (material_transportation_cost_vc * 0.03)
utitlity_cost_rv = (material_transportation_cost_rv * 0.03)
utility_cost_ls = (material_transportation_cost_ls * 0.03)
utility_cost_cc = (material_transportation_cost_cc * 0.03)

# Space costs per pound cake
space_cost = 50
# Staff costs per pound cake
staff_cost = 60

# Total inventory cost of each flavor cake per pound.
total_inventory_cost_bf = (material_transportation_cost_bf 
                           + utility_cost_bf 
                           + space_cost 
                           + staff_cost)
total_inventory_cost_vc = (material_transportation_cost_vc 
                           + utility_cost_vc 
                           + space_cost 
                           + staff_cost)
total_inventory_cost_rv = (material_transportation_cost_rv 
                           + utitlity_cost_rv 
                           + space_cost 
                           + staff_cost)
total_inventory_cost_ls = (material_transportation_cost_ls 
                           + utility_cost_ls 
                           + space_cost 
                           + staff_cost)
total_inventory_cost_cc = (material_transportation_cost_cc 
                           + utility_cost_cc 
                           + space_cost 
                           + staff_cost)

print(f"Total inventory cost of per pound Black Forest = {total_inventory_cost_bf} bdt.")
print(f"Total inventory cost of per pound Vanilla Cake = {total_inventory_cost_vc} bdt.")
print(f"Total inventory cost of per pound Red Velvet = {total_inventory_cost_rv} bdt.")
print(f"Total inventory cost of per pound Lemon Sponge = {total_inventory_cost_ls} bdt.")
print(f"Total inventory cost of per pound Chocolate Cake = {total_inventory_cost_cc} bdt.")

''' Assignment 1 '''
'''
3. 
Owner wants to visualize the selling price 
before discount for each cake per pound.

4.
Owner wants to visualize the selling price
after discound for each cake per pound.

5.
Owner wants to estimate total amount of profit
after sell for each cake.

6.
Owner wants to estimate % of profit/loss
after sell of each cake.
'''



