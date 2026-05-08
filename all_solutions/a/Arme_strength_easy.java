//https://open.kattis.com/problems/armystrengtheasy
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

class ArmyStrength {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int c = sc.nextInt();

        for (int i = 0; i < c; i++) {
            sc.nextLine();
            int g = sc.nextInt();
            int m = sc.nextInt();
            ArrayList<Integer> god = new ArrayList<Integer>();
            ArrayList<Integer> mec = new ArrayList<Integer>();

            for (int j = 0; j < g; j++) {
                god.add(sc.nextInt());
            }
            for (int j = 0; j < m; j++) {
                mec.add(sc.nextInt());
            }

            Collections.sort(god);
            Collections.sort(mec);

            while(!god.isEmpty()&&!mec.isEmpty()){
                if(god.get(0)<mec.get(0)){
                    god.remove(0);
                }else{
                    mec.remove(0);
                }
            }

            System.out.println(god.isEmpty() ? "MechaGodzilla" : "Godzilla");
        }

        sc.close();
    }
}