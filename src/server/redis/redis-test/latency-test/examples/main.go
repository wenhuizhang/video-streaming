package main

import (
	"fmt"
	"time"

	"github.com/tylertreat/bench"
	"github.com/tylertreat/bench/requester"
)

func main() {
	r := &requester.RedisPubSubRequesterFactory{
		URL:         "10.10.0.14:6379",
		PayloadSize: 117000,
		Channel:     "benchmark",
	}

	benchmark := bench.NewBenchmark(r, 10000, 128, 30*time.Second, 0)
	summary, err := benchmark.Run()
	if err != nil {
		panic(err)
	}

	fmt.Println(summary)
	summary.GenerateLatencyDistribution(nil, "redis.txt")
}
