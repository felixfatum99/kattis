//https://open.kattis.com/problems/babybites
import java.util.*;

public class BabyBites{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
         
        int counter = 0; 
        
        boolean makessense = true; 
        
        for(int i = 0; i < n; i++){
            String a = sc.next();
            if(a.length()>4){
                counter++;                
            }else{
                int number = Integer.parseInt(a);
                counter++;
                if(counter!=number){
                    makessense = false;    
                }
            }
        }
        
        if(makessense==true){
            System.out.println("makes sense");    
        }else{
            System.out.println("something is fishy");
        }
    }        
}