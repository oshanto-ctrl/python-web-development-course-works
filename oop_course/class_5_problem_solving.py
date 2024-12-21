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
'''
HELPER STATEMENT:
On the other hand, the selling price of the cach cake is 780, 600, 800, 650, and 660, 
respectively, per pound. Suddenly, the owner gives 5% discount on first 3 cakes and 
7% discount on rest of the cake. With the discount offer, 
Owner sells 5, 7, 10, 5, 9 pounds till today in total for cach cake. Now, owner wants to calculate the below business questions using Python programming language. To do it, owner hires a Python programmer who can make software to estimate the below queries:
'''

# 3 Owner wants to visualize the selling price before discount for each cake per pound.

# Selling price of each cake per pound
selling_price_bf = 780
selling_price_vc = 600
selling_price_rv = 800
selling_price_ls = 650
selling_price_cc = 660

# Owners' total cake sales in pound for the day
bf_sold_amount = 5
vc_sold_amount = 7
rv_sold_amount = 10
ls_sold_amount = 5
cc_sold_amount = 9

# Selling price of each cake per pound before discount
before_discount_selling_price_bf = selling_price_bf * bf_sold_amount
before_discount_selling_price_vc = selling_price_vc * vc_sold_amount
before_discount_selling_price_rv = selling_price_rv * rv_sold_amount
before_discount_selling_price_ls = selling_price_ls * ls_sold_amount
before_discount_selling_price_cc = selling_price_cc * cc_sold_amount

print(f"""
    Todays Report:
    Before Discount Each Cake Price (per pound)
    ---------------------------------------------
    Selling price of Black Forest {before_discount_selling_price_bf} bdt.
    Selling price of Vanilla Cake {before_discount_selling_price_vc} bdt.
    Selling price of Red Velvet {before_discount_selling_price_rv} bdt.
    Selling price of Lemon Sponge {before_discount_selling_price_ls} bdt.
    Selling price of Chocolate Cake {before_discount_selling_price_cc} bdt.
    """)

# 4. Owner wants to visualize the selling price after discount for each cake per pound.

# Each cake discount amount
discount_amount_on_bf = (selling_price_bf * bf_sold_amount) * 0.05
discount_amount_on_vc = (selling_price_vc * vc_sold_amount) * 0.05
discount_amount_on_rv = (selling_price_rv * rv_sold_amount) * 0.05
discount_amount_on_ls = (selling_price_ls * ls_sold_amount) * 0.07
discount_amount_on_cc = (selling_price_cc * cc_sold_amount) * 0.07

# First 3 cake has 5% discounts.
after_discount_selling_price_bf = before_discount_selling_price_bf - discount_amount_on_bf
after_discount_selling_price_vc = before_discount_selling_price_vc - discount_amount_on_vc
after_discount_selling_price_rv = before_discount_selling_price_rv - discount_amount_on_rv
# Last 2 cake has 7% discounts.
after_discount_selling_price_ls = before_discount_selling_price_ls - discount_amount_on_ls
after_discount_selling_price_cc = before_discount_selling_price_cc - discount_amount_on_cc

print(f"""
    After Discount Each Cake Price (per pound)
    ---------------------------------------------
    Selling price of Black Forest {after_discount_selling_price_bf} bdt.
    Selling price of Vanilla Cake {after_discount_selling_price_vc} bdt.
    Selling price of Red Velvet {after_discount_selling_price_rv} bdt.
    Selling price of Lemon Sponge {after_discount_selling_price_ls} bdt.
    Selling price of Chocolate Cake {after_discount_selling_price_cc} bdt.
    """)

# 5. Owner wants to estimate total amount of profit after sell for each cake.

# Total profit for each cake
profit_bf = after_discount_selling_price_bf - (total_inventory_cost_bf * bf_sold_amount)
profit_vc = after_discount_selling_price_vc - (total_inventory_cost_vc * vc_sold_amount)
profit_rv = after_discount_selling_price_rv - (total_inventory_cost_rv * rv_sold_amount)
profit_ls = after_discount_selling_price_ls - (total_inventory_cost_ls * ls_sold_amount)
profit_cc = after_discount_selling_price_cc - (total_inventory_cost_cc * cc_sold_amount)

print(f"""
    Total Profit After Selling Each Cake (per pound)
    ---------------------------------------------
    Profit from Black Forest {profit_bf} bdt.
    Profit from Vanilla Cake {profit_vc} bdt.
    Profit from Red Velvet {profit_rv} bdt.
    Profit from Lemon Sponge {profit_ls} bdt.
    Profit from Chocolate Cake {profit_cc} bdt.
    """)

# 6. Owner wants to estimate % of profit/loss after sell of each cake.

# Percentage of profit/loss for each cake
percentage_profit_bf = (profit_bf / (total_inventory_cost_bf * bf_sold_amount)) * 100
percentage_profit_vc = (profit_vc / (total_inventory_cost_vc * vc_sold_amount)) * 100
percentage_profit_rv = (profit_rv / (total_inventory_cost_rv * rv_sold_amount)) * 100
percentage_profit_ls = (profit_ls / (total_inventory_cost_ls * ls_sold_amount)) * 100
percentage_profit_cc = (profit_cc / (total_inventory_cost_cc * cc_sold_amount)) * 100

print(f"""
    Percentage of Profit/Loss After Selling Each Cake (per pound)
    ---------------------------------------------
    Percentage profit/loss from Black Forest {percentage_profit_bf:.2f}%.
    Percentage profit/loss from Vanilla Cake {percentage_profit_vc:.2f}%.
    Percentage profit/loss from Red Velvet {percentage_profit_rv:.2f}%.
    Percentage profit/loss from Lemon Sponge {percentage_profit_ls:.2f}%.
    Percentage profit/loss from Chocolate Cake {percentage_profit_cc:.2f}%.
    """)
