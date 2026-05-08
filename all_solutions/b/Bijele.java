//https://open.kattis.com/problems/bijele
import java.util.*;

class Bijele{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        int king = sc.nextInt();
        int queen = sc.nextInt();
        int rooks = sc.nextInt();
        int bishops = sc.nextInt();
        int knights = sc.nextInt();
        int pawns = sc.nextInt();
        
        int kingr = 1 - king;
        int queenr = 1 - queen;
        int rooksr = 2 - rooks;
        int bishopsr = 2 - bishops;
        int knightsr = 2 - knights;
        int pawnsr = 8 - pawns;
        
        System.out.println(kingr + " " + queenr + " " + rooksr + " " + bishopsr + " " + knightsr + " " + pawnsr);
    }
}