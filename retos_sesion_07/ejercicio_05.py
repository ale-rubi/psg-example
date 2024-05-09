# Escribe un programa que reciba una cadena y retorna verdadero o falso si es palindrome la frase o palabra ejemplo "Anita lava la Tina" es verdad

a = "Anita lava la Tina"
a2 = a.lower()
a3 = a2.replace(" ","")
b = a3[::-1]
print (a , a2 , a3)
print (a3==b)