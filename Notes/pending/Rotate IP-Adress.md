---
<div class="frontmatter"><ul>
title: Rotate ip
name: Rotate IP-Adress
description: 
status: pending
categories: misc
tags: 
  - #note

lang: en
private: true
weight: 1
image: 
video: 
id: c8b536
uid: 14a8c65b-adcd-4032-879a-14bd97ae1e76
link: https://username.github.io/repo/posts/2024/08/23/0/1/rotate-ip-
path: Notes/pending/Rotate IP-Adress.md
slug: Rotate IP-Adress
date: 2024-08-23T15:27:07
created_at: 1724394427
updated_at: 1724394427

---

# Rotate IP-Adress



## Abstract

Rotate IP-Adress in Python with ProtonVPN
With IP rotation you can enhance the level of anonymity. Additionally, it is a widely used practice to automate such tasks as data scraping and web crawling.


## Introduction



## Objectives



## Methodologies

How it’s done:
We want to make use of the command-line tool from ProtonVPN, more specific we want to run the following command from the Shell in Python which which connects to a random server through VPN:
```
sudo protonvpn c -r
```
To run this command automatically from a Python program we can use the subprocess module which allows to run terminal commands. The following Python code makes a random connection to a ProtonVPN server.


Use cases:
Example 1: Random connection every hour

The following Python program connects every hour to a random VPN connection.


Example 2: Switch IP in Selenium
This example shows how you can rotate the IP-adress for a bot which is using the selenium package. The selenium package is used to automate web browser interaction from Python. The IP rotating is useful when your write a bot for a contest which you can only participate a certain amount of time with the same IP. The following pseudo-code can give you an idea:

https://medium.com/@privacytips/best-vpn-solutions-how-to-rotate-your-ip-for-secure-remote-admin-52318a6cc5c4

https://github.com/bradsec/pfsense-vpn-rotator

## Results



## Discussions



## Conclusion



## Summary



## Declarations




## References

1. 
1. 
1. 


[^1]: 
[^2]: 
[^3]: 


