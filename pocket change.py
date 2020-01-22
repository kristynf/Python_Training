print "This program will calculate the value of your pocket change"
quarters = float(raw_input("How many quarters do you have?: "))
dimes = float(raw_input("How manu dimes do you have: "))
nickels = float(raw_input("How many nickels do you have: "))
pennies = float(raw_input("How many pennies do you have: "))
tot_quar = 0.25 * quarters
tot_dime = 0.10 * dimes
tot_nic = 0.05 * nickels
tot_pen = 0.01 * pennies
pocket = tot_quar + tot_dime + tot_nic + tot_pen
print "You have $", pocket, "total change in your pocket."


