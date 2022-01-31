# Author: ATN 1/27/22

# def food_costs(groceries, costs):
#     # making sure that the original lists will not be altered
#     groceries_mod = groceries
#     costs_mod = costs

#     # for each nested list
#     for x in groceries_mod:
#         for i, v in enumerate(x):
#             # formats each list entry to add the costs
#             x[i] = v + ": $" + str(costs_mod[0])
#             # remove the cost entry after using
#             del(costs_mod[0])
#     return groceries_mod
       

# print(food_costs([['apple','pear','banana'],['salmon','tuna','cod'],['milk','eggs','yogurt']],[1.99,2.99,0.99,9.99,10.99,6.99,3.49,2.49,1.49]))

# def factorial(n):
#     counter = 1
#     value = ""

#     while counter < n + 1:
#         value += str(counter)
#         counter += 1
#     return value

# print(factorial(5))

# def fibonacci (n):
#     # setting the first two values as a starting point
#     values = [0, 1]
#     x = 0
#     # setting a finite number of iterations
#     while x < n:
#         # adding the current value to the previous
#         values.append(values[x] + values[-1])
#         x += 1
#     return values

# print(fibonacci(10))
