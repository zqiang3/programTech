![kafka topic](/Users/spark/Downloads/log_anatomy.png)

每一个分区都是一个顺序的、不可变的消息队列， 并且可以持续的添加。分区中的消息都被分配了一个序列号，称之为偏移量(offset),在每个分区中此偏移量都是唯一的。
Kafka集群<b>保持所有的消息，直到它们过期</b>， 无论消息是否被消费了。
实际上消费者所持有的仅有的元数据就是这个偏移量，也就是消费者在这个log中的位置。 这个偏移量由消费者控制：正常情况当消费者消费消息的时候，偏移量也线性的的增加。但是实际偏移量由消费者控制，消费者可以将偏移量重置为更老的一个偏移量，重新读取消息。
可以看到这种设计对消费者来说操作自如， 一个消费者的操作不会影响其它消费者对此log的处理。
再说说分区。Kafka中采用分区的设计有几个目的。一是可以处理更多的消息，不受单台服务器的限制。Topic拥有多个分区意味着它可以不受限的处理更多的数据。第二，分区可以作为并行处理的单元，稍后会谈到这一点。

## 安装

```bash
brew install kafka
```

安装目录

```bash
# kafka安装目录
/usr/local/Cellar/kafka/2.1.0

# 配置文件目录
/usr/local/etc/kafka/
```

## 常用命令

```bash
kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic sunday

kafka-topics --list --zookeeper localhost:2181

kafka-topics --describe --zookeeper localhost:2181 --topic sunday

kafka-topics --delete --zookeeper localhost:2181 --topic suday
```





producer 和 consumer 只跟 leader 交互



## go操作kafka

连接kafka

```go
package main

import (
	"fmt"
	"github.com/Shopify/sarama"
)

// 基于sarama第三方库开发的kafka client

func main() {
	config := sarama.NewConfig()
	config.Producer.RequiredAcks = sarama.WaitForAll           // 发送完数据需要leader和follow都确认
	config.Producer.Partitioner = sarama.NewRandomPartitioner  // 新选出一个partition
	config.Producer.Return.Successes = true                    // 成功交付的消息将在success channel返回

  	// 构造一个消息
	msg := &sarama.ProducerMessage{}
	msg.Topic = "sunday"
	msg.Value = sarama.StringEncoder("hahah")

  	// 连接kafka
	client, err := sarama.NewSyncProducer([]string{"127.0.0.1:9092"}, config)
	if err != nil {
		fmt.Println("producer closed, err: ", err)
		return
	}

	defer client.Close()

  	// 发送消息
	pid, offset, err := client.SendMessage(msg)
	if err != nil {
		fmt.Println("send msg failed, err: ", err)
		return
	}

	fmt.Printf("pid: %v offset: %v\n", pid, offset)
}
```

