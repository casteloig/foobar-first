package main

import (
	"context"
	"log"
	"net"
	"os"

	pb "bar.proy1/proto"

	"google.golang.org/grpc"
)

type server struct {
	pb.UnimplementedBarServiceServer
}

func (s *server) BarFunc(ctx context.Context, in *pb.Request) (*pb.Response, error) {
	return &pb.Response{Result: "bar"}, nil
}

func main() {

	ip, err := os.LookupEnv("LIS_IP")
	if !err {
		ip = "0.0.0.0"
	}

	port, err := os.LookupEnv("LIS_PORT")
	if !err {
		port = "4001"
	}

	log.Printf("server listening at %v %v", ip, port)
	lis, error := net.Listen("tcp", ip+":"+port)
	if error != nil {
		log.Fatalf("failed to listen: %v", err)
	}

	s := grpc.NewServer()
	pb.RegisterBarServiceServer(s, &server{})
	log.Printf("server listening at %v", lis.Addr())
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
