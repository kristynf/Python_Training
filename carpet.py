print "This program will calculate the square footage of carpet needed for a room"
length = float(raw_input("What is the length of the room: "))
width = float(raw_input("What is the width of the room: "))
cost_per_yard = float(raw_input("What is the cost per yard?: "))
print type(length)
print type(width)
sqft = length * width
sqyd = sqft / 9.0
total_cost = cost_per_yard * sqyd
print "You need,", sqft, "sqft of carpet for the room"
print "This is:", sqyd, "Square yards of carpet."
print "The price of your carpet is $", total_cost


