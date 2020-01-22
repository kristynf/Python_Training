gender = (raw_input("What is your gender (m/f)?: "))
if gender == 'f':
    age = int(raw_input("What is your age?: "))
    if age >= 10 and age <=12:
        print "Congratulations, you qualify to play on the team!"
elif gender == 'm':
    print "Only females are joining this team!"
