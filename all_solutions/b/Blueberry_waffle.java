//https://open.kattis.com/problems/blueberrywaffle
import java.util.Scanner;

class BlueberryWaffle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int f = sc.nextInt();
        int s = sc.nextInt();

        int d = (s%f);
        int c = (s-(d))/f;

        if(c%2==0){
            if(d>(f/2)){
                System.out.println("down");  
            }else{
                System.out.println("up");
            }
        }else{
            if(d>(f/2)){
                System.out.println("up");
            }else{
                System.out.println("down");  
            }
        }


        sc.close();
    }
}