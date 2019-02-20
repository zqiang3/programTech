| 家族名  | 目的       | 可用于所有流 | 只用于stdin stdout | 内存中的字符串 |
| ------- | ---------- | ------------ | ------------------ | -------------- |
| getchar | 字符输入   | fgetc, getc  | getchar            |                |
| putchar | 字符输出   | fputc, putc  | putchar            |                |
| gets    | 文本行输入 | fgets        | gets               |                |
| puts    | 文本行输出 | fputs        | puts               |                |
| scanf   | 格式化输入 | fscanf       | scanf              | sscanf         |
| printf  | 格式化输出 | fprintf      | printf             | sprintf        |

```c
#include <stdio.h>
FILE *fopen(const char *restrict pathname, const char *restrict type);

int getc(FILE *fp);  // 可用宏实现
int fgetc(FILE *fp);
int getchar(FILE *fp);  // All three return: next character if OK, EOF on end of file or error

int putc(int c, FILE *fp);  // 可用宏实现
int fputc(int c, FILE *fp);
int putchar(int c);  // All three return: c if OK, EOF on error

int ungetc(int c, FILE *fp);  // Returns: c if OK, EOF on error

char *fgets(char *restricted buf, int n, FILE *restrict fp);
char *gets(char *buf);  // dangerous
// Both return: buf if OK, NULL on end of file or error

int fputs(const char *restrict str, FILE *restrect fp);
int puts(const char *str);
// Both return: non-negative value if OK, EOF on error

size_t fread(void *restrict ptr, size_t size, size_t nobj, FILE *restrict fp);
size_t fwrite(const void *restrict ptr, size_t size, size_t nobj, FILE *restrict fp);
// Both return number of objects read or written

long ftell(FILE *fp);  // Return current file position if OK, -1L on error
int fseek(FILE *fp, long offset, int whence);  // Return 0 if OK, nonzero on error
void rewind(FILE *fp);

char *tmpnam(char *ptr);  // Returns: pointer to unique pathname
FILE *tmpfile(void);  // Returns: file pointer if OK, NULL on error

char *tempnam(const char *derectory, const char *prefix);  // Returns: pointer to unique pathname
int mkstemp(char *template);  // Returns: file descriptor if OK, -1 on error
```



## getc()

http://www.runoob.com/cprogramming/c-function-getc.html

```c
int getc(FILE *stream);

#include <stdio.h>

int main(void)
{
    int ch;
    int count = 0;

    puts("input text");

    while( (ch = getc(stdin)) != EOF)
    {
        putc(ch, stdout);
        count++;
    }
    printf("count = %d\n", count);

    return 0;
}

```

## fgetc()

```c
int fgetc(FILE *stream);
```

返回值：该函数以无符号 char 强制转换为 int 的形式返回读取的字符，如果到达文件末尾或发生读错误，则返回 EOF。 

## putc()

```c
int putc(int c, FILE *stream);
```

该函数以无符号 char 强制转换为 int 的形式返回写入的字符，如果发生错误则返回 EOF 

## fread()

```c
size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream);
```



## gets()

http://www.runoob.com/cprogramming/c-function-gets.html

```c
char *gets(char *str);
```



返回值：如果成功，该函数返回 str。如果发生错误或者到达文件末尾时还未读取任何字符，则返回 NULL .

由于gets()并不检查str缓冲区的大小，在未遇到换行符或文件结尾不断地从流中读取字符，会造成**缓冲区溢出**，因此并不推荐使用，可使用fgets()代替。

## fgets()

```c
char *fgets(char *str, int n, FILE *stream);
```



## fputs()

http://www.runoob.com/cprogramming/c-function-fputs.html

```c
int fputs(const char *str, FILE *stream);
```

返回值：该函数返回一个非负值，如果发生错误则返回 EOF 

## fprintf()

http://www.runoob.com/cprogramming/c-function-fprintf.html

```c
int fprintf(FILE *stream, const char *format, ...);
```

返回值：如果成功，则返回写入的字符总数，否则返回一个负数。 

## fwrite()

```c
size_t fwrite(const void *ptr, size_t size, size_t nmemb, FILE *stream);
```



## fclose()

```c
int fclose(FILE *stream);
```

返回值：如果流成功关闭，则该方法返回零。如果失败，则返回 EOF。 