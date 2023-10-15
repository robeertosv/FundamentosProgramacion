
/*importeVentas = float(input("Introduce cuánto has vendido este mes: "))

salario = ( 2000 + (importeVentas + importeVentas * 0.03) ) * (1 - 0.32)

print("Este mes vas a cobrar:",salario,"euros")*/
import java.util.Scanner;

public class ej12 {
    public static void main(String[] args) {
        Scanner read = new Scanner(System.in);
        System.out.println("Cuanto has vendido este mes??");
        float importeVentas = Float.parseFloat(read.nextLine());
        read.close();
        float salario = (2000 + (importeVentas + importeVentas * 0.3f)) * (1 - 0.32f);
        System.out.println("Este mes vas a cobrar: "+salario+" EUR");
    }
}
