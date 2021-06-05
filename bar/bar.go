package main

import (
	"context"
	"log"
	"net"
	"os"

	pb "bar.proy1/proto"
	"google.golang.org/grpc"

	"github.com/sirupsen/logrus"
)

var listeningLog = logrus.New()
var templateLogger *logrus.Entry

func createTemplateLogger(ip string, port string) {
	templateLogger = listeningLog.WithFields(logrus.Fields{
		"ip":   ip,
		"port": port,
	})
}

func setupStructLogging() {

	var filename string = "logs_bar.log"
	f, err := os.OpenFile(filename, os.O_WRONLY|os.O_APPEND|os.O_CREATE, 0644)

	if err != nil {
		log.Println(err)
	} else {
		listeningLog.Out = f
	}
	listeningLog.Formatter = &logrus.JSONFormatter{}
	listeningLog.Level = logrus.TraceLevel

}

type server struct {
	pb.UnimplementedBarServiceServer
}

func (s *server) BarFunc(ctx context.Context, in *pb.Request) (*pb.Response, error) {
	return &pb.Response{Result: "bar"}, nil
}

func main() {

	setupStructLogging()

	ip, err := os.LookupEnv("LIS_IP")
	if !err {
		ip = "0.0.0.0"
	}

	port, err := os.LookupEnv("LIS_PORT")
	if !err {
		port = "4001"
	}
	createTemplateLogger(ip, port)

	templateLogger.Info("Server listening")
	lis, error := net.Listen("tcp", ip+":"+port)
	if error != nil {
		templateLogger.Fatal("Failed to listen")
	}

	s := grpc.NewServer()
	pb.RegisterBarServiceServer(s, &server{})

	templateLogger.Info("Serving at ")
	if err := s.Serve(lis); err != nil {
		templateLogger.Fatal("failed to serve")
	}

}
