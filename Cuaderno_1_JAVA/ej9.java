/*
a = 2.5
b = 5.25
c = 8.2
def media(a, b, c):
    return (a + b + c) / 2
def sumaTotal(a, b, c):
    return a + b + c
def productoTotal(a, b, c):
    return a * b * c
print(f'La media de {a}, {b} y {c} es: {media(a,b,c)}\nLa suma total de esos tres números es {sumaTotal(a,b,c)}\nEl producto total es {productoTotal(a,b,c)}')
 */
public class ej9 {
    public static void main(String []args) {
        float a = 2.5f;
        float b = 5.25f;
        float c = 8.2f;

        System.out.println("La media de a,b y c: "+ media(a,b,c));
        System.out.println("La suma de a,b y c: "+ sumaTotal(a,b,c));
        System.out.println("El producto de a,b y c: "+ productoTotal(a,b,c));
    }

    public static float media(float a, float b, float c) {
        return (a+b+c)/2;
    }

    public static float sumaTotal(float a, float b, float c) {
        return a+b+c;
    }

    public static float productoTotal(float a, float b, float c) {
        return a*b*c;
    }
}