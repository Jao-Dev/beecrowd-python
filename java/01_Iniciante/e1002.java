import java.util.Scanner;

public class e1002 {
    public static void main(String[] args) {
       Scanner scanner = new Scanner(System.in);
       
       double x = scanner.nextDouble();
       double area = 3.14159 * Math.pow(x, 2);

       System.out.printf("A=%.4f\n", area);
       
       scanner.close();
    }
}