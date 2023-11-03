public class ej4 {
    public static void main(String []args) {
        int num_hijos = 4;
        int ingresos = 3000;
        int ingreso_imponible = ingresos - 600 -60*num_hijos;

        float impuesto = ingreso_imponible / 3;

        System.out.println(impuesto);
    }
}
