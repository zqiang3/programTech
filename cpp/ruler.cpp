#include <iostream>
#include <cstdio>
using namespace std;

const int Len = 66;

void curv(char arr[], int low, int high, int level)
{
    if (level == 0)
        return;

    if (low >= high)
        return;

    int mid = low + (high - low) / 2;
    arr[mid] = '|';
    curv(arr, low, mid, level - 1);
    curv(arr, mid, high, level - 1);
    
}


void print_addr(char *ruler)
{
    printf("addr = 0x%x\n", ruler);
}

void clear_ruler(char ruler[])
{
    int i;
    for (i = 1; i < Len -2; i++)
        ruler[i] = ' ';
}

int main()
{
    char ruler[Len];
    print_addr(ruler);
    clear_ruler(ruler);
    ruler[Len - 1] = '\0';

    int min, max;
    min = 0;
    max = Len - 2;
    ruler[min] = ruler[max] = '|';

    cout << ruler << endl;
    int level = 6;
    int i;
    for (i = 1; i <= level; i++)
    {
        curv(ruler, min, max, i);
        cout << ruler << endl;
        clear_ruler(ruler);
    }

    return 0;
}
