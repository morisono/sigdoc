![60x Moby-logo](https://user-images.githubusercontent.com/111455900/269958337-46c19f6d-e7b4-4c05-8536-70c57ea950ac.png)

# Docker on WSL2

- GPU Support
```
docker run --rm -it --gpus=all nvcr.io/nvidia/k8s/cuda-sample:nbody nbody -gpu -benchmark
Run "nbody -benchmark [-numbodies=<numBodies>]" to measure performance.
```

```
➜ docker --help

Usage:  docker [OPTIONS] COMMAND

A self-sufficient runtime for containers

Common Commands:
  run         Create and run a new container from an image
  exec        Execute a command in a running container
  ps          List containers
  build       Build an image from a Dockerfile
  pull        Download an image from a registry
  push        Upload an image to a registry
  images      List images
  login       Log in to a registry
  logout      Log out from a registry
  search      Search Docker Hub for images
  version     Show the Docker version information
  info        Display system-wide information

Management Commands:
  builder     Manage builds
  buildx*     Docker Buildx
  checkpoint  Manage checkpoints
  compose*    Docker Compose
  container   Manage containers
  context     Manage contexts
  dev*        Docker Dev Environments
  extension*  Manages Docker extensions
  image       Manage images
  init*       Creates Docker-related starter files for your project
  manifest    Manage Docker image manifests and manifest lists
  network     Manage networks
  plugin      Manage plugins
  sbom*       View the packaged-based Software Bill Of Materials (SBOM) for an image
  scout*      Docker Scout
  system      Manage Docker
  trust       Manage trust on Docker images
  volume      Manage volumes

Swarm Commands:
  config      Manage Swarm configs
  node        Manage Swarm nodes
  secret      Manage Swarm secrets
  service     Manage Swarm services
  stack       Manage Swarm stacks
  swarm       Manage Swarm

Commands:
  attach      Attach local standard input, output, and error streams to a running container
  commit      Create a new image from a container's changes
  cp          Copy files/folders between a container and the local filesystem
  create      Create a new container
  diff        Inspect changes to files or directories on a container's filesystem
  events      Get real time events from the server
  export      Export a container's filesystem as a tar archive
  history     Show the history of an image
  import      Import the contents from a tarball to create a filesystem image
  inspect     Return low-level information on Docker objects
  kill        Kill one or more running containers
  load        Load an image from a tar archive or STDIN
  logs        Fetch the logs of a container
  pause       Pause all processes within one or more containers
  port        List port mappings or a specific mapping for the container
  rename      Rename a container
  restart     Restart one or more containers
  rm          Remove one or more containers
  rmi         Remove one or more images
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  wait        Block until one or more containers stop, then print their exit codes

Invalid Plugins:
  scan        failed to fetch metadata: fork/exec /usr/local/lib/docker/cli-plugins/docker-scan: no such file or directory

Global Options:
      --config string      Location of client config files (default "/home/user/.docker")
  -c, --context string     Name of the context to use to connect to the daemon (overrides DOCKER_HOST env var and
                           default context set with "docker context use")
  -D, --debug              Enable debug mode
  -H, --host list          Daemon socket to connect to
  -l, --log-level string   Set the logging level ("debug", "info", "warn", "error", "fatal") (default "info")
      --tls                Use TLS; implied by --tlsverify
      --tlscacert string   Trust certs signed only by this CA (default "/home/user/.docker/ca.pem")
      --tlscert string     Path to TLS certificate file (default "/home/user/.docker/cert.pem")
      --tlskey string      Path to TLS key file (default "/home/user/.docker/key.pem")
      --tlsverify          Use TLS and verify the remote
  -v, --version            Print version information and quit

Run 'docker COMMAND --help' for more information on a command.

For more help on how to use Docker, head to https://docs.docker.com/go/guides/
```

Data: `C:\Users\<user>\AppData\Local\Docker\wsl\main`
- https://docs.docker.jp/desktop/windows/wsl.html#wsl-rerequisites


### 動作確認
```bash
sudo docker run --rm hello-world
```

## 停止・削除

完全に削除するには、コンテナ・イメージを削除する必要があります。
```bash
docker ps -q 

docker ps -q | xargs docker stop
docker ps -q | xargs docker rm # コンテナの削除

docker images -q | xargs docker rmi # イメージの一括削除

docker rmi <tag>:<id> # If it is tagged in multiple repositories, needs to select tag
```
- https://docs.docker.com/reference/cli/docker/image/rm/
### Trouble shoot
- Docker Desktop.exe が起動しない
	- システムを再起動する
- `docker: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?.`
- Check `Docker Desktop> Settings > Resources > WSL integration`
- Docker desktopからの参照先WSLを変更
> デフォルトでは、Docker DesktopはWSL 2エンジンのデータを `C:\Users\[USERNAME]\AppData\Local\Docker\wsl`。 たとえば、場所を別のドライブに変更する場合は、次の方法で変更できます `Settings -> Resources -> Advanced` Dockerダッシュボードのページ。 これと他のWindows設定の詳細を読む [Windowsのドッカーデスクトップ設定の変更](https://docs.docker.com/desktop/settings/windows/)
- e.g. `F:\wsl\ubuntu\DockerDesktopWSL`

 > Moving a disk image may take several minutes to complete depending on its size and the type of the source and destination drives.


	- docker wsl change integrated distro
	- `wsl --unregister docker-desktop`
	- `wsl --shutdown`
	 
- version の不一致などを確認
```
cat /etc/os-release
docker -v
```
## Appendix

次のように、Linuxファイルシステム上にマウントする。
```
mkdir /etc/linkding/data -p
cd /etc/linkding/data
docker run --name linkding -p 9090:9090 -v /etc/linkding/data -d sissbruecker/linkding:latest
```

- Windows Terminal settings   : `C:\WINDOWS\system32\wsl.exe -d <distro>`
次のように、リモートのWindowsホスト上にマウントすることは、性能を下げるので避ける。
```

docker run -v /mnt/c/users:/users
```

https://github.com/sissbruecker/linkding/