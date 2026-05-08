//https://open.kattis.com/problems/betting
import java.util.Scanner;

public class Betting {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double x = sc.nextInt();
        System.out.println(100/x);
        System.out.println(100/(100-x));
    }
}