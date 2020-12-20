import random
naperstki={
"1st": random.randint(0,1),
"2nd": random.randint(0,1),
"3rd": random.randint(0,1)
}
choice=input("please choose naperstok: 1st, 2nd, 3rd ")
if naperstki[choice]==1:
    print("yes")
else:
    print("no")
