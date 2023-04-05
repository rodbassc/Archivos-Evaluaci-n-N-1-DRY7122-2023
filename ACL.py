ACL = int(input("Por favor ingrese número de ACL: "))

if ACL >= 1 and ACL <=99:
    print("Corresponde a una ACL de tipo ESTANDAR")

elif ACL >= 100 and ACL <= 199:
    print("Corresonde a una ACL de tipo EXTENDIDA")

else:   
    print("No corresponde a una ACL")

