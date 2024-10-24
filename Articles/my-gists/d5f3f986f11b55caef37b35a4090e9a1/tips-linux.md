- Create Mirror website
```
sudo apt-get install httrack
httrack #url -o ***
# wget
cat links.txt | xargs -i wget --mirror --convert-links --adjust-extension --page-requisites --no-parent {}
```