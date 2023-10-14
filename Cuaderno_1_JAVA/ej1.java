public class ej1 {
    public static void main(String []args) {
        Object myInt = null;
        Object myFloat = null;
        myInt = 3;
        String myStr = "Roberto";
        myFloat = 3.45f;

        System.out.println(myInt.getClass().getSimpleName());
        System.out.println(myStr.getClass().getSimpleName());
        System.out.println(myFloat.getClass().getSimpleName());
    }
}