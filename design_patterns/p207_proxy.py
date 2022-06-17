"""代理模式

能够提供对象的替代品或其占位符。

## 作用
可以实现延迟初始化, 访问控制, 记录日志请求,  缓存请求结果

## 区别
代理与其服务对象遵循同一接口， 使得自己和服务对象可以互换， 在这一点上它与外观不同。

适配器模式能为被封装对象提供不同的接口， 代理模式能为对象提供相同的接口， 装饰模式则能为对象提供加强的接口。

代理通常自行管理其服务对象的生命周期(在服务端侧添加)， 而装饰的生成则总是由客户端进行控制。(在客户端侧添加)
"""

import time
from datetime import datetime
from typing import List, Dict

class ServerMixin:
    pass

class HTTPServer(ServerMixin):
    def view_hello(self):
        time.sleep(3)
        return 'hello'

class Nginx(ServerMixin):
    def __init__(self) -> None:
        self.conn: HTTPServer = None
        self.cache: Dict[str, str] = {}

    def handle_get(self, url: str):
        if self.conn is None:
            self.conn = HTTPServer()

        if url in self.cache:
            return self.cache[url]

        if url.startswith('/hello'):
            self.cache[url] = self.conn.view_hello()
            return self.cache[url]
        return '404'

    def handle(self, url: str) -> str:
        self.handle_get(url)
        self.access_log(url)

    def access_log(self, url: str):
        print(f'{datetime.now()} - get - {url}')


def main():
    s = Nginx()
    print(datetime.now())
    s.handle('/hello')
    s.handle('/xxxx')
    s.handle('/hello')

if __name__ == '__main__':
    main()
