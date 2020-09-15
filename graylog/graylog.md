## Link

https://docs.graylog.org/en/3.2/pages/gelf.html



## GELF

Structured events from anywhere. Compressed and chunked.

The Graylog Extended Log Format(GELF) is a log format that avoids the shortcommings of classic plain syslog.

Syslog is okay for logging system messages of your machines or network gear. GELF is a great choice for logging from within applications. There are libraries and appenders for many programming languages and logging frameworks so it is easy to implement. You could use GELF to send every exception as a log message to your Graylog cluster. You don't have to care about timeouts, connection problems or anything that might break your application from within your logging class because GELF can be sent via UDP.



## GELF via UDP

chunking

UDP datagrams are limited to a size of 65536 bytes. Some Graylog components are limited to processing up to 8192 bytes. A lot of compressed information fits in there but you sometimes might just have more information to send. This is why Graylog supports chunked GELF.

You can define chunks of messages by prepending a byte  header to a GELF message including a message ID and sequence number to reassemble the message later.

Most GELF libraries support chunking transparently and will detect if a message is too big to be send in one datagram.