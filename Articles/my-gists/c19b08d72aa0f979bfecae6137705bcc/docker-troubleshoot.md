# Docker trouble shoot
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