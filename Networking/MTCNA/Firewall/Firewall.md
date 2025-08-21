# The Firewall
source: https://www.idn.id/tutorial-menggunakan-firewall-di-mikrotik/

Firewall is a security system used to protect our network from incoming threat. Firewall is used to protect the network either coming from the WAN (Internet) or the LAN (Local). 
![[firewall.jpg]]

## Why Firewall
- It is used to protect our network either from WAN(Internet) or LAN(Local).
- Protect the network that is going through the router.
- Firewall feature in RouterOS are in IP > Firewall.
- Basic firewall are in IP > Firewall > Filter Rules.

## Firewall - Filter Rules
- A really basic firewall rules in RouterOS
- Every filter rules are organized in a sequence of chain (berurutan dalam sebuah rantai).
- Every chain will be read by the router from top to bottom.
