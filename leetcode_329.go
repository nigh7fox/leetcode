package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(isSubsequence("aaaaaa", "bbaaaa"))
}

func isSubsequence(s string, t string) bool {
	var ans int = 0
	var lastIdx int = 0
	if s == "" {
		return true
	}
	for i, _ := range t {
		if i < len(s) {
			var currIdx int = strings.Index(t, string(s[i]))
			if currIdx >= 0 && lastIdx <= currIdx {
				fmt.Printf("Found %s\n", string(s[i]))
				lastIdx = currIdx
				ans++
			}
		}
	}
	return ans == len(s)
}
