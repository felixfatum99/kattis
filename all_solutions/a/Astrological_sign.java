//https://open.kattis.com/problems/astrologicalsign
import java.util.*;

public class AstrologicalSign{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int x = sc.nextInt();
        
        for(int i = 0; i < x; i++){
            int a = sc.nextInt();
            String b = sc.next();
            if(b.equals("Apr")){
                if(a<=20){
                    System.out.println("Aries");
                }else{
                    System.out.println("Taurus");    
                }   
            }
            if(b.equals("May")){
                if(a<=20){
                    System.out.println("Taurus");
                }else{
                    System.out.println("Gemini");    
                }   
            }
            if(b.equals("Jun")){
                if(a<=21){
                    System.out.println("Gemini");
                }else{
                    System.out.println("Cancer");    
                }   
            }
            if(b.equals("Jul")){
                if(a<=22){
                    System.out.println("Cancer");
                }else{
                    System.out.println("Leo");    
                }   
            }
            if(b.equals("Aug")){
                if(a<=22){
                    System.out.println("Leo");
                }else{
                    System.out.println("Virgo");    
                }   
            }
            if(b.equals("Sep")){
                if(a<=21){
                    System.out.println("Virgo");
                }else{
                    System.out.println("Libra");    
                }   
            }
            if(b.equals("Oct")){
                if(a<=22){
                    System.out.println("Libra");
                }else{
                    System.out.println("Scorpio");    
                }   
            }
            if(b.equals("Nov")){
                if(a<=22){
                    System.out.println("Scorpio");
                }else{
                    System.out.println("Sagittarius");    
                }   
            }
            if(b.equals("Dec")){
                if(a<=21){
                    System.out.println("Sagittarius");
                }else{
                    System.out.println("Capricorn");    
                }   
            }
            if(b.equals("Jan")){
                if(a<=20){
                    System.out.println("Capricorn");
                }else{
                    System.out.println("Aquarius");    
                }   
            }
            if(b.equals("Feb")){
                if(a<=19){
                    System.out.println("Aquarius");
                }else{
                    System.out.println("Pisces");    
                }   
            }
            if(b.equals("Mar")){
                if(a<=20){
                    System.out.println("Pisces");
                }else{
                    System.out.println("Aries");    
                }   
            }
        }
    }        
}