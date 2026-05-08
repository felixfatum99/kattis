//https://open.kattis.com/problems/brokenswords
import java.util.*;

public class BrokenSwords
{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        
        int workingTopAndBottom = 0;
        int workingLeftAndRight = 0;
        
        int swords = 0;
        
        for (int i = 0; i < n; i++) {
            
            //Hele "linjen"
            String number = sc.next();
            
            String[] numbers = number.split("");
            
            for (int j = 0; j < 4; j++) {
                if (numbers[j].equals("0")) {
                    if(j < 2) {
                        workingTopAndBottom++;

                    } else {
                        workingLeftAndRight++;
                    }
                }
            }
            
            
        }
        
        if (workingTopAndBottom < workingLeftAndRight) {
            swords = workingTopAndBottom / 2;
        } else {
            swords = workingLeftAndRight / 2;
        }
        
        workingTopAndBottom -= swords * 2;
        workingLeftAndRight -= swords * 2;
        
        System.out.println(swords + " " + workingTopAndBottom + " " + workingLeftAndRight);
    }
}