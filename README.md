# 这是一个西电回放录播下载的python脚本

- 环境： anaconda python=3.12

- 该下载脚本用了协程实现，基本下载50分钟左右的视频只需要3分钟左右
  通过conda下载  aiohttp包

运行步骤：

- 创建虚拟环境

```bash
conda create -n {随便起个环境名字} python=3.12
```

- 下载协程相关的软件包

```bash
conda install -c conda-forge aiohttp
```

- 打开视频播放的界面

  ```python
  F12打开开发者界面
  网络 -> Fetch/XHR -> 刷新界面找到第一个 playback.m3u8请求-> 复制该请求网址
  eg: 		http://202.117.115.52:8092/file/cloud://10.168.76.10:6201/HIKCLOUD/accessid/NUVQYWFpMEp6c0ppVVJkdFVMbDc5N3VVZjU1MWw4Szc2ODEyOGYyejdHNzkxN2FJMlhYNmQyNzQ0ZDNpTDM2/accesskey/a3gxcEs3SVNiN1lCeTFoOW80OThPb3o4N3I3R3hBQnpFajY3NUk3NVJ6VDdUNDdubTQ4UzQxNDUwN3RRZDJN/bucket/bucket/key/365a7dfac0844bc399604c418d749d83/1/1731529026/1731532323/0/playback.m
  
  修改 d2代码中的 m3u8_url 为你复制的请求链接
  修改 mp4_name 为你想要保存的视频文件名称， 如第11周的第1节课可命名为 11-1

  运行主程序
  ```

  

