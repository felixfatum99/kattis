//https://open.kattis.com/problems/anthonyanddiablo
import java.util.*;

public class Diablo{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double a = sc.nextDouble();
        double b = (sc.nextDouble()/4)*2;
        
        if(b > a){
            System.out.println("Diablo is happy!");
        }else{
            System.out.println("Need more materials!");
        }
    }
}