/*
 * euros = float(input("Introduce la cantidad de EUR: "))

EURaGBP = 0.87 # A 23 de septiembre de 2023

def cambio(eur):
    return euros * EURaGBP * (1-0.02)

print(f"Para {euros}EUR vas a recibir {cambio(euros)}")
 */
import java.util.Scanner;
public class ej13 {
    public static void main(String []args) {
        Scanner read = new Scanner(System.in);
        System.out.println("Introduce la cantidad de EUR");
        float euros = Float.parseFloat(read.nextLine());
        read.close();
        float cambio = cambio(euros);
        System.out.println("El cambio de la cantidad introducida es de "+cambio+" GBP");
    }

    public static float cambio(float eur) {
        float EURaGBP = 0.87f;
        return eur * EURaGBP * (1-0.02f);
    }
}
