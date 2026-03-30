import java.util.Scanner;

public class e1001 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int x = scanner.nextInt();
        int y = scanner.nextInt();
        int resultado = x+y;

        System.out.println("X = " + resultado);

        scanner.close();
    }
}
