#include <stdio.h>
#include <conio.h>

#ifdef _WIN32
#define DLLEXPORT __declspec(dllexport)
#else
#define DLLEXPORT
#endif

DLLEXPORT int Wait() {
    char key = _getch();
    return (int)key;
}
