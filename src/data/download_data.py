import kagglehub
import os

os.environ["KAGGLEHUB_CACHE"] = "C:\\Users\\7louu\\OneDrive\\Bureau\\Testt\\Harassment-Project-\\src\\data"

path = kagglehub.dataset_download("saifulislam7/cyberbullying-and-harassment-detection-using-ml")

print('Dataset downloaded to:', path)