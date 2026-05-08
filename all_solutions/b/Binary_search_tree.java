//https://open.kattis.com/problems/bst
import java.io.*;
import java.util.*;

class BST {
  public static void main(String[] args) throws IOException{
  BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

  TreeMap<Integer, Integer> depths = new TreeMap<>();
  
  
  
        Integer floor, ceil, depth;
        long totalDepth = 0; //running total 

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            Integer newNode = Integer.parseInt(br.readLine());
            
            floor = depths.floorKey(newNode); 
            ceil = depths.ceilingKey(newNode); 

            if (floor == null) {
                if (ceil == null) 
                    depth = 0;
                
                else 
                    depth = depths.get(ceil) + 1;
            } 
            
            else if (ceil == null)
                depth = depths.get(floor) + 1; 
            else 
                depth = Math.max(depths.get(floor), depths.get(ceil)) + 1;
            
            depths.put(newNode, depth);
            totalDepth += depth;
            System.out.println(totalDepth);
        }
  }
}