import os

def refine(list):
    res = []
    for item in list:
        if(item.endswith(".png") or item.endswith(".jpg") or item.endswith(".jpeg") or item.endswith(".cdr") or item.endswith(".svg")):
            res.append(item)
    return res

dirs = os.listdir("./")
refined = refine(dirs)

isCreated = False
for dir in dirs:
    if(dir == "IMAGES"):
        isCreated = True
        break
if(not isCreated):
    os.system("mkdir IMAGES")
os.system("cd IMAGES")

for item in refined:
    os.system(f"mv ${item} IMAGES/")

print("Task Completed...")