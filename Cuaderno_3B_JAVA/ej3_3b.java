import java.util.*;

public class ej3_3b {
    public static void main(String[] args) {
        System.out.println(media());
    }

    public static float media() {
        Scanner read = new Scanner(System.in);
        boolean correct = false;
        ArrayList<Integer> nums = new ArrayList<Integer>();
        int cantidad = 0;
        float media = 0;

        while (!correct) {
            try {
                System.out.println("Cuantos números vas a introducir?");
                cantidad = Integer.parseInt(read.nextLine());
            } catch (Exception e) {
                System.out.println("Introduce una cantidad de número válida");
                continue;
            }

            for (int i = 0; i < cantidad; i++) {
                try {
                    System.out.println("Introduce el " + i + 1 + "º número: ");
                    nums.add(Integer.parseInt(read.nextLine()));
                    int sumatorio = 0;
                    for (int j = 0; j < cantidad; j++) {
                        sumatorio += nums.get(j);
                    }
                    read.close();

                    correct = true;
                    media = sumatorio / cantidad;
                } catch (Exception e) {
                    System.out.println("No has introducido un número válido");
                    break;
                }
            }

        }
        return media;
    }
}