```python
import cProfile
# run（command, filename=None, sort=-1

prof = Profile()
prof.enable()
prof.create_stats()
prof.print_stats()           # 打印到标准输出
prof.dump_stats("prof.out")  # 保存到文件，二进制格式
```

输出信息解释

ncalls：表示函数调用的次数；
tottime：表示指定函数的总的运行时间，除掉函数中调用子函数的运行时间；
percall：（第一个percall）等于 tottime/ncalls；
cumtime：表示**该函数及其所有子函数的调用**运行的时间，即函数开始调用到返回的时间；
percall：（第二个percall）即函数运行一次的平均时间，等于 cumtime/ncalls；
filename:lineno(function)：每个函数调用的具体信息；