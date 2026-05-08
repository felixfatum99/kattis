//https://open.kattis.com/problems/boatparts
import java.util.*;

public class BoatParts{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        int b = sc.nextInt();
        int d = sc.nextInt();
        
        HashSet<String> boatParts = new HashSet<String>();
        int sum = 0;
        
        for(int i = 1; i <= d; i++){
            String a = sc.next();
            boatParts.add(a);
            if(boatParts.size()==b&&sum==0){
                System.out.println(i);
                sum++;
            }
        }
        
        if(sum==0){
            System.out.println("paradox avoided");
        }
    }        
}