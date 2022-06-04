package main

import (
	"fmt"

	tspb "google.golang.org/protobuf/types/known/timestamppb"
)

func main() {
	fmt.Println(tspb.Now())
}
