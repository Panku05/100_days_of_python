borrow = 5000
apr = 0.05
for i in range(10):
    borrow += (borrow * apr)
    print("year", i+1, "is", round(borrow, 2), "$")
    