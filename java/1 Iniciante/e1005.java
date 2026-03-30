import java.util.Scanner;

public class e1005 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double pesoX = 3.5;
        double pesoY = 7.5;
        double pesoTotal = pesoX+pesoY;

        double x = scanner.nextDouble()*pesoX;
        double y = scanner.nextDouble()*pesoY;
        double resultado = (x+y)/pesoTotal;

        System.out.printf("MEDIA = %.5f\n", resultado);

        scanner.close();
    }
}
