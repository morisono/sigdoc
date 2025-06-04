# Docker NVidia trouble shoot

- Install toolkit
```sh
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
    
sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit
```

- Memory runtime error
  ```sh
  sudo fallocate -l 8G /swapfile  # スワップファイルを8GBに設定
  sudo chmod 600 /swapfile
  sudo mkswap /swapfile
  sudo swapon /swapfile
  ```

- Error: `libcuda.so.1: cannot open shared object file`
  - symlink の張替え
     ```sh
     ll /usr/lib/wsl/lib
     lll /usr/lib/x86_64-linux-gnu/ | grep cuda
     sudo ln -s /usr/lib/wsl/lib/libcuda.so.1 /usr/lib/x86_64-linux-gnu/libcuda.so.1
     sudo ln -s /usr/lib/wsl/lib/libcuda.so.$CUDA_DRIVER_VERSION /usr/lib/x86_64-linux-gnu/libcuda.so.1
     ```

- Error: `docker: Error response from daemon: unknown or invalid runtime name: nvidia.`
  ```sh
  --env NVIDIA_DISABLE_REQUIRE=1 
  ```

- DockerがNVIDIAランタイムを認識できない

  - バージョンの不整合 確認
    ```sh
    docker info
    journalctl -u docker.service
    nvcc --version
    nvidia-smi
    ```

  - Dockerの設定ファイル（/etc/docker/daemon.json）を編集します。以下のように設定してみてください：
    ```json
    {
      "runtimes": {
        "nvidia": {
          "path": "nvidia-container-runtime",
          "runtimeArgs": []
        }
      },
      "default-runtime": "nvidia"
    }
    ```
  
  - 設定を適用する
    ```sh
    sudo systemctl daemon-reload
    sudo systemctl restart docker
    ```
  
- Dockerコンテナを削除する
  ```sh
  sudo systemctl restart docker.socket docker.service
  docker rm -f <container id>
  ```

- キャッシュを使わずにコンテナをリビルドする
   ```sh
   docker build -t ${NAME}:${TAG} . --no-cache --memory=8g
   ```

- `WSL2 backend always crash System.InvalidOperationException: Failed to deploy distro docker-desktop #7208`
	- https://github.com/docker/for-win/issues/7208
	- https://github.com/docker/for-win/issues/7208#issuecomment-643697540


- https://github.com/docker/for-win/issues/8204%E3%81%AE
```
As a workaround to get Docker working on a Windows Insider build. Uninstall Docker and WSL 2 kernel. Go to the Control Panel -> Programs -> Turn Windows features on or off Uncheck the following: Containers, Hyper-V, Windows Subsystem for Linux Restart the system Install Docker without the WSL2 enabled/checked in the first screen Go to the Control Panel -> Programs -> Turn Windows features on or off Turn on/check the Windows Subsystem for Linux Restart the system. Do not install the WSL2 Kernel.
```
- disable `Install required Windows components for WSL 2`
 - https://stackoverflow.com/questions/66026771/my-docker-is-failing-to-launch-on-my-windows-10-pro

- `For information on key differences with WSL 2 please...`
```
PS> wsl --set-default-version 2

For information on key differences with WSL 2 please visit https://aka.ms/wsl2
```


- WSL2では、Hyper-V とは共存しない
- Docker desktopだけインストールされている状態のwslではWSL2とdockerが紐づけられている

```
PS > wsl -l -v
  NAME                   STATE           VERSION
* docker-desktop-data    Running         2
  docker-desktop         Running         2

```

- Unit docker.service could not be found
```
# Docker desktop 再起動してみる
```