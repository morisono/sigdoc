mkdir whisper
cd whisper
python3 -m venv venv
source venv/bin/activate

# always a good idea to make sure pip is up-to-date
pip install --upgrade pip

# Installation
pip install -U openai-whisper
# pip install git+https://github.com/openai/whisper.git

# Getting started
whisper $audio_file --model small --language Japanese



# if you need ---

# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
