import java.util.ArrayList;
import java.util.Scanner;

public class e1105 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true) {
            int b = sc.nextInt();
            int n = sc.nextInt();
            if (b == 0 && n == 0) {
                break;
            }

            ArrayList<Integer> reserva = new ArrayList<>();
            for (int i = 0; i < b; i++) {
                reserva.add(sc.nextInt());
            }

            for (int i = 0; i < n; i++) {
                int d = sc.nextInt();
                int c = sc.nextInt();
                int v = sc.nextInt();

                int d1 = d - 1;
                int c1 = c - 1;
                reserva.set(d1, reserva.get(d1) - v);
                reserva.set(c1, reserva.get(c1) + v);
            }

            boolean mq0 = reserva.stream().allMatch(val -> val >= 0);
            if (mq0) {
                System.out.println("S");
            } else {
                System.out.println("N");
            }
        }
        sc.close();
    }
}
