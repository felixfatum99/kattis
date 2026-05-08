//https://open.kattis.com/problems/avion
import java.util.*;
public class FBI{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        String o = sc.next();
        String t = sc.next();
        String tr = sc.next();
        String f = sc.next();
        String fi = sc.next();
        int sum = 0;
        int sum1 = 0; 
        int sum2 = 0;
        int sum3 = 0;
        int sum4 = 0; 

        int a = o.length();
        int l = t.length();
        int m = tr.length();
        int n = f.length();
        int w = fi.length();

        for(int d=0;d<a;d++){
            if(o.charAt(d)=='F'){
                if(o.charAt(d+1)=='B'){
                    if(o.charAt(d+2)=='I'){
                        sum = sum + 1;  
                    }  
                }
            }else{
                sum = sum + 0;
            }
        }
        int b = t.length();
        for(int e=0;e<l;e++){
            if(t.charAt(e)=='F'){
                if(t.charAt(e+1)=='B'){
                    if(t.charAt(e+2)=='I'){
                        sum1 = sum1 + 1;  
                    }  
                }
            }else{
                sum1 = sum1 + 0;
            }
        }
        int c = tr.length();
        for(int x=0;x<m;x++){
            if(tr.charAt(x)=='F'){
                if(tr.charAt(x+1)=='B'){
                    if(tr.charAt(x+2)=='I'){
                        sum2 = sum2 + 1;  
                    }  
                }
            }else{
                sum2 = sum2 + 0;
            }
        }
        int d = f.length();
        for(int g=0;g<n;g++){
            if(f.charAt(g)=='F'){
                if(f.charAt(g+1)=='B'){
                    if(f.charAt(g+2)=='I'){
                        sum3 = sum3 + 1;  
                    }  
                }
            }else{
                sum3 = sum3 + 0;
            }
        }
        int e = fi.length();
        for(int h=0;h<w;h++){
            if(fi.charAt(h)=='F'){
                if(fi.charAt(h+1)=='B'){
                    if(fi.charAt(h+2)=='I'){
                        sum4 = sum4 + 1;  
                    }  
                }
            }else{
                sum4 = sum4 + 0;
            }
        }
        if(sum==0&&sum1==0&&sum2==0&&sum3==0&&sum4==0){
            System.out.println("HE GOT AWAY!");
        }
        if(sum>0){
            System.out.print(1+" ");
        }
        if(sum1>0){
            System.out.print(2+" ");
        }
        if(sum2>0){
            System.out.print(3+" ");
        }
        if(sum3>0){
            System.out.print(4+" ");
        }
        if(sum4>0){
            System.out.print(5);
        }
    }
}