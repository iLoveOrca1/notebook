# About Tunnel
Tunnel is an encapsulation method for a data packet inside a network. Before being sent, a packet will be slightly modified. That is an addition of a new tunnel header. When the data already passed the tunnel and arrived at the client (the end of the tunnel) then the tunnel header will be poped just like before it enter the tunnel.

# Tunnels in MikroTik
There are many types of tunnel in MikroTIk:
- PPTP (Point To Point Tunneling Protocol)
- L2TP (Layer 2 Tunneling Protocol)
- PPPoE (Point to Point Protocol over Ethernet)
- EoIP (Ethernet over IP)
- SSTP (Secure Socket Tunneling Protocol)

We can see that in virtual interface that we can add them.

# VPN in MikroTik
- OpenVPN
- Wiregurad

# VPN vs Tunnels
VPN works in as a client-server so you only need one public IP to access the vpn. Meanwhile Tunnel works like point-to-point. That means that you need two public IP to connect each router.

# More About Tunnel in MikroTik

### 1. PPTP
This is an older type of protocol that utilize TCP control channel and GRE (General Routing Encapsulation) for tunneling. It is faster but less secure due to an outdated encryption (MS-CHAP v2). It's vulnerable to attacks such as Brute Force and MITM due to it outdated system.
