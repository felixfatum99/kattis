//https://open.kattis.com/problems/baconeggsandspam
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Scanner;

public class BaconEggSpam {
    ArrayList<String> persons;

    public BaconEggSpam(){
        persons = new ArrayList<>();
    }

    public void addPerson(String person){
        persons.add(person);
    }

    public ArrayList getPersons(){return persons;}

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int y = 1;

        while(y!=0){

            int x = sc.nextInt();
            y = x;
            if(y==0) break;
            HashMap<String, BaconEggSpam> map = new HashMap<>();

            for(int i = 0; i < x; i++){
                if(i==0){String garbage = sc.nextLine();}
                String line = sc.nextLine();
                String[] words = line.split(" ");

                for(int j = 1; j < words.length; j++){
                    if(map.containsKey(words[j])){
                        BaconEggSpam add = map.get(words[j]);
                        add.addPerson(words[0]);
                    }else{
                        BaconEggSpam add = new BaconEggSpam();
                        add.addPerson(words[0]);
                        map.put(words[j], add);
                    }
                }
            }

            ArrayList<String> sorted = new ArrayList<>();
            for(String key: map.keySet()) {
                sorted.add(key);
            }
            Collections.sort(sorted);

            for(int i = 0; i < sorted.size(); i++){
                ArrayList<String> temp = map.get(sorted.get(i)).getPersons();
                Collections.sort(temp);
                System.out.print(sorted.get(i)+" ");
                for(int j = 0; j < temp.size(); j++){
                    System.out.print(temp.get(j)+" ");
                }
                System.out.println();
            }

            System.out.println();
        }

    }
}