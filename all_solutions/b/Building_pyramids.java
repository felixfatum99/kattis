//https://open.kattis.com/problems/pyramids
import java.util.*;

class Pyramids{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        long input = sc.nextInt();
        long lag = 0;
        long b1 = 1;
        long b2 = 1;
        long y = 2;

        while(b1<=input){
            b2 = b2+y;
            b1 += b2*b2;
            lag++;
        }

        System.out.println(lag);
    }
}