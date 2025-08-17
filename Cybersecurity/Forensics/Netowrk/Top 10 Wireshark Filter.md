1. IP Filter
	`ip.addr == x.x.x.x`
	`ip.src == x.x.x.x`
	`ip.dst == x.x.x.x`

2. Protocol
	`dns`
	`http`
	`http or dns`
	`http and dns`

3. Specific Port
	 `tcp.port == 443`
	 `udp.port == 9002`

4. Show any TCP problems
	`tcp.analysis.flags`

5. Exclude specific stuff  # cleaning excess stuff
	`!(http or ip.addr == x.x.x.x)`
	`!(http and udp)`
	`!(icmp and ip.src == x.x.x.x)`

6. Content of a packet
	`tcp contain KEYWORD`
	`http contain facebook`
	`http contain google.com`
	`tcp contain netcat`

7. HTTP stuff
	`http.request`
	`http.response.code == 404`
	`http.response`

8. TCP flags
	`tcp.flags.syn == 1`

All of it combined

`ip.addr == 5.161.95.137 or ip.addr == 5.161.100.25 and !(dns or icmp or arp or tcp.analysis.flags or tcp.flags.reset == 1)`