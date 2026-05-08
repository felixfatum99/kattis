//https://open.kattis.com/problems/armcoordination
import java.util.Scanner;

class ArmCoordination {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();
        int r = sc.nextInt();

        System.out.print(x-r);
        System.out.println(" "+(y+r));
        System.out.print(x+r);
        System.out.println(" "+(y+r));
        System.out.print(x+r);
        System.out.println(" "+(y-r));
        System.out.print(x-r);
        System.out.println(" "+(y-r));
        sc.close();
    }
}