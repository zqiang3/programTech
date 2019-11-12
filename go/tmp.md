



## new kafka subsciber

```go
func RegKafkaSubscriber(moduleName string, groupID string, sub Subscriber) error {
	return NewKafkaSubscriber(moduleName, groupID, sub.Handler)

func NewKafkaSubscriber(moduleName string, groupID string, handler MessageHandler) error {
	t, err := getTopicConfig(moduleName)
	if err != nil {
		return err
	}

	var topics []string
	topics = append(topics, t.topic)
	return subscribe(moduleName, t.cluster, topics, groupID, handler)
}
```





## subscribe

```go

func subscribe(moduleName string, cluster string, topics []string, groupID string, handler MessageHandler) error {
	if len(cluster) == 0 {
		return fmt.Errorf("%s kafka cluster is empty", moduleName)
	}
	if len(topics) == 0 {
		return fmt.Errorf("%s kafka topic is empty", moduleName)
	}

	if isStart {
		logrus.Error("consuming is already started, can't subscribe new topic")
		return errors.New("consuming is already started, can't subscribe new topic")
	}
	onceInit.Do(func() { initTmq() })

	//一般只在程序初始化时调用，未用读写锁，忽略锁范围
	m.Lock()
	defer m.Unlock()
	_, ok := consumerMap[moduleName]
	if ok {
		//如果已存在，无需新建
		return fmt.Errorf("%s's consumer is existed", moduleName)
	}

	c := &consumer{
		mqType:  "kafka",
		module:  moduleName,
		group:   groupID,
		cluster: cluster,
		topics:  topics,
		handler: handler,
	}
	consumerMap[moduleName] = c

	for _, topic := range topics {
		if len(topic) == 0 {
			//跳过空值
			logrus.Errorf("%s's kafka consumer cluster %s config invalid", moduleName, cluster)
			continue
		}

		kafkaConfig := tmq.ConsumerConfig{
			MqType:        "kafka",
			Topic:         topic,
			Group:         groupID,
			MqCluster:     cluster,
			WorkerNumber:  1,
			Handler:       *c,
			PreferService: sarama.PreferServiceDCLeader, //默认读主
		}
		tmqConfig.AddConsumerConfig(&kafkaConfig)
	}

	return nil
}

```

