//https://open.kattis.com/problems/brokencalculator
package main

import "fmt" 

func main(){
    var cases int; 
    fmt.Scan(&cases)

    var output []int = make([]int, cases) 
    var prev = 1; 
    for i := 0; i < cases; i++ {
        var a, b int; 
        var op string; 
        fmt.Scan(&a)
        fmt.Scan(&op)
        fmt.Scan(&b)

        if op == "+"{
            output[i] = (a+b)-prev; 
            prev = (a+b)-prev;
        }else if op == "-"{
            output[i] = (a-b)*prev; 
            prev = (a-b)* prev; 
        }else if op == "*"{
            output[i] = (a*b)*(a*b); 
            prev = (a*b)*(a*b); 
        }else if op == "/"{
            if(a%2)==0{
                output[i] = a/2 
                prev = a/2;
            }else{
                output[i] = (a+1)/2
                prev = (a+1)/2
            }
        }
    }
    for i := 0; i < cases; i++ {
        fmt.Println(output[i])
    }
}