#include <stdio.h>
#include <unistd.h>

int main() {
    // 1. 必须初始化 i = 0
    for (int i = 0; i < 4; i++) {
        fork();
        // 打印当前进程 ID，可以看到进程是如何增加的
        printf("My PID: %d\n", getpid()); 
    }

    printf("hello\n");
    return 0;
}
