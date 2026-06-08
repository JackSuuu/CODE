#include <unistd.h>
#include <sys/mman.h>
#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <err.h>

#define CACHE_LINE_SIZE  64
#define NLOOP            (4*1024UL*1024*1024)
#define NSECS_PER_SEC    1000000000UL

static inline long diff_nsec(struct timespec before, struct timespec after) {
    return ((after.tv_sec * NSECS_PER_SEC + after.tv_nsec) - 
            (before.tv_sec * NSECS_PER_SEC + before.tv_nsec));
}

int main(int argc, char *argv[]) {
    char *progname = argv[0];

    if (argc != 2) {
        fprintf(stderr, "usage: %s <size[KB]>\n", progname);
        exit(EXIT_FAILURE);
    }

    register int size = atoi(argv[1]) * 1024;
    if (size <= 0) {
        fprintf(stderr, "size should be >= 1 KB\n");
        exit(EXIT_FAILURE);
    }

    // Allocate memory anonymously
    char *buffer = mmap(NULL, size, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    if (buffer == MAP_FAILED) {
        err(EXIT_FAILURE, "mmap() failed");
    }

    struct timespec before, after;
    clock_gettime(CLOCK_MONOTONIC, &before);

    // Access memory in strides equal to the cache line size
    for (int i = 0; i < NLOOP / (size / CACHE_LINE_SIZE); i++) {
        for (long j = 0; j < size; j += CACHE_LINE_SIZE) {
            buffer[j] = 0;
        }
    }

    clock_gettime(CLOCK_MONOTONIC, &after);
    
    // Print the average time (in nanoseconds) per memory access
    printf("%f\n", (double)diff_nsec(before, after) / NLOOP);

    if (munmap(buffer, size) == -1) {
        err(EXIT_FAILURE, "munmap() failed");
    }

    exit(EXIT_SUCCESS);
}
