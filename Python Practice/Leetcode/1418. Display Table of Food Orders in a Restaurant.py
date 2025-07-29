
"""
Given the array orders, which represents the orders that customers have done in a restaurant. More specifically orders[i]=[customerNamei,tableNumberi,foodItemi] where customerNamei is the name of the customer, tableNumberi is the table customer sit at, and foodItemi is the item customer orders.

Return the restaurant's “display table”. The “display table” is a table whose row entries denote how many of each food item each table ordered. The first column is the table number and the remaining columns correspond to each food item in alphabetical order. The first row should be a header whose first column is “Table”, followed by the names of the food items. Note that the customer names are not part of the table. Additionally, the rows should be sorted in numerically increasing order.



Example 1:

Input: orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
Output: [["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]]
Explanation:
The displaying table looks like:
Table,Beef Burrito,Ceviche,Fried Chicken,Water
3    ,0           ,2      ,1            ,0
5    ,0           ,1      ,0            ,1
10   ,1           ,0      ,0            ,0
For the table 3: David orders "Ceviche" and "Fried Chicken", and Rous orders "Ceviche".
For the table 5: Carla orders "Water" and "Ceviche".
For the table 10: Corina orders "Beef Burrito".
Example 2:

Input: orders = [["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]]
Output: [["Table","Canadian Waffles","Fried Chicken"],["1","2","0"],["12","0","3"]]
Explanation:
For the table 1: Adam and Brianna order "Canadian Waffles".
For the table 12: James, Ratesh and Amadeus order "Fried Chicken".
Example 3:

Input: orders = [["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]]
Output: [["Table","Bean Burrito","Beef Burrito","Soda"],["2","1","1","1"]]

"""

import numpy as np
def displayTable(orders: list[list[str]]) -> list[list[str]]:

    orders = np.array(orders)[:,1:3]

    foods = sorted(list(set(orders[:,1])))
    foods.insert(0,"Table")
    foods = {x:i for i,x in enumerate(foods)}

    tables = list(set(orders[:, 0]))

    zeros = np.zeros((len(tables)+1,len(foods)))

    zeros[0,:] = range(len(foods))
    zeros[1:,0] = tables
    zeros.sort(axis=0)

    print(tables)
    print(zeros)
    print(foods)
    print(zeros[:,0])

    for x in orders:
        print(foods.values())
        food_change = foods[x[1]]
        table_place = np.where(zeros[:,0] == int(x[0]))[0]
        print(table_place,food_change)
        zeros[table_place,food_change] = zeros[table_place,food_change] + 1

    list_zeros = list(zeros)
    list_zeros[0] = foods.keys()
    list_zeros = [list(x) for x in list_zeros]

    list_zeros = [
        [str(int(item)) if isinstance(item, float) and item.is_integer() else str(item) for item in sublist]
        for sublist in list_zeros]

    return list_zeros

print(displayTable(orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]))












