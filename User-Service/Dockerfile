FROM golang:latest

WORKDIR /usr/src/app

COPY . .

RUN go build -o main .

EXPOSE 3002

CMD ["./main"]
