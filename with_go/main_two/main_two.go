package main

import (
	"fmt"
	pb "simple/pb"
)

func main() {
	s := &pb.SimpleMessageTwo{
		Id:     2,
		Msg:    "Simple msg",
		Sender: "Logesh",
	}
	fmt.Println(s)
}
