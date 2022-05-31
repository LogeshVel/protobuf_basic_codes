package main

import (
	"fmt"

	goPB "myproto/pb"
)

func main() {
	a := &goPB.SimpleMessage{
		Id:  1,
		Msg: "My Message",
	}
	fmt.Println(a)
}
