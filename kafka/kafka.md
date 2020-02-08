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



## 启动

kafka依赖zookeeper，因此需要首先启动zookeeper。

Apache Kafka depends on Zookeeper for cluster management. Hence, prior to starting Kafka, Zookeeper has to be started. There is no need to explicitly install Zookeeper, as it  comes included with Apache Kafka.

```bash
bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties
```



## 常用命令

```bash
kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic sunday

kafka-topics --list --zookeeper localhost:2181

kafka-topics --describe --zookeeper localhost:2181 --topic sunday

kafka-topics --delete --zookeeper localhost:2181 --topic suday
```





producer 和 consumer 只跟 leader 交互



## 基础概念

在深入了解kafka之前，必须深入了解主题，经纪人，生产者和消费者等主要术语。

### 主题

属于特定类别的消息流称为主题。数据存储在主题中，主题被拆分成分区。对于每个主题，kafka保存一个分区的数据。

### partition

kafka分区是消息的线性有序序列，每个消息由它们的索引（偏移）来标识。kafka集群中的所有数据都是不相连的分区联合。传入消息写在分区的末尾，消息由消费者顺序读取。

### Replicas of partition

副本只是一个分区的备份，副本从不读取或写入数据。它们用于防止数据丢失。





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

