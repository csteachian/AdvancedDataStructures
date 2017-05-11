# Q13 May 2016 Car Park 2D array
# By Mr Simpson
# 24th March 2017

rules = [[0.0 for x in range(0,3)] for y in range(0,2)]
rules[0][0] = 0.5 # y is first, then x
rules[0][1] = 3.0
rules[1][0] = 5.0
rules[1][1] = 15.0
rules[1][2] = 30.0

#
duration =  4400 #87 minutes stayed in car park
days = (duration // 1440) + 1
cost = 0.0
if duration <= 30:
    cost = rules[0][0]
elif duration <= 120:
    cost = rules[0][1]
elif duration <= 150:
    cost = rules[0][1] + rules[1][0]
elif duration <= 240:
    cost = rules[0][1] + rules[1][1]
elif duration <= 1440:
    cost = rules[1][2]
else:
    cost = rules[1][2] * days
print("You stayed ",str(duration)," minutes. Cost is €",cost)

