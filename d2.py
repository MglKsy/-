import asyncio
import os
import re
import aiohttp
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

mp4_name = "11-2"
m3u8_url = "http://202.117.115.52:8092/file/cloud://10.168.76.10:6201/HIKCLOUD/accessid/NUVQYWFpMEp6c0ppVVJkdFVMbDc5N3VVZjU1MWw4Szc2ODEyOGYyejdHNzkxN2FJMlhYNmQyNzQ0ZDNpTDM2/accesskey/a3gxcEs3SVNiN1lCeTFoOW80OThPb3o4N3I3R3hBQnpFajY3NUk3NVJ6VDdUNDdubTQ4UzQxNDUwN3RRZDJN/bucket/bucket/key/fca56e90e6e846268274a43a0d432e77/1/1731531278/1731533975/0/playback.m3u8"

async def get_m3u8_file():
    if not os.path.exists("ts_file"):
        os.mkdir("ts_file")
    async with aiohttp.ClientSession() as session:
        async with session.get(url=m3u8_url,headers=headers) as resp:
            text = await resp.text()
            path = os.path.join("ts_file","play.m3u8")
            print("m3u8文件存放位置：",path)
            with open(path, "w") as f:
                f.write(text)

async def get_urls():
    with open("ts_file/play.m3u8", "r", encoding="utf8") as f:
        pattern = r"^\d.*"
        urls = re.findall(pattern,f.read(),re.MULTILINE)
    base_url = os.path.dirname(m3u8_url)

    new_urls = []
    # print(base_url + "/" + urls[1])
    for u in urls:
        new_url = base_url + "/" + u
        new_urls.append(new_url)
    # for u in new_urls:
    #     print(u)
    return urls,new_urls

async def download(url):
    path = os.path.join("ts_file",os.path.basename(url))
    with open(path,"wb") as f:
        async with aiohttp.ClientSession() as session:
            async with session.get(url,headers=headers) as resp:
                f.write(await resp.content.read())
                print(f"{os.path.basename(url)} 下载完成")

def delete_tss(urls):
    for url in urls:
        os.remove(url)
    print("ts文件删除成功")

def merge(filename='out'):
    '''
    视频合并
    :return:
    '''
    # 进入到下载后ts 的目录
    os.chdir("ts_file")
    # 视频合并的命令
    os.system(f'ffmpeg -i play.m3u8 -c copy {filename}.mp4')
    print(f'视频{filename} 合并成功====')


async def main():
    await get_m3u8_file()
    await get_urls()
    urls,new_urls = await get_urls()

    tasks = [asyncio.create_task(download(url)) for url in new_urls]
    await asyncio.gather(*tasks)



    merge(mp4_name)
    delete_tss(urls)

if __name__ == '__main__':
     asyncio.run(main())
