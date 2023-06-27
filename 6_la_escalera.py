"""
 * Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 * 
 * Ejemplo: 4
 *         _   
 *       _|   
 *     _|          
 *   _|               
 * _|                    
 * 
"""


def print_ladder(steps):
    
    if steps == 0:
        print("__")
    elif steps>0:
        space = steps * 2
        print(" "*space + "_")
        for i in range(steps):
            space-=2
            print(" "*space + "_|")         
    else:
        space = -1
        print("_")
        for i in range((steps*-1)):
            space+=2
            print(" "*space + "|_")


print_ladder(0)
print_ladder(4)
print_ladder(-4)