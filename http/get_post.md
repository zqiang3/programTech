## link

https://www.zhihu.com/question/28586791



## 区别

* get没有副作用，是幂等的，post可能有副作用
* 携带数据的格式有区别，协议本身没有限制，但浏览器的实现有这种限制。elastic search就用了带body的GET,也可以把参数放在HEADER里
* GET携带的数据可以在url中看到，有更多机会被泄漏，但POST也不安全，因为http是明文传输的，避免泄密的最可靠手段就是https