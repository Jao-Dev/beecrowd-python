import java.util.ArrayList;
import java.util.Scanner;

public class e1065 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        ArrayList<Integer> x = new ArrayList<>();

        for (int i=0; i<5; i++){
            int y = sc.nextInt();
            if(y%2==0){
                x.add(y);
            }
        };

        int cont = x.size();
        System.out.printf("%d valores pares\n", cont);

        sc.close();
    }
}
