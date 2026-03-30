import java.util.Scanner;

public class e1003 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int x = scanner.nextInt();
        int y = scanner.nextInt();
        int resultado = x+y;

        System.out.printf("SOMA = %d\n", resultado);

        scanner.close();
    }
}
