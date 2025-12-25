import asyncio
import socket


class AsyncSocket:
    def __init__(self, host: str, port: int, *, loop=None):
        self.host = host
        self.port = port
        self.loop = loop or asyncio.get_event_loop()

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setblocking(False)

        self._connected = False

    async def connect(self):
        if self._connected:
            return

        await self.loop.sock_connect(self.sock, (self.host, self.port))
        self._connected = True

    async def read(self, n: int = 4096) -> bytes:
        if not self._connected:
            raise RuntimeError("Socket not connected")

        data = await self.loop.sock_recv(self.sock, n)
        return data

    async def write(self, data: bytes):
        if not self._connected:
            raise RuntimeError("Socket not connected")

        if not isinstance(data, (bytes, bytearray)):
            raise TypeError("data must be bytes")

        await self.loop.sock_sendall(self.sock, data)

    async def close(self):
        if self.sock:
            self.sock.close()
            self._connected = False