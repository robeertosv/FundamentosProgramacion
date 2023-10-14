import java.util.Scanner;
public class ej7 {
    public static void main(String []args) {
        Scanner read = new Scanner(System.in);
        System.out.println("Dime un número");
        String num = read.nextLine();
        read.close();
        int number = Integer.parseInt(num);
        number = number +1;
        System.out.println("El número "+num+" + 1 = "+number);
    }
}
