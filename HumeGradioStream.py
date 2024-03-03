from hume import HumeStreamClient
from hume.models.config import FaceConfig
from hume.models.config import ProsodyConfig
import gradio as gr

import asyncio

async def HumeStream(client_key, video_file):
    newOpenTimeOut = 3000
    newCloseTimeOut = 3000

    client = HumeStreamClient(client_key, open_timeout=newOpenTimeOut, close_timeout=newCloseTimeOut)
    
    file = video_file

    configs = [FaceConfig(identify_faces=True), ProsodyConfig()]
    async with client.connect(configs) as socket:
        result = await socket.send_file(file)
        return result



interface = gr.Interface( # inputs key, and video file #outputs: prediction json
    fn = HumeStream,
    inputs = ["text", gr.Video(label = "Video to analyze", format="mp4")], #client key, video file
    outputs = ["text"],# for predictions in JSON
    description = "Enter a video for emotion analysis"
).launch(share=True, auth=("jet", "pass"), auth_message="check your email for username and password")

