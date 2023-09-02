print("Ingresa el mensaje cifrado")
mensajecifrado = input()
print("Ingresa el numero de veces que se movieron las letras")
veces = int(input())

mensajedecifrado = ""

for i in range(0, len(mensajecifrado), 1):
    letra = mensajecifrado[i]
    minuscula = (letra >= 'a' and letra <= 'z')
    mayuscula = (letra >= 'A' and letra <= 'Z')
    if not(minuscula or mayuscula):
        mensajedecifrado += letra
    else:
        ascii = ord(letra)
        base_ascii = ord('a')
        if mayuscula:
            base_ascii = ord('A')
        nuevo_ascii = (ascii - base_ascii - veces) % 26 + base_ascii
        nueva_letra = chr(nuevo_ascii)
        mensajedecifrado += nueva_letra

print("Mensaje decifrado:", mensajedecifrado)