#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct cpuinfo {

char name[50];
int count1;
int count2;
int count3;
int count4;
int count5;
int count6;
int count7;
int count8;
int count9;
} cpu;


int main(void)
{


FILE *rfp;
char *filename = "/proc/stat";
cpu s_cpu;

if *1 == NULL ){

fprintf(stderr,"Cannot open file");
}

fscanf(rfp,"%s %d %d %d %d %d %d %d %d %d",s_cpu.name,&s_cpu.count1,&s_cpu.count2,&s_cpu.count3,&s_cpu.count4,&s_cpu.count5,&s_cpu.count6,&s_cpu.count7,&s_cpu.count8,&s_cpu.count9);


printf("%s %d %d %d %d %d %d %d %d %d\n",s_cpu.name,s_cpu.count1,s_cpu.count2,s_cpu.count3,s_cpu.count4,s_cpu.count5,s_cpu.count6,s_cpu.count7,s_cpu.count8,s_cpu.count9);

}
