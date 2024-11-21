def F(L):
    for n in range(1, L[0]+1):
        S = ""
        for t in L[1:]:
            if n%t[0] == 0:
                S = S + t[1]
        if S == "":
            print(n)
        else:
            print(S)

F([1000, [3, "Fizz"], [5, "Buzz"]])

#Input as a list containing a number and as many lists of the form [NUMBER, "STRING"]
#The first number tells the program up to what number it should run, and the lists tell the program that at any number divisible by NUMBER, it should output STRING (as well as any other strings that fit the conditions)