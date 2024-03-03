from hume import HumeBatchClient
from hume.models.config import FaceConfig


newTimeOut = 3000
client = HumeBatchClient("y7wUAPHS6ihjAyZsZwp4AN8EZtTFtyIfGnKJR4nRwhwLprDa", timeout=newTimeOut)


files = ["/Users/jetlin/Desktop/HackMercedWorkshops/HumeRunthrough/humerunthroughpicture.jpg"]
configs = [FaceConfig(identify_faces=True)]
job = client.submit_job(urls=[], configs=configs, files=files)

print(job)
print("Running...")

job.await_complete()
job.download_predictions("predictions.json")
print("Predictions downloaded to predictions.json")

job.download_artifacts("artifacts.zip")
print("Artifacts downloaded to artifacts.zip")

print(job.get_predictions())