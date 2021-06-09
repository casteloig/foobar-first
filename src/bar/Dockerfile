FROM golang AS build

RUN mkdir /app
WORKDIR /app

COPY proto/ ./proto/
COPY bar.go .
COPY go.mod .
COPY go.sum .

EXPOSE 4001

RUN go install google.golang.org/protobuf/cmd/protoc-gen-go@v1.26
RUN go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@v1.1

#COPY --from=build /usr/local/go/bin/ .

ENTRYPOINT [ "go", "run" ]
CMD [ "bar.go" ]