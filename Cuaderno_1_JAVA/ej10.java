/*
La temperatura expresada en grados centígrados TC, se puede convertir a
grados Fahrenheit (TF) mediante la siguiente fórmula:
TF = 9.0*TC/5.0 + 32.0
Escribe un programa que utilizando un cierto valor de temperatura en grados
Fahrenheit, muestre en pantalla la temperatura equivalente en grados
Centígrados.

"""

gradosF = float(input('Introduce un valor para la temperatura: '))

# Si TF = (9.0 * TC / 5.0) + 32.0
# TC = (32*5 - 5TF) / 9

def conversor(TF):
    return (TF - 32) * (5/9)

print(f'{gradosF}ºF es igual a {conversor(gradosF)}ºC')
 */
public class ej10 {
    public static void main(String []args) {
        System.out.println("50ºF son: "+conversor(50)+"ºC");
    }

    public static float conversor(float TF) {
        return (TF - 32) * 5/9;
    }
}
