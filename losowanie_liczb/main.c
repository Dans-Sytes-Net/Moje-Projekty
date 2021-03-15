#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    int a,x;
    char o;
    do{
    system("cls"); // czyœci konsole
    printf("Podaj liczbe od 1 do 10:");
    scanf(" %d",&a);
    time_t tt; // pobiera czas
    srand(time(&tt)); // ziarno na podstawie czasu
    x = (rand()%10)+1; // generuje liczbe od 1- 10 ---- bez +1 generuje od 0-9
    if(a==x) printf("Wygrales!\n");
    else printf("Przegrales\n");
    printf("Czy chcesz zagrac jeszcze raz?  T/N ");
    scanf("%s",&o);
    }while(o=='T'||o=='t');
    return 0;
}
