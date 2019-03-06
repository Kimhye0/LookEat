from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

arguments = {"keywords":"느타리버섯", "language":"Korean","limit":100, "output_directory":"mushroom","print_urls":True}
paths = response.download(arguments)
print(paths)