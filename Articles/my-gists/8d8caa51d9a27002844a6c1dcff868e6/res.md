```sh
❯ nikto -h $aucnet
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          210.144.113.52
+ Target Hostname:    www.aucnet.jp
+ Target Port:        443
+ Start Time:         2024-06-07 11:31:26 (GMT9)
---------------------------------------------------------------------------
+ Server: nginx
+ The anti-clickjacking X-Frame-Options header is not present.
+ Uncommon header 'x-content-type-options' found, with contents: nosniff
+ Uncommon header 'x-xss-protection' found, with contents: 1; mode=block
+ Uncommon header 'strict-transport-security' found, with contents: max-age=31536000; includeSubdomains
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ 6544 items checked: 0 error(s) and 4 item(s) reported on remote host
+ End Time:           2024-06-07 11:48:52 (GMT9) (1046 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

wafw00f on  master via 🐍 v2.7.18 took 17m26s
➜ nuclei -ut && nuclei -target $aucnet

                     __     _
   ____  __  _______/ /__  (_)
  / __ \/ / / / ___/ / _ \/ /
 / / / / /_/ / /__/ /  __/ /
/_/ /_/\__,_/\___/_/\___/_/   v2.9.6

                projectdiscovery.io

[INF] No new updates found for nuclei templates

                     __     _
   ____  __  _______/ /__  (_)
  / __ \/ / / / ___/ / _ \/ /
 / / / / /_/ / /__/ /  __/ /
/_/ /_/\__,_/\___/_/\___/_/   v2.9.6

                projectdiscovery.io

[WRN] Found 2770 templates with syntax error (use -validate flag for further examination)
[WRN] Found 16 templates with runtime error (use -validate flag for further examination)
[INF] Current nuclei version: v2.9.6 (outdated)
[INF] Current nuclei-templates version: v9.8.7 (latest)
[INF] New templates added in latest release: 62
[INF] Templates loaded for current scan: 5444
[INF] Targets loaded for current scan: 1
[INF] Templates clustered: 1481 (Reduced 1406 Requests)
[ssl-issuer] [ssl] [info] www.aucnet.jp:443 [GlobalSign nv-sa]
[ssl-dns-names] [ssl] [info] www.aucnet.jp:443 [aucnet.jp,www.aucnet.jp]
[INF] Using Interactsh Server: oast.live
[addeventlistener-detect] [http] [info] https://www.aucnet.jp/
[xss-deprecated-header] [http] [info] https://www.aucnet.jp/ [1; mode=block]
[tech-detect:google-tag-manager] [http] [info] https://www.aucnet.jp/
[tech-detect:google-font-api] [http] [info] https://www.aucnet.jp/
[tech-detect:nginx] [http] [info] https://www.aucnet.jp/
[thumbs-db-disclosure] [http] [info] https://www.aucnet.jp/Thumbs.db
[robots-txt-endpoint] [http] [info] https://www.aucnet.jp/robots.txt
[http-missing-security-headers:cross-origin-opener-policy] [http] [info] https://www.aucnet.jp/
[http-missing-security-headers:x-permitted-cross-domain-policies] [http] [info] https://www.aucnet.jp/
[http-missing-security-headers:clear-site-data] [http] [info] https://www.aucnet.jp/
[http-missing-security-headers:x-frame-options] [http] [info] https://www.aucnet.jp/
[http-missing-security-headers:referrer-policy] [http] [info] https://www.aucnet.jp/
[http-missing-security-headers:cross-origin-embedder-policy] [http] [info] https://www.aucnet.jp/
[http-missing-security-headers:cross-origin-resource-policy] [http] [info] https://www.aucnet.jp/
[http-missing-security-headers:content-security-policy] [http] [info] https://www.aucnet.jp/
[http-missing-security-headers:permissions-policy] [http] [info] https://www.aucnet.jp/
[caa-fingerprint] [dns] [info] www.aucnet.jp
[robots-txt] [http] [info] https://www.aucnet.jp/robots.txt
[waf-detect:nginxgeneric] [http] [info] https://www.aucnet.jp/
[tls-version] [ssl] [info] www.aucnet.jp:443 [tls12]
```