def nom_cuad(x):
    return (f"El cuadrado de {x} es {x*x}")

def dec_to_bin(dec):
    bin_list = []
    
    while dec >= 1:
        print(f"current decimal value is {dec}")
        if dec%2 == 0:
            bin_list.insert(0, '0')
        else:
            bin_list.insert(0, '1')
        dec = int(dec / 2)
        print(f"current binary value is {bin_list}")

    bin_number = ''.join(bin_list)
    print(bin_number)



def main():
    #print("Se calcularan cuadrados de numeros")

    #print("Ingrese un número entero: ")
    #n1 = int(input())
    #print("Ingrese otro número entero: ")
    #n2 = int(input())

    #for x in range(n1,n2+1):
        #print(f"El valor de x = {x}")
        #print(nom_cuad(x))

    #print("Es todo por ahora")
    dec_to_bin(1246)

main()