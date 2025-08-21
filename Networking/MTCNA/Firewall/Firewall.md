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
- There are 3 default chain input, output, and forward.
- We could also make our own custom chains as we want. By default if there are no filter rules, all traffic that is coming from, pass, and out of the router will be allowed even if it was unsafe.


## Firewall - Simple Packet Flow

![[packet-flow.jpg]]
There are three bacis packet flow
- Input - to the router
- Forward - pass the router
- Output - from the router 

#### More About Default Chains
1. input
	This chains handle the packet that is going and addressed into the router itself. For example remote access requests to the router.

2. forward
	This chain handle the packet that is going through (pass) the router. For example ping from client pc into the internet.

3. output 
	This chain handle the packet that is originated from the router and going into another network. For example iptables and nftables.

### Firewall - If condition
• IF the packet meets the criteria we created.
![[if.png]]

