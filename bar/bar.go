package main

import (
	"context"
	"log"
	"net"

	pb "bar.proy1/proto"

	"google.golang.org/grpc"
)

const (
	port = "127.0.0.1:4001"
)

type server struct {
	pb.UnimplementedBarServiceServer
}

func (s *server) BarFunc(ctx context.Context, in *pb.Request) (*pb.Response, error) {
	return &pb.Response{Result: "bar"}, nil
}

func main() {
	lis, err := net.Listen("tcp", port)
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}

	s := grpc.NewServer()
	pb.RegisterBarServiceServer(s, &server{})
	log.Printf("server listening at %v", lis.Addr())
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}

}
