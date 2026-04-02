import java.util.ArrayList;
import java.util.Scanner;

public class e1064 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        ArrayList<Double> x = new ArrayList<>();

        for (int i=0; i<6; i++){
            double y = sc.nextDouble();
            if(y>0){
                x.add(y);
            }
        };

        double soma = 0;
        for (double i:x){soma+=i;}

        double media = soma/x.size(); 
        int cont = x.size();

        System.out.printf("%d valores positivos\n", cont);
        System.out.printf("%.1f\n", media);
        
        sc.close();
    }
}
