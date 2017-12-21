import gevent
import urllib.request

def download_image(image_url, image_name):
    # 大开网络资源
    response = urllib.request.urlopen(image_url)
    # 此处要耗时,二进制读取图片
    image_data = response.read()
    # 写入制定文件
    with open(image_name,"wb") as file:
        file.write(image_data)

# 请求资源数据的连接
image_url1 = ""
image_url2 = ""
image_url3 = ""
# gecent.joinall()等待协程执行完毕,主线程退出
gevent.joinall([gevent.spawn(download_image, image_url1, "1.jpg"),
                gevent.spawn(download_image, image_url1, "1.jpg"),
                gevent.spawn(download_image, image_url1, "1.jpg")
               ])



