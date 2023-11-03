import java.util.Scanner;
public class ej8 {
    public static void main(String []args) {
        Scanner read = new Scanner(System.in);

        System.out.println("Dime la base del rectángulo");
        float base = Float.parseFloat(read.nextLine());

        System.out.println("Dime la altura del rectángulo");
        float altura = Float.parseFloat(read.nextLine());
        read.close();

        float area = base * altura;

        System.out.println("El área del rectángulo de base "+base+" y altura "+altura+" es "+area);
    }
}
