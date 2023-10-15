import java.util.Scanner;

public class ej1_3b {
    public static void main(String[] args) {
        leer_entero_validado();
    }

    public static Boolean leer_entero_validado() {
        Scanner read = new Scanner(System.in);
        boolean correcto = false;
        Object num = null;

        while(!correcto) {
            try {
                
                System.out.println("Introduce un número: ");
                num = Integer.parseInt(read.nextLine());
                read.close();
                correcto = true;
            } catch (Exception e) {
                System.out.println("No has introducido un número válido, intentalo de nuevo");
            }
        }

        return correcto;
    }
}