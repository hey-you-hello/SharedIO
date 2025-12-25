from uuid import uuid4 as uid
import time

class task:
    _nounce = 0   # class-level nounce（每個主機一條序列）

    def __init__(self, IO, client_name, anniversary):
        """
        IO          : bytes / BytesIO / payload
        client_name : 發送者名稱（host hash）
        anniversary : 牽手時間（紀念日）
        """
        self.io = IO
        self.name = client_name

       
        self.timestamp = time.time() - anniversary

        
        self.uuid = uid().hex

        
        self.nounce = self._next_nounce()

    @classmethod
    def _next_nounce(cls):
        cls._nounce += 1
        return cls._nounce
