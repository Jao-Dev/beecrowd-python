import java.util.Scanner;

public class e1006 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double pesoX = 2;
        double pesoY = 3;
        double pesoZ = 5;
        double pesoTotal = pesoX+pesoY+pesoZ;

        double x = scanner.nextDouble()*pesoX;
        double y = scanner.nextDouble()*pesoY;
        double z = scanner.nextDouble()*pesoZ;
        double resultado = (x+y+z)/pesoTotal;

        System.out.printf("MEDIA = %.1f\n", resultado);

        scanner.close();
    }
}
