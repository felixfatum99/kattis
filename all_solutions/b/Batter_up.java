//https://open.kattis.com/problems/batterup
import java.util.*;

public class Base{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        double a = sc.nextInt();
        double n = 0;
        double t = a;
        
        for(int i=0; i<a; i++){
            double b = sc.nextInt();
            if(b<0){
                t = t - 1;
            }else if(b>=0){
                n = n + b;
            }
            
        }
        
        System.out.println(n/t);
    }
}