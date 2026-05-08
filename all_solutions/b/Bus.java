//https://open.kattis.com/problems/bus
import java.util.*;

public class Bus{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();

        int sum = 1;

        for(int i = 0; i < a; i++){
            int x = sc.nextInt();
            for(int y = 0; y < x-1; y++){
                sum = (sum * 2)+1;
            }
            System.out.println(sum);
            sum = 1;
        }
    }        
}