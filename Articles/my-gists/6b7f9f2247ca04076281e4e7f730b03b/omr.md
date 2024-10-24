## OMR (Optical Musicscore Recognition)
(WSL2, fish shell, Linuxbrew)


```
# tesseract ocr
sudo apt update
sudo apt install tesseract-ocr
sudo apt install tesseract-ocr-eng tesseract-ocr-jpn tesseract-ocr-rus tesseract-ocr-fra tesseract-ocr-spa tesseract-ocr-chi-sim tesseract-ocr-kor 
tesseract --version
```

```
brew install openjdk@11
set JAVA_HOME "/usr/local/opt/openjdk@11"
git clone https://github.com/Audiveris/audiveris.git
cd audiveris
./gradlew build
./gradlew run

```

https://audiveris.github.io/audiveris/_pages/install/sources/