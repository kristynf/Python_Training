age = float(raw_input("What is your age?: "))
gender = (raw_input("What is your gender (m/f)?: "))
if age >= 10 and age <= 12 and gender == 'f':
    print "Congrations, you qualify to play on the team!"
elif age < 10 or age > 12 or gender != 'f':
    print "Sorry, there are other teams you may qualify for"
    
