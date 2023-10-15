/*
 * fruta_1 = input("Dime una fruta: ")
fruta_2 = input("Dime otra fruta: ")

frutero = fruta_1 + " y " + fruta_2

print(f"En el frutero hay {frutero}")
 */
import java.util.Scanner;
public class ej15 {
    public static void main(String []args) {
        Scanner read = new Scanner(System.in);
        
        System.out.println("Dime una fruta: ");
        String fruta_1 = read.nextLine();

        System.out.println("Dime otra fruta: ");
        String fruta_2 = read.nextLine();

        read.close();
        String frutero = fruta_1 +" y "+ fruta_2; 
        System.out.println("En el frutero hay: "+frutero);
    }
}
