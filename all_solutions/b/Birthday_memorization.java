//https://open.kattis.com/problems/fodelsedagsmemorisering
import java.util.*;

public class Birthday {
    String name;
    int value;

    public Birthday(String name, int value){
        this.name = name;
        this.value = value;
    }

    public String getName(){
        return name;
    }

    public int getValue(){
        return value;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int cases = sc.nextInt();

        HashMap<String, Birthday> birthdays = new HashMap<>();
        String x = sc.nextLine();

        for(int i = 0; i < cases; i++){
            String line = sc.nextLine();
            String[] lineSplitted = line.split(" ");
            String name = lineSplitted[0];
            String date = lineSplitted[2];
            int value = Integer.parseInt(lineSplitted[1]);

            Birthday temp = new Birthday(name, value);

            if(birthdays.containsKey(date)){
                int valueOne = birthdays.get(date).getValue();
                int valueTwo = temp.getValue();
                if(valueOne<valueTwo){
                    birthdays.remove(date);
                    birthdays.put(date, temp);
                }
            }else{
                birthdays.put(date, temp);
            }
        }


        System.out.println(birthdays.size());
        ArrayList<String> names = new ArrayList<>();

        for(Map.Entry<String, Birthday> entry : birthdays.entrySet()) {
            names.add(entry.getValue().getName());
        }

        Collections.sort(names);

        for(int i = 0; i < birthdays.size(); i++){
            System.out.println(names.get(i));
        }
    }
}