pur_price = float(raw_input("What is the purchase price?: "))
if pur_price <= 10:
    print "Your price is:$", pur_price * 0.9
elif pur_price >= 10:
    print "Your price is:$", pur_price * 0.8
