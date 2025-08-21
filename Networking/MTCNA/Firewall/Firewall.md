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
- The packet will be matched with a criteria inside a chain, if matched the packed will be executed. If not the packet will be matched with the rules inside the next chain untill it matched a criteria. 
- There are 3 chain input, output, and forward.




### Firewall Chains
1. input
	This chains handle the packet that is going and addressed into the router itself. For example remote access requests to the router.

2. forward
	This chain handle the packet that is going through (pass) the router. For example ping from client pc into the internet.

3. output 
	This chain handle the packet that is originated from the router and going into another network. For example iptables and nftables.



