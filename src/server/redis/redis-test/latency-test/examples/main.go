package main

import (
	"fmt"
	"time"
	"os"
	"strconv"

	"github.com/tylertreat/bench"
	"github.com/tylertreat/bench/requester"
)

func main() {
	r := &requester.RedisPubSubRequesterFactory{
		URL:         "10.10.0.14:6379",
		PayloadSize: 1843200,
		Channel:     "benchmark",
	}

	var sub_num int64
	var subs_num uint64
	sub_num, err := strconv.ParseInt(os.Args[1], 10, 64)
	subs_num = uint64(sub_num)
	fmt.Println(subs_num)

	benchmark := bench.NewBenchmark(r, 10000, subs_num, 30*time.Second, 0)
	summary, err := benchmark.Run()
	if err != nil {
		panic(err)
	}

	fmt.Println(summary)
	summary.GenerateLatencyDistribution(nil, "redis.txt")
}
