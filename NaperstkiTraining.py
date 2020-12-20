import random
cells={
"L":random.randint(1,0)
}
if cells ["L"]:
    cells["R"]:0
    cells["C"]:0
else:
    cells["C"]=random.randint(0,1)
    if cells["C"]:
        cells["R"]=0
    else:
        cells["R"]=1
guess=input("Please choose a cell:")
if guess in list(cells):
    if cells[guess]==1:
        print("You have guessed right")
    else:
        print("Try again")
else:
        print("Wrong cell")
