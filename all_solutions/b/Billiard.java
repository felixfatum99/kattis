//https://open.kattis.com/problems/billiard
import java.util.Scanner;

public class Kattis {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    double a, b, s, m, n;
    StringBuilder sb = new StringBuilder();
    while((a = sc.nextInt())!= 0) {
      b = sc.nextInt();
      s = sc.nextInt();
      m = sc.nextInt();
      n = sc.nextInt();
      double vertical = (b*n);
      double horizontal = (a*m);
      sb.append(String.format("%.2f %.2f%n", Math.toDegrees(Math.atan(vertical/horizontal)), Math.sqrt((vertical*vertical)+horizontal*horizontal)/s));
    }
    System.out.println(sb);
  }
}