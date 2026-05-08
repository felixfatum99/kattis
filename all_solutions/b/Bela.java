//https://open.kattis.com/problems/bela
import java.util.*;

public class Bela{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        int h = sc.nextInt();
        String t = sc.next();
        int point = 0;
        
        for(int i = 0; i<h*4; i++){
            String hx = sc.next();
            if(hx.charAt(0)=='A'){
                point += 11;
            }
            if(hx.charAt(0)=='K'){
                point += 4;
            }
            if(hx.charAt(0)=='Q'){
                point += 3;
            }
            if(hx.charAt(0)=='J'){
                 if(hx.charAt(1)==t.charAt(0)){
                    point += 20;
                }else{
                    point += 2;
                }
            }
            if(hx.charAt(0)=='T'){
                 point += 10;
            }
            if(hx.charAt(0)=='9'){
                 if(hx.charAt(1)==t.charAt(0)){
                    point += 14;
                }else{
                    point += 0;
                }
            }
            if(hx.charAt(0)=='8'){
                 point += 0;
            }
            if(hx.charAt(0)=='7'){
                 point += 0;
            }
        }
        System.out.println(point);
    }
}