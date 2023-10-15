import java.util.Scanner;

public class ej2_3b {
    public static void main(String[] args) {
        entero_pedido(0, 10, "El número está ok");
    }

    public static void entero_pedido(int min, int max, String msg) {
        Scanner read = new Scanner(System.in);
        int num = 0;
        boolean correct = false;

        while (!correct) {
            try {

                num = Integer.parseInt(read.nextLine());
                read.close();
                if (num >= min && num <= max) {
                    System.out.println(msg);
                    correct = true;
                } else {
                    System.out.println("Numero fuera de rango");
                    break;
                }
            } catch (Exception e) {
                System.out.println("No es un número válido, introduce uno");
            }

        }
        return;
    }
}