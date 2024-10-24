# Using Scapy for packet analysis
from scapy.all import sniff

# Define a packet callback function
def packet_callback(packet):
    print(packet.summary())

# Start sniffing packets on the network interface
sniff(iface="eth0", prn=packet_callback, count=10)  # Replace "eth0" with your network interface

# Using PyShark for packet analysis
import pyshark

# Open a capture file or start live capture
capture = pyshark.LiveCapture(interface='eth0')  # Replace "eth0" with your network interface

# Loop through captured packets and print details
for packet in capture.sniff_continuously(packet_count=10):  # Capture 10 packets
    print(packet)

# Using dpkt for packet analysis
import dpkt
import socket

# Open a PCAP file for reading
with open('capture.pcap', 'rb') as f:  # Replace 'capture.pcap' with your PCAP file
    pcap = dpkt.pcap.Reader(f)

    # Loop through packets and print source and destination IP addresses
    for timestamp, buf in pcap:
        eth = dpkt.ethernet.Ethernet(buf)
        ip = eth.data
        src_ip = socket.inet_ntoa(ip.src)
        dst_ip = socket.inet_ntoa(ip.dst)
        print(f"Source IP: {src_ip}, Destination IP: {dst_ip}")
