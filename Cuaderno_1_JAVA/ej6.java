import java.util.Scanner;

public class ej6 {
    public static void main(String []args) {
        Scanner read = new Scanner(System.in);
        System.out.println("Cuantos km has hechado en el asfalto?");
        float distancia = Float.parseFloat(read.nextLine());
        System.out.println("Cuanto diesel has hechado?");
        float litrosFuel = Float.parseFloat(read.nextLine());
        System.out.println("A cuanto está el diesel?");
        float precioFuel = Float.parseFloat(read.nextLine());
        System.out.println("En otros gastos, ¿cuánto te has fundido?");
        float costesVarios = Float.parseFloat(read.nextLine());

        read.close();

        float costeGasolina = litrosFuel * precioFuel;
        float kilometroPorLitro = distancia / litrosFuel;
        float costeTotalPorKM = (costeGasolina + costesVarios) / distancia;

        System.out.println("En gasolina has gastado "+costeGasolina+"EUR \n" + //
                "El consumo ha sido de "+kilometroPorLitro+" km/L \n" + //
                "El coste total \r\n" + //
                "por kilómetro ha sido de "+costeTotalPorKM+" EUR/km");
    }
}