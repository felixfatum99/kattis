//https://open.kattis.com/problems/basketballoneonone
import java.util.*;

public class Basketball{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        String a = sc.next();
        
        int A = 0; 
        int B = 0; 
        
        for(int i = 0; i < a.length(); i++){
            if(a.charAt(i)=='A'){
                if(a.charAt(i+1)=='1'){
                    A++;    
                } 
                if(a.charAt(i+1)=='2'){
                    A += 2;    
                }        
            }   
            if(a.charAt(i)=='B'){
                if(a.charAt(i+1)=='1'){
                    B++;    
                } 
                if(a.charAt(i+1)=='2'){
                    B += 2;         
                }    
            }   
        }
        
        if(A>B){
            System.out.println("A");    
        }else{
            System.out.println("B");
        }
    }        
}