## 字符串函数

```c
char *strcpy(char *s1, const char * s2); // return s1
char *strncpy(char *s1, const char * s2, size_t n); // return s1
char *strcat(char *s1, const char *s2);  // return s1
char *strncat(char *s1, const char * s2, size_t n); // return s1
int strcmp(const char *s1, const char *s2);  // return int
int strncmp(const char *s1, const char *s2, size_t n);  // return int
char *strchr(const char *s, int c);  // return 找到的第一个位置的指针；未找到返回NULL
char *strrchr(const char *s, int c);  // return 从右查找，找到的第一个位置的指针；未找到返回NULL
char *strstr(const char * s1, const char *s2);  // return pointer
size_t strlen(const char *s);  // 不包括标志结束的空字符
```

