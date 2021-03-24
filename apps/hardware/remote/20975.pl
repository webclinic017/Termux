source: https://www.securityfocus.com/bid/2802/info

Olicom routers were previously manufactured and distributed by Olicom, a company now owned by Intel. Olicom routers provide a low-cost routing solution for small businesses.

A problem with Olicom routers could allow unauthorized access to certain configuration variables within the device. The ILMI SNMP Community string allows read and write access to certain configuration parameters such as the organization to which the routers belongs. These parameters do not affect normal operation, but could be used further in a social engineering attack.

This problem makes it possible for a remote user to launch a social engineering attack, potentially gaining unauthorized access to the device. 

snmpwalk router ILMI |more