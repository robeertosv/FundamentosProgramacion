public class ej5 {
    public static void main(String[] args) {
        int[] hora = { 15, 23, 28 };
        int segundosActual = hora[0] * 3600 + hora[1] * 60 + hora[2];
        int segundosMediaNoche = 24 * 3600;

        int segundosAMediaNoche = segundosMediaNoche - segundosActual;
        System.out.println("Llevamos: " + segundosActual + " segundos de día. Quedan " + segundosAMediaNoche
                + " segundos para media noche");
    }
}
