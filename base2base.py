#Siddharth Singh
#ss5683@drexel.edu
#CS 164-66H
#Honors Project
#Base Converter

def convert(n, ibase, obase):
    try:
        dec = None
        if ibase in ('2', '8', '10', '16'):
            dec = int(n, int(ibase))
        else:
            print("Invalid base!")
            restart()

        if obase == '2':
            res = bin(dec)[2:]
        elif obase == '8':
            res = oct(dec)[2:]
        elif obase == '10':
            res = str(dec)
        elif obase == '16':
            res = hex(dec)[2:]
        else:
            print("Invalid base!")
            restart()
        return res
    except ValueError:
        print("Invalid number!")
        restart()

def restart():
    print("\n")
    main()

def main():
    ibase = input("Enter the input base [2/8/10/16]: ")
    n = input("Enter the number: ")
    obase = input("Enter the output base [2/8/10/16]: ")
    res = convert(n, ibase, obase)
    print("Result: " + res)
    restart()

if __name__ == "__main__":
    main()