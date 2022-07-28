
--------------------
for i in range(6):

    for j in range(i+1):

        print("*",end="")

    print()

#inverted half pyramid
----------------------
for i in range(6):

    for j in range(6-i):

        print("*",end="")

    print()

#hallow inverted pyramid
------------------------
n = int(input("enter the number : "))

for row in range(0,n):

    for col in range(0,n):

        if col==0 or row==0 or row+col==(n-1):

            print("*",end=" ")

        else:

            print(" ",end=" ")
    print()

#fully pyramid
--------------

for i in range(6):

    for k in range(6-i):

        print(end=" ")

    for j in range(i+1):

        print("*",end= " ")

    print()

#inverted fully pyramid
------------------------

for i in range(6):

    for k in range(6+i):

        print(end=" ")

    for j in range(6-i):

        print("*",end= " ")

    print()

#hollow fully pyramid
---------------------

n = int(input("enter the number : "))
k = 2
for row in range(1,n+1):

    for col in range(1,2*n):

        if row+col==n+1 or col-row==n-1:

            print("*",end="")

        elif row==n and col!=k:

            print("*",end="")

            k=k+2

        else:
            print(end=" ")

    print()


