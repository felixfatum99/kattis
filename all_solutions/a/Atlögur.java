//https://open.kattis.com/problems/atlogur
import java.util.Scanner;

class Atlogur {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int chi = 0; 
        int csi = 0; 
        int ci = 0; 

        for (int i = 0; i < n; i++) {
            int hi = sc.nextInt();
            int si = sc.nextInt();

            if(i == 0){
                chi = hi;
                csi = si;
            }else{

            while(chi > 0 && hi > 0){
                hi -= csi;
                if(hi>0){
                    chi -= si;
                }
            }

            if(chi<=0){
                chi = hi;
                csi = si;
                ci = i;
            }
            }
        }

        System.out.println(ci+1);
        sc.close();
    }
}