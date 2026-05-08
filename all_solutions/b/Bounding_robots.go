//https://open.kattis.com/problems/boundingrobots
package main

import "fmt" 

func main(){
    for{
    var w, l, c, r, cx, cy, rx, ry int; 
    var d string;
    fmt.Scan(&w)
    fmt.Scan(&l)
    if(w==0&&l==0){
        return;
    }
    fmt.Scan(&c)
    cx = 0; 
    cy = 0; 
    rx = 0; 
    ry = 0; 
    for i := 0; i < c; i++ {
        fmt.Scan(&d)
        fmt.Scan(&r)    
        if d == "u"{
            rx += r;
            if (cx + r) > l-1{
                cx = l-1;
            }else{
                cx += r;
            }
        }else if d == "d"{
            rx -= r;
            if (cx - r) < 0{
                cx = 0;
            }else{
                cx -= r;
            }
        }else if d == "l" {
            ry -= r;
            if (cy - r) < 0{
                cy = 0;
            }else{
                cy -= r;
            }
        }else if d == "r"{
            ry += r;
            if (cy + r) > w-1{
                cy = w-1;
            }else{
                cy += r;
            }
        }
    }
    fmt.Println("Robot thinks", ry, rx)
    fmt.Println("Actually at", cy, cx)
    }
}