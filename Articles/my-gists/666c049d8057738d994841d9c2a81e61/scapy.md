# scapy

Scapyは、Pythonでパケット操作を行うための強力なライブラリです。ネットワークトレースやパケットの生成などが可能です。

https://scapy.net/

以下の関数は、各 TTL に対してパケットを送信し、応答がある場合は応答元のIPアドレスを表示します。
> [!note] 
TTL（Time to Live）は、コンピュータネットワークにおいて、データグラム（通信の単位）がネットワーク上で通過できるホップ数または経過できる時間を制限するための値です。TTLは通常、データグラムがネットワーク内を移動する際に利用されます。
```py
from scapy.all import *

def trace_route(destination, max_hops=30):
    for ttl in range(1, max_hops + 1):
        packet = IP(dst=destination, ttl=ttl) / ICMP()
        reply = sr1(packet, verbose=0, timeout=1)
        if reply is None:
            break
        elif reply.src == destination:
            print(f"{ttl}: {reply.src} (Destination reached)")
            break
        else:
            print(f"{ttl}: {reply.src}")

if __name__ == "__main__":
    destination_ip = "example.com"  # Set the destination IP or domain
    trace_route(destination_ip)
```

