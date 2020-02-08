func InterfaceAddrs() ([]Addr, error) //InterfaceAddrs返回该系统的网络接口的地址列表



### Dial()

func Dial(network, address string) (Conn, error)  //Dial 连接到指定address和name的网络，其中network包含如下几种："tcp", "tcp4" (IPv4-only), "tcp6" (IPv6-only),"udp", "udp4" (IPv4-only), "udp6" (IPv6-only), "ip", "ip4"(IPv4-only), "ip6" (IPv6-only), "unix", "unixgram" and"unixpacket". 对于TCP和UDP网络来说，addresses的形式如下host：port，其行使和JoinHostPort以及SplitHostPort函数中的addresses形式一致。





## Usage

```go
addr, _ := net.InterfaceAddrs()
	fmt.Println(addr)

	interfaces, _ := net.Interfaces()
	fmt.Println(interfaces)

	hp := net.JoinHostPort("127.0.0.1", "8080")
	fmt.Println(hp)

	lt, _ := net.LookupAddr("127.0.0.1")
	fmt.Println(lt)

	cname, _ := net.LookupCNAME("www.baidu.com")
	fmt.Println(cname)

	host, _ := net.LookupHost("www.baidu.com")
	fmt.Println(host)

	ip, _ := net.LookupIP("www.baidu.com")
	fmt.Println(ip)
```





