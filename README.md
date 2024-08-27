# food-waste-inference-api
This lightweight web API is intended to run alongside the [Smart Bin Server](https://github.com/Soundbendor/compost-bin-server), allowing computer vision inference to be offloaded to a separate GPU node, while our database and public web API for serving compost bin clients runs on a storage node.

This API exposes one route, which allows a client to send an image to the server, and returns an image with segmentations drawn overtop, as well as a `results.txt` which provides labels and polygon coordinates for each detected food waste item.

We use [YOLOv8](https://github.com/ultralytics/ultralytics) for our image recognition model. Training code for this model can be found [here](https://github.com/Soundbendor/food-detection-cv)
