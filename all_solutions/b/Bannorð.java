//https://open.kattis.com/problems/bannord
import java.util.Scanner;

class Bannord {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        String e = sc.nextLine();
        String[] letters = e.split("", e.length());
        String[] line = sc.nextLine().split(" ", -1);

        for (int i = 0; i < line.length; i++) {
            int checker = 0; 
            for (int j = 0; j < letters.length; j++) {
                if(line[i].contains(letters[j])){
                    checker++;
                }
            }
            if(checker==0){
                System.out.print(line[i]);
                System.out.print(" ");
            }else{
                for (int k = 0; k < line[i].length(); k++) {
                    System.out.print("*");
                }
                System.out.print(" ");
            }
        }
        
        sc.close();
    }
}