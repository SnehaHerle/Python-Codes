#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main(int argc , char * argv[])
{
int i; 
int flag=0;
char arr[100];

strcpy(arr,argv[1]);
int x= strlen(arr);
for(i=0;i<x;i++)
        {
            printf("arr wale %c\n",arr[i]);
        }
for(i=0;i<x/2;i++)
{
if(arr[i]!=arr[x-i-1])
{
flag=1;
printf("Not a palindrome\n");
break;
}
}
if(flag==0)
{
printf("It is a palindrome\n");
}
return 0;
}
