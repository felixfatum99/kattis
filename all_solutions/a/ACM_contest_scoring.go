//https://open.kattis.com/problems/acm
package main

import (
    "fmt"
)

func main() {
    ACM_Contest_Scoring()
}

func ACM_Contest_Scoring() {
    problems := make(map[byte]int)
    count := 0
    min_count := 0
    for true {
        var min int
        var char byte
        var status string
        fmt.Scanf("%d %c %s\n", &min, &char, &status)
        if min == -1 {
            break
        }
        if status == "right" {
            if value, contains := problems[char]; contains {
                min_count += 20 * value
            }
            count++
            min_count += min
        } else {
            problems[char]++
        }
    }

    fmt.Printf("%d %d\n", count, min_count)
}