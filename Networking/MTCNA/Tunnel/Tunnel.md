# About Tunnel
Tunnel is an encapsulation method for a data packet inside a network. Before being sent, a packet will be slightly modified. That is an addition of a new tunnel header. When the data already passed the tunnel and arrived at the client (the end of the tunnel) then the tunnel header will be poped just like before it enter the tunnel.

TLDR; It makes a virtual Interface that connect directly into the other router as if it was a point-to-point connection between the router

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

**1. PPTP**
This is an older type of protocol that utilize TCP control channel and GRE (General Routing Encapsulation) for tunneling. It is faster but less secure due to an outdated encryption (MS-CHAP v2). It's vulnerable to attacks such as Brute Force and MITM due to it outdated system.

**2. L2TP**
This tunneling protocol often paired with IpSec protocol for tunneling. It doesn't provide encryption but itself was more secure than PPTP with IpSec combined. It is commonly used in VPN remote access, it support multiple platform but can be slower due to the double encapsulation.

**3. PPPoE***
A protocol used for encapsulating PPP protocol over Ethernet networks. Often used in ISP to manage broadband connection and support multiple authentication and common in DSL and fibre optic connection.

**4. EoIP**
This is the most simple tunneling protocol in MikroTik. EoIP is a propietary protocol to build a bridge and tunnel with the other MikroTik router where EoIP interface will act like a normal ethernet interfaces. EoIP uses GRE protocol to build its tunnel. EoIP didn't use any encryption so it isn't recommended to be used as a transmission method that carry confidential data. EoIP uses tunnel ID to identify it's tunnel. MAC addresses between EoIP must differ.

**5.
