import numpy as np

def solve(nov):

    eq = []

    for i in range(nov):
        eqs = str(input(f"Enter the {i+1} equation: "))
        eq.append(eqs)
    print("\n")

    print(eq,end="\n")


    var = []
    coeff = []
    for i in eq:

        i = i.replace(" ","")
        equation_ls = [a for a in i]
        
       # print(equation_ls)
        
       
        for ele in equation_ls:

            if ord(ele) in range(97, 123):                   #taking out variables in list var

                var.append(ele)
        
            elif ele in ["+","="]:
                pass

            else:

                coeff.append(ele)

    for _ in range(coeff.count('-')):
        coeff[coeff.index('-')+1] = coeff[coeff.index('-')] + coeff[coeff.index('-')+1]
        coeff.pop(coeff.index('-'))

    coeff = np.array(coeff).astype(np.int32).reshape((nov, nov+1))

    const = coeff[:, -1]
    const = const.reshape((nov, 1))

    del var[nov:]

    coeff = np.delete(coeff, -1, 1)  

    print(f"Coeff:\n{coeff}\n")
    print(f"Const:\n{const}\n")
    print(f"Var:\n{var}\n")
    
    ans = np.dot(np.linalg.inv(coeff), const).tolist()

    for i in range(len(var)):

        print(f"{var[i]}={ans[i]}")





if __name__=="__main__":

    print('''Please note that:
             1). Equations should have non zero coefficient.
             2). Please enter only single digit coefficient.
             3). Do not provide more than 1 space in between like 2x   +  3y   4  z  = 30.\n''')

    nov = int(input("Enter the number of variable: "))
    print("\n")

    solve(nov)