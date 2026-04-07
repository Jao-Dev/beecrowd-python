import java.util.Scanner;

public class e1103 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int h1 = sc.nextInt();
        int m1 = sc.nextInt();
        int h2 = sc.nextInt();
        int m2 = sc.nextInt();

        while (!(h1==0 && h2==0 && m1==0 && m2==0)) {
            int hora1 = (h1*60)+m1;
            int hora2 = (h2*60)+m2;

            if(hora1<hora2){
                int horaTotal = (hora1-hora2)*(-1);
                System.out.println(horaTotal); 
            }
            else if(hora1>hora2){
                int horaTotal = (24*60)+hora2-hora1;
                System.out.println(horaTotal);
            }
            
            h1 = sc.nextInt();
            m1 = sc.nextInt();
            h2 = sc.nextInt();
            m2 = sc.nextInt();
        }

        sc.close();
    }
}
