def fun1():
    try:


        l=[1,5,6,5,7]
        i=int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some error occured")
        return 0

    finally:
        print("I am always executed")

X=fun1()
print(X)        