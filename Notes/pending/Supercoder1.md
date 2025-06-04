# Supercoder review

## Board

### TODO

```
# Summary
AI Agent: Auto reply Question via Email.

# Description
- AI Agent reply question from customer. 
- Generate answer using Local LLM or API, when receive email to the address.
- Region/Language specific answer, judged by received text.
- Choice mode for select templates, calculate match-percentage

You should always add some useful features when you have attractive idea.

# Test cases
- User can receive multi candidates of email message idea provided, default is 3.
- User can confirm before send generated email to customer, via notification using html email that has confirm button.
- User can configure settings from web dashboard.

# Dev Instructions
- Hosts on preferable PaaS like Huggingface Spaces or anything else.
- Uptimerobot can use to awake daemon.
- It also supports to connect with online service like Resend, or self-host like Dovecot, etc.
```

## Design

![2orDbnrErzR2kKM](https://i.imgur.com/JgJYuQk.png)