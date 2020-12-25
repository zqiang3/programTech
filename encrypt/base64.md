## base64加密算法

Base64编码的思想是采用64个基本的ASCII码字符对数据进行重新编码。他将需要编码的数据拆分成字节数组，以三个字节为一组。按顺序排列24位数据，再把这24位数据分成四组，即每组6位。再在每组的最高位前补两个0凑足一个字节。这样就把一个3字节为一组的数据重新编码成了4个字节。当所要编码的数据的字节数不是3的整数倍，也就是说在分组时最后一组不足3个字节。这时在最后一组填充1到2个0字节。并在最后编码完成后在结尾添加1到2个‘=’。

例如：将RON进行Base64编码：

1. 首先取RON对应的ASCII码值：R(82)O(79)N(78)；
2. 再取二进制值：R(01010010)O(01001111)N(01001110)；
3. 然后把这三个字节的二进制码接起来（010100100100111101001110）；
4. 再以6位为单位分成4个数据块,并在最高位填充两个0后形成4个字节的编码后的值，(00010100)(00100100)(00111101)(00001110)；
5. 再把这四个字节转换为10进制数据得到：(20)(36)(61)(14)，这里算出来的值实际上是数据在字符表中的索引。
6. 最后根据BASE64给出的64个基本字符表，查出对应的ASCII码字符：(U)(k)(9)(O)。

注：BASE64字符表：ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=



## golang实现

```go
package main

import "fmt"

const (
	base64string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
)

func Base64(s string) string {
	if len(s) % 3 != 0 {
		return ""
	}
	times := len(s) / 3 * 4
	bs := []byte(s)

	con := make([]byte, 0)
	for _, b := range bs {
		con = append(con, char2binary(b)...)
	}

	var r []byte
	var rs uint8
	var rstring string
	for i := 0; i < times; i++ {
		r = doEncrypt(con[6*i : 6*(i+1)])
		rs = binary2char(r)
		rstring += string(rs)
	}
	return rstring
}


func char2binary(b byte) []byte {
	output := make([]byte, 0)
	for count := 0; count < 8; count++ {
		output = append(output, b % 2)
		b >>= 1
	}
	rOutput := make([]byte, 0)
	for i := 7; i >= 0; i-- {
		rOutput = append(rOutput, output[i])
	}
	return rOutput
}

func binary2char(bs []byte) uint8 {
	var sum byte
	for _, b := range bs {
		sum = sum * 2 + b
	}
	return base64string[sum]
}

func doEncrypt(input []byte) []byte {
	output := make([]byte, 0)
	output = append(output, 0)
	output = append(output, 0)
	for _, b := range input {
		output = append(output, b)
	}
	return output
}

func main() {
	r := Base64("thisisgoooddayHHASDFSDFSD223322QQ!=/SFS")
	fmt.Println(r)
}

```

