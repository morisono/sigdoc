---

title: Sharing Large file
name: share-large-file
description: 
status: pending
categories: tech
tags: 
  - #howto

lang: en
private: true
weight: 1
image: 
video: 
id: 6d2307
uid: 867b2b69-7589-455d-8941-c2fb3058e85b
link: https://username.github.io/repo/posts/2024/08/24/0/1/sharing-large-file-
path: Notes/pending/share-large-file.md
slug: share-large-file
date: 2024-08-24T15:47:43
created_at: 1724482063
updated_at: 1724482063

---

# share-large-file



## Introduction



## Methodologies

- Compression
```bash
# Password protect
7zz a -t7z download.7z README.md -mem=AES256 -pPass

# Lite Password protect (zip)
7zz a download.zip README.md -mem=AES256 -pPass

# Large file Compression
bzip2 -kv *.txt

## Using 7z (Neither tar, gzip, nor bzip2 supports password protection)
7zz a download.bz2

# Decompress
bzip2 -6 -dkvv download.bz2

## Using 7z
7zz x download.bz2
```

- Downloading
```bash
# First make index
wget --spider $URLTOFILE

# Check "Accept-Ranges: bytes" capable or not
wget --server-response --spider URLTOFILE

# Using SFTP
lftp sftp://user:password@server.org:22 -e 'mirror --verbose --use-pget-n=8 -c /remote/path /local/path'

# Compress before download
## send Accept-Encoding, to mirror bz2
wget --header='Accept-Encoding: gzip' $URL

### compressed speed test ###
wget -O /dev/null $url
 
### debug on screen ##
wget -O- --header='Accept-Encoding: gzip' $URL

## Testing

Use this option to test:

- Testing and troubleshooting HTTP server problems
- CDN edge node speed.
- Your origin server speed.
- Web server gzip comparability.
- Load balancer / reverse proxy server testing.

## Conclusion


## References

1. https://www.cyberciti.biz/faq/unix-linux-wget-download-compressed-gzip-headers/

1. https://superuser.com/questions/162624/how-to-password-protect-gzip-files-on-the-command-line
1. https://superuser.com/questions/480950/how-to-decompress-a-bz2-file
1. https://linuxopsys.com/lftp-commands#3_Reverse_mirroring_of_directory
1. https://superuser.com/questions/40281/how-do-i-get-an-entire-directory-in-sftp
1. https://ja.wikipedia.org/wiki/ZIP_(%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%83%E3%83%88)

[^1]: https://chromewebstore.google.com/detail/curlwget/dgcfkhmmpcmkikfmonjcalnjcmjcjjdn?hl=en
[^2]: https://linux.die.net/man/1/lftp
[^3]: 
