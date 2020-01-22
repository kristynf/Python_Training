print "This program will calculate if you can make the next gas station if it is 200 km away"
tank_size = float(raw_input("What is your tank size, in liters: "))
tank_full = float(raw_input("How full is your tank now: "))
economy = float(raw_input("How many kilomters per liter does your car get?: "))
veh_range = (tank_size * (tank_full/100) * economy)
if veh_range <= 200:
    print "You only have ", veh_range, "km left. You need to get fuel now!"
elif veh_range > 200:
    print "You have ", veh_range, "km left. You will make it to the next gas station!"
    

