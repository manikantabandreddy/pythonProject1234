import csv
with open(r"C:\Users\ACER\OneDrive\Desktop\new.csv","r") as readobj:
    read=csv.reader(readobj)
    read=list(readobj)
    for i in read:
        print(i)
print("read the file suceesfully")

row=["efDfsvsvdfZDcSDfDfDFFDgzsfgzdfgzd"]
with open(r"C:\Users\ACER\Desktop\mani.csv","w") as writeobj:
    write = csv.writer(writeobj)
    write.writerows(row)

newrow=["effdSFSDfSDSfDfDfSDfSDFSD"]
with open(r"C:\Users\ACER\Desktop\mani.csv","a") as appendobj:
    append = csv.writer(appendobj)
    append.writerow(newrow)