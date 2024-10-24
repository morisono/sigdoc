- ptt (linux)
```sh
curl -s https://pentest-tools.com/cli-scan/linux/ptt.zip -o /tmp/ptt.zip
unzip /tmp/ptt.zip -d /tmp/ptt
chmod +x /tmp/ptt/main
sudo mv /tmp/ptt/main /usr/local/bin/ptt

# If you have docker or pip installed, you can use them to get ptt-scan:
docker run --rm -it pentesttoolscom/ptt-scan:latest run website_scanner https://pentest-ground.com:81/

ptt run website_scanner <target_url>
ptt -h
```

```sh
usage: ptt [-h] [--fail {low,medium,high,none}] [--key KEY] [--timeout TIMEOUT]
           [--nocolor] [--verbose] [-q]
           {run} ...

Command-line utility for PentestTools.com. Example usage: ptt -q --key <api_key> run
website_scanner https://pentest-ground.com

positional arguments:
  {run}

optional arguments:
  -h, --help            Show this help message and exit.
  --fail {low,medium,high,none}
                        Define failure criteria. `--fail low` fails if even a low
                        vulnerability finding is found.
  --key KEY             The API key. If not provided, obtain one automatically.
  --timeout TIMEOUT     Time to wait for the scan.
  --nocolor             If set, don't color the output at stdout and stderr.
  --verbose             If set, print debug information.
  -q, --quiet           If set, suppress info data and errors. Only print the final
                        report.

```


- https://pentest-tools.com/website-vulnerability-scanning/website-scanner#cli-scan