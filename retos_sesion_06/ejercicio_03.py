#Una puerta tiene dos interruptores que controlan dos luces la puerta sólo debe abrirse cuando las dos luces están apagadas o las dos están encendidas, caso contrario la puerta no se abre, ¿qué operador lógico se puede utilizar?

a = True
b = False
print (not((a or b) and not (a and b)))
b = True
a = False
print (not((a or b) and not (a and b)))
a = True
b = True
print (not((a or b) and not (a and b)))
a = False
b = False
print (not((a or b) and not (a and b)))

# XNOR