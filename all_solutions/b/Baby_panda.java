//https://open.kattis.com/problems/babypanda
import java.math.BigInteger;
import java.util.Scanner;

class BabyPanda {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        BigInteger n = sc.nextBigInteger();
        BigInteger m = sc.nextBigInteger();

        int output = 0; 

        while(m!= BigInteger.valueOf(0)){
            if(m.mod(BigInteger.valueOf(2))==BigInteger.valueOf(0)){
                m = m.divide(BigInteger.valueOf(2));
            }else{
                output++;
                m = (m.subtract(BigInteger.valueOf(1))).divide(BigInteger.valueOf(2));
            }
        }

        System.out.println(output);
        sc.close();
    }
}