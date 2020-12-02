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


    # coeff = []

    # for i in eq:

    #     i = i.replace(" ","")

    #     cox = i[:i.index("x")]
    #     coy = i[i.index("y")-2:i.index("y")]
    #     coz = i[i.index("z")-2:i.index("z")]

    #     coeff.append(cox)
    #     coeff.append(coy)
    #     coeff.append(coz)
    
    # coeff = np.array(coeff).reshape((3,3))
    # coeff = coeff.astype(np.int)
    # return(coeff)

    # def const(*eq):

    #     const = []

    #     for i in eq:

    #         i = i.replace(" ","")

    #         con = i[i.index("=")+1:]
        
    #         const.append(con)

    #     const = np.array(const).reshape((3,1))
    #     const = const.astype(np.int)
    #     return(const)

    # def sol(coeff,const):

    #     ans = np.dot(np.linalg.inv(coeff), const)
    #     ans = ans.tolist()

    #     x = ans[0][0]
    #     y = ans[1][0]
    #     z = ans[2][0]

    #     print(f"x = {int(x)}\ny = {int(y)}\nz = {int(z)}")

#        print(np.linalg.inv(coeff))

    # print(f"Solution :")
    # sol(coeff(*eq), const(*eq))




if __name__=="__main__":

    print('''Please note that:
             1). Equations should have non zero coefficient.
             2). Please enter only single digit coefficient.
             3). Do not provide more than 1 space in between like 2x   +  3y   4  z  = 30.\n''')

    nov = int(input("Enter the number of variable: "))
    print("\n")

    solve(nov)