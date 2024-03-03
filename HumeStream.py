from hume import HumeStreamClient
from hume.models.config import FaceConfig
from hume.models.config import ProsodyConfig

import asyncio

async def main():
    newOpenTimeOut = 3000
    newCloseTimeOut = 3000
    client = HumeStreamClient("<your-api-key-here>", open_timeout=newOpenTimeOut, close_timeout=newCloseTimeOut)
    configs = [FaceConfig(identify_faces=True), ProsodyConfig()]
    async with client.connect(configs) as socket:
        result = await socket.send_file("/Users/jetlin/Desktop/HackMercedWorkshops/HumeRunthrough/IMG_6115.MOV")
        print(result)

asyncio.run(main())