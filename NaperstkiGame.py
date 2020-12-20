import random
cells={
"L": random.randint(0,1)
}
if cells["L"]:
    cells["C"]=0
    cells["R"]=0
else:
    cells["C"]=random.randint(0,1)
