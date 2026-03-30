import java.util.Scanner;

public class e1009 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String nome = scanner.next();
        double sFixo = scanner.nextDouble();
        double vendas = scanner.nextDouble();

        double salario = (vendas*0.15)+sFixo;

        
        System.out.printf("TOTAL = R$ %.2f\n", salario);

        scanner.close();
    }
}
