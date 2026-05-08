//https://open.kattis.com/problems/autori
import java.util.Scanner;

public class Autori {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    String name = scan.nextLine();

    String init = name.substring(0,1);

    for(int i = 1; i<name.length(); i++){
      if(name.charAt(i)=='-'){
        init = init + name.substring(i+1,i+2);
      }
    }

    System.out.println(init);
  }
}