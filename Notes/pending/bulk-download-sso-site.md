---
<div class="frontmatter"><ul>
title: Bulk Download Sso Site
name: BulkDownloadSsoSite
description: Bulk Download Sso Site
type: overview
categories: tech
topics: tech
tags: 
  - #note

id: 528e16
uid: ed990e3f-26db-49ee-9255-15431aa73525
date: 2024-09-12T19:08:34
created_at: 1726135714
updated_at: 1726135714
path: Notes/pending/bulk-download-sso-site.md
slug: bulk_download_sso_site
url: https://username.github.io/repo/posts/2024/09/12/0/1/bulk-download-sso-site
redirect_from: 
  - 

lang: en
author: undefined
private: true
weight: 1
toc: false
draft: true
status: 
keywords: 
changelog: 
versions: 
</ul></div>
---

# Bulk Download Sso Site

<div class='top' align='center'>
  <img src='top.png' alt='alt' height='200px'>
</div>
<div class="toc"></div>
<div style="page-break-after: always;"></div>



## Abstract



## Introduction



## Methodologies

### Prerequisites


Create request body for downloading a file after completing the SSO process:

### Steps to Capture the Download Request:
1. **Open SSO page**: Use Chrome to navigate to the SSO login page and log in as required.
2. **Complete the login**: Finish the login process and confirm that the SSO process is successful.
3. **Open developer tools**: Press `F12` to open the Chrome Developer Tools.
4. **Refresh the page with the download link**: Once logged in, navigate to a page containing the download link and refresh the page.
5. **Capture the request**:
   - Switch to the `Network` tab in the developer tools.
   - Initiate the file download (e.g., by clicking the download link).
   - Identify the request for the download in the `Name` list (usually the first item).
   - Right-click the request and select `Copy` → `Copy as cURL (bash)`.

6. **Modify the request**:
   - Paste the copied request into a text editor.
   - Ensure the headers are complete, especially the `cookie` header, which contains session information required for authentication.
   - Edit the request as needed to fit the batch download process or automate it.

### Refined cURL Command Example:

```bash
curl 'https://www.templatebank.com/downloadfile?18102' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8' \
  -H 'accept-language: en-US,en;q=0.5' \
  -H 'cache-control: max-age=0' \
  -H 'cookie: ASP.NET_SessionId=egcpcn1raig0nc35skdrd4ri; MemID=3986621; MFlag=1; Mail2=fognito%40protonmail%2Ecom; ASPSESSIONIDQAQQTACC=EGHHMAOAPMAJLOFKPJBAKGAK' \
  -H 'referer: https://www.templatebank.com/contents/outsourcing-agreement-contingent-fees' \
  -H 'sec-ch-ua: "Chromium";v="128", "Not;A=Brand";v="24", "Brave";v="128"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: document' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-user: ?1' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
```

### Key Considerations:
- **`cookie` header**: Ensure the session cookies are present for authentication, especially after completing SSO.
- **`user-agent`**: Keep the user-agent to mimic the browser session.
- **URL modification**: Change the URL dynamically for other downloads (e.g., in a script) by using the list of download links from `katana`.

This should allow you to automate file downloads after performing the SSO authentication.
Here's a refined version of the steps to define the request body for downloading a file after completing the SSO process:

### Steps to Capture the Download Request:
1. **Open SSO page**: Use Chrome to navigate to the SSO login page and log in as required.
2. **Complete the login**: Finish the login process and confirm that the SSO process is successful.
3. **Open developer tools**: Press `F12` to open the Chrome Developer Tools.
4. **Refresh the page with the download link**: Once logged in, navigate to a page containing the download link and refresh the page.
5. **Capture the request**:
   - Switch to the `Network` tab in the developer tools.
   - Initiate the file download (e.g., by clicking the download link).
   - Identify the request for the download in the `Name` list (usually the first item).
   - Right-click the request and select `Copy` → `Copy as cURL (bash)`.

6. **Modify the request**:
   - Paste the copied request into a text editor.
   - Ensure the headers are complete, especially the `cookie` header, which contains session information required for authentication.
   - Edit the request as needed to fit the batch download process or automate it.

### Refined cURL Command Example:

```bash
curl 'https://www.templatebank.com/downloadfile?18102' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8' \
  -H 'accept-language: en-US,en;q=0.5' \
  -H 'cache-control: max-age=0' \
  -H 'cookie: ASP.NET_SessionId=egcpcn1raig0nc35skdrd4ri; MemID=3986621; MFlag=1; Mail2=fognito%40protonmail%2Ecom; ASPSESSIONIDQAQQTACC=EGHHMAOAPMAJLOFKPJBAKGAK' \
  -H 'referer: https://www.templatebank.com/contents/outsourcing-agreement-contingent-fees' \
  -H 'sec-ch-ua: "Chromium";v="128", "Not;A=Brand";v="24", "Brave";v="128"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: document' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-user: ?1' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
```

### Key Considerations:
- **`cookie` header**: Ensure the session cookies are present for authentication, especially after completing SSO.
- **`user-agent`**: Keep the user-agent to mimic the browser session.
- **URL modification**: Change the URL dynamically for other downloads (e.g., in a script) by using the list of download links from `katana`.

This should allow you to automate file downloads after performing the SSO authentication.


Here is the refined and streamlined version of your `curl` command for downloading the file from an SSO-authenticated session, with the following changes:

1. **Remove unnecessary headers**: Headers such as `User-Agent` and `Referer` are not necessary.
2. **Adjust the `Accept` header**: Change it to match the content type of the file you want to download.
3. **Windows compatibility**: Remove `--compress` and ensure proper escaping for batch file execution.
4. **Add SSL options**: Include `--ssl-no-revoke` for secure connections.

### Refined `curl` Command:

```bash
set url "https://www.templatebank.com/downloadfile?18102"

curl -vJLO \
  -H 'accept: text/csv' \
  -H 'accept-language: en-US,en;q=0.5' \
  -H 'cache-control: max-age=0' \
  -H 'cookie: MemID=3986621; MFlag=1; Mail2=fognito%40protonmail%2Ecom; ASPSESSIONIDSCSSRDBC=BHMEOEBAGCGLPFDLBNOFNJDA; ASP.NET_SessionId=k0h0klsu2ftip12ajhipg02g; ASPSESSIONIDQAQQTACC=NJHGMAOADALFBJFBCKGBFELK' \
  -H 'content-type: application/x-www-form-urlencoded' \
  -H 'origin: https://www.templatebank.com' \
  -H 'sec-ch-ua: "Chromium";v="128", "Not;A=Brand";v="24", "Brave";v="128"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: document' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-user: ?1' \
  -H 'sec-gpc: 1' \
  -H 'upgrade-insecure-requests: 1' \
  --ssl-no-revoke \
  --data-raw 'contentsInfoId=2300&fileId=18102&categoryId=110' \
  $url
```

### Key Adjustments:
1. **`-H 'accept: text/csv'`**: Adjusted to match the expected content type (`text/csv`). You can change this depending on the actual file type you are downloading.
2. **Removed `User-Agent` and `Referer`**: These headers are optional and removed for simplicity unless they are absolutely required for the download.
3. **`--ssl-no-revoke`**: Ensures secure SSL connections.
4. **`--data-raw`**: Used to pass necessary POST data for the file download request.
5. **`-vJLO`**: Options for verbose output, continuing downloads, and saving to a file.

### Batch File Execution on Windows:
- Save this as a `.bat` file.
- Double-click the `.bat` file or run it from the command line to download the file.

This refined command should handle the file download process after you complete the SSO login and capture the appropriate cookies.
ploo
### Key Considerations:
- **`cookie` header**: Ensure the session cookies are present for authentication, especially after completing SSO.
- **`user-agent`**: Keep the user-agent to mimic the browser session.
- **URL modification**: Change the URL dynamically for other downloads (e.g., in a script) by using the list of download links from `katana`.

This should allow you to automate file downloads after performing the SSO authentication.