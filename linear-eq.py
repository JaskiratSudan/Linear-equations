import numpy as np

def solve(*eq):

    def coeff(*eq):

        coeff = []

        for i in eq:

            i = i.replace(" ","")

            cox = i[:i.index("x")]
            coy = i[i.index("y")-2:i.index("y")]
            coz = i[i.index("z")-2:i.index("z")]

            coeff.append(cox)
            coeff.append(coy)
            coeff.append(coz)
    
        coeff = np.array(coeff).reshape((3,3))
        coeff = coeff.astype(np.int)
        return(coeff)

    def const(*eq):

        const = []

        for i in eq:

            i = i.replace(" ","")

            con = i[i.index("=")+1:]
        
            const.append(con)

        const = np.array(const).reshape((3,1))
        const = const.astype(np.int)
        return(const)

    def sol(coeff,const):

        ans = np.dot(np.linalg.inv(coeff), const)
        ans = ans.tolist()

        x = ans[0][0]
        y = ans[1][0]
        z = ans[2][0]

        print(f"x = {int(x)}\ny = {int(y)}\nz = {int(z)}")

#        print(np.linalg.inv(coeff))

    print(f"Solution :")
    sol(coeff(*eq), const(*eq))



if __name__=="__main__":

    print('''Please note that:
             1). Equations should have non zero coefficient.
             2). Do not provide more than 1 space in between like 2x   +  3y   4  z  = 30.
             3). Answers are rounded up.\n''')

    eq1 = str(input("Enter 1st eq. : "))
    eq2 = str(input("Enter 2nd eq. : "))
    eq3 = str(input("Enter 3rd eq. : "))
    print("\n")

    solve(eq1,eq2,eq3)