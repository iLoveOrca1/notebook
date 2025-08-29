# 802.11x standarad

| Gen       | Standard | Adopt | Link Rate / Mbps | RF        |
| --------- | -------- | ----- | ---------------- | --------- |
|           | 802.11   | 1997  | 1-2              | 2.4       |
|           | 802.11a  | 1999  | 6-54             | 5         |
|           | 802.11b  | 1999  | 1-11             | 2.4       |
|           | 802.11g  | 2003  | 6-54             | 2.4       |
| Wi-Fi 4   | 802.11n  | 2009  | 6.5 - 600        | 2.4 , 5   |
| Wi-Fi 5   | 802.11ac | 2013  | 6.5 - 6,933      | 5         |
| Wi-Fi 6   | 802.11ax | 2021  | 0.4–9,608        | 2.4 ,5    |
| Wi-Fi 6-E | 802.11ax | 2021  | 0.4–9,608        | 2.4 ,5, 6 |
| Wi-Fi 7   | 802.11be | 2024  | 0.4–23,059       | 2.4 ,5, 6 |
| Wi-Fi 8   | 802.11be |       | 100.000          | 2.4 ,5, 6 |

---

## #2 - Wireless Mode
There are two main Function of Wireless:
- Access Point: Transmitter
- Station: Receiver

Please take a note that not all mode works on a bridge network since not all mode support L2 bridging especially as a receiver (station). For wireless feature MikroTik router require minimum of level 3 license.

**1. Access Point Mode**
	There are two main mode for access point mode, bridge and and ap-bridge:

	a. **bridge mode** can be connected with one client (point-to-point). With bridge mode you didn't have to worry about hacker interrupting and scanning the wireless devices. This mode is usually used on a point-to-point connection like wireless PTP from one router to another.

	b. **ap-bridge mode** can be connected with one or more client (point-to-multipoint). AP-Bridge mode usually used in topology like public wifi or an access point. Keep in mind to be able to use ap-bridge mode we need to have a minimum of level 4 license.

**2. Station Mode**
For every station mode, we could use every station mode with only level 3 license

	a.  **station mode** is used and act as a wireless client in a PTP(point to point) and PTMP(point to multipoint) topology. This wireless mode can only be used in a routing network(Layer 3 only) and does not support bridging. Keep in mind that client that are connected to this mode has to be on a different segment(different network). for example
		- RAP(ap-bridge) - 172.16.8.1
		- RAP(station) - 172.16.8.2
		- Laptop Client(to station RAP) - 192.168.88.2

	b. **station bridge** different from the station, with station bridge we can use a same segment with the access point and will be used in the same layer 2 segment. Keep in mind this mode is only possible if both the client and the access point are using MikroTik devices. here are the example
	- RAP(ap-bridge) - 172.16.8.1
	- RAP(station) - 172.16.8.2
	- Laptop Client(to station RAP) - 172.16.8.3

	c. **station pseudobridge** doesn't differ a lot from station bridge mode. But, with pseudobridge mode we could use our mikrotik as station-bridge with another router or AP vendor and not just MikroTik. But the station-pseudobridge mode also have a downside, that is the client for the **station router** will share the same mac address with the first client that is connected the the **station router** kinda like a NAT but for mac address.

	d. **station pseudobridge clone** doesn't differ a lot either from station pseudobridge. The difference is that with station pseudobridge clone we could set which mac address will be shared for bridging(station-bridge-cloned-mac) even tho it still will use only one mac address.

 	e. **station wds** for those who didnt know wds, wds are also called wireless distribution system
