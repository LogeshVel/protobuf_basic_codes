package main

import (
	"fmt"

	"github.com/LogeshVel/goproto/pb"
)

func main() {
	p := &pb.PBMessage{
		YourMsg:  "My message",
		YourName: "Logesh",
	}
	fmt.Println(p)
}
