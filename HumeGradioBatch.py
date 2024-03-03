from hume import HumeBatchClient
from hume.models.config import FaceConfig
import gradio as gr


def HumeBatch(client_key, file):
    newTimeOut = 3000
    client = HumeBatchClient(client_key, timeout=newTimeOut)

    files = [file]

    configs = [FaceConfig(identify_faces=True)]
    job = client.submit_job(urls=[], configs=configs, files=files)
    
    print(job)
    print("Running...")
    job.await_complete()
    job.download_predictions("predictions.json")
    job.download_artifacts("artifacts.zip")
    return (job, job.get_predictions())


interface = gr.Interface(
    fn = HumeBatch,
    inputs = ["text", gr.Image(label = "Image to analyze", type="filepath")], #client key, files
    outputs = ["text", "text"],# for predictions, and for artifacts
    description = "Enter a picture for emotion analysis"
).launch(share=True, auth=("jet", "pass"), auth_message="check your email for username and password")


# print(job)
# print("Running...")

# job.await_complete()
# job.download_predictions("predictions.json")
# print("Predictions downloaded to predictions.json")

# job.download_artifacts("artifacts.zip")
# print("Artifacts downloaded to artifacts.zip")

# print(job.get_predictions())