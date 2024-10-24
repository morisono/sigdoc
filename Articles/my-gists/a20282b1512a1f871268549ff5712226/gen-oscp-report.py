import os
import sys
import json
from datetime import datetime

def collect_data():
    data = {
        "summary": [
            {"ip": "192.168.xx.xx", "hostname": "hostname1", "exploit": "Name of initial exploit"},
            {"ip": "192.168.xx.xx", "hostname": "hostname2", "exploit": "Name of initial exploit"},
            {"ip": "192.168.xx.xx", "hostname": "hostname3", "exploit": "Name of initial exploit"},
            {"ip": "192.168.xx.xx", "hostname": "hostname4", "exploit": "Name of initial exploit"},
            {"ip": "192.168.xx.xx", "hostname": "hostname5", "exploit": "BOF"}
        ],
        "information_gathering": [
            {"ip": "192.168.1.1"},
            {"ip": "192.168.1.2"},
            {"ip": "192.168.1.3"},
            {"ip": "192.168.1.4"},
            {"ip": "192.168.1.5"}
        ],
        "penetration": [
            {
                "ip": "192.168.x.x",
                "service_enumeration": {
                    "open_ports": "TCP: 1433,3389\nUDP: 1434,161",
                    "nmap_scan_results": "Nmap scan details here",
                    "initial_shell_vulnerability": "Initial shell vulnerability details here",
                    "vulnerability_explanation": "Explanation here",
                    "vulnerability_fix": "Fix here",
                    "severity": "Severity here",
                    "proof_of_concept_code": "PoC code here",
                    "local_txt_proof_screenshot": "Local.txt screenshot here",
                    "local_txt_contents": "Local.txt contents here"
                },
                "privilege_escalation": {
                    "priv_esc_info": "Privilege escalation info here",
                    "vulnerability_exploited": "Exploited vulnerability here",
                    "vulnerability_explanation": "Explanation here",
                    "vulnerability_fix": "Fix here",
                    "severity": "Severity here",
                    "exploit_code": "Exploit code here",
                    "proof_screenshot": "Proof screenshot here",
                    "proof_txt_contents": "Proof.txt contents here"
                }
            },
            # Add additional systems as needed
        ],
        "buffer_overflow": {
            "ip": "192.168.x.x",
            "vulnerability_exploited": "bof",
            "bof_notes": "Buffer Overflow notes here",
            "proof_screenshot": "Proof screenshot here",
            "completed_bof_code": "Completed BOF code here"
        },
        "additional_items": {
            "proof_and_local_contents": [
                {"ip": "192.168.x.x", "local_txt_contents": "hash_here", "proof_txt_contents": "hash_here"},
                {"ip": "192.168.x.x", "local_txt_contents": "hash_here", "proof_txt_contents": "hash_here"},
                {"ip": "192.168.x.x", "local_txt_contents": "hash_here", "proof_txt_contents": "hash_here"},
                {"ip": "192.168.x.x", "local_txt_contents": "hash_here", "proof_txt_contents": "hash_here"},
                {"ip": "192.168.x.x", "local_txt_contents": "hash_here", "proof_txt_contents": "hash_here"}
            ],
            "metasploit_usage": "192.168.x.x",
            "completed_bof_code": "Completed BOF code here"
        }
    }
    return data

def generate_report(data, output_file="OSCPReport.json"):
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    data = collect_data()
    generate_report(data)
    print(f"OSCP report data has been written to {os.path.abspath('OSCPReport.json')}")
