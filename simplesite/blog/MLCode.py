from torchvision.models import resnet50, ResNet50_Weights
from torchvision.io import decode_image

import torch

# Detect dependencies
from torchvision.io.image import read_image
from torchvision.models.detection import fasterrcnn_resnet50_fpn_v2, FasterRCNN_ResNet50_FPN_V2_Weights
from torchvision.utils import draw_bounding_boxes
from torchvision.transforms.functional import to_pil_image, resize


# Base 64 dependencies
import base64
from io import BytesIO

# PIL Fonts
from PIL import ImageFont


def buffer_to_torch(web_data):
    tensor_data = torch.frombuffer(web_data, dtype=torch.uint8)
    img_data = decode_image(tensor_data)
    resized_image = resize(img_data, 1024)
    print(resized_image.shape)
    return resized_image


def predict_image(img):
    weights = ResNet50_Weights.DEFAULT
    model = torch.load('static/models/resnet.pth')
    model.eval()
    preprocess = weights.transforms()
    print("preprocess completed")
    print(img.shape[0])
    # Step 3: Apply inference preprocessing transforms
    batch = preprocess(img).unsqueeze(0)
    print("batch completed")
    prediction = model(batch).squeeze(0).softmax(0)
    print("squeeze completed")
    class_id = prediction.argmax().item()
    score = prediction[class_id].item()
    category_name = weights.meta["categories"][class_id]
    print("reached end of org predict function")
    return (category_name, score)


def detect_image(img):
    # Step 1: Initialize model with the best available weights
    weights = FasterRCNN_ResNet50_FPN_V2_Weights.DEFAULT
    model = torch.load("static/models/CNN.pth")
    model.eval()

    # Step 2: Initialize the inference transforms
    preprocess = weights.transforms()

    # Step 3: Apply inference preprocessing transforms
    batch = [preprocess(img)]

    # Step 4: Use the model and visualize the prediction
    prediction = model(batch)[0]
    labels = [weights.meta["categories"][i] for i in prediction["labels"]]
    box = draw_bounding_boxes(img, boxes=prediction["boxes"],
                              labels=labels,
                              colors="red",
                              font="static/fonts/arial.ttf",
                              width=4, font_size=30)
    im = to_pil_image(box.detach())
    buffered = BytesIO()
    im.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())
    print("reached end of boxing image")
    return img_str

