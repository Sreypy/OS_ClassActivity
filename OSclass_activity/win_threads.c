#include <windows.h>
#include <stdio.h>

DWORD WINAPI ThreadFunc(LPVOID lpParam) {
    int id = *((int*)lpParam);
    printf("Hello from thread %d\n", id);
    return 0;
}

int main() {
    HANDLE threads[10];
    int ids[10];

    for (int i = 0; i < 10; i++) {
        ids[i] = i;
        threads[i] = CreateThread(NULL, 0, ThreadFunc, &ids[i], 0, NULL);
    }

    WaitForMultipleObjects(10, threads, TRUE, INFINITE);

    printf("All threads finished!\n");
    return 0;
}