from torchvision.models import resnet50, ResNet50_Weights
from torchvision.io import decode_image

import torch

# Detect dependencies
from torchvision.io.image import read_image
from torchvision.models.detection import fasterrcnn_resnet50_fpn_v2, FasterRCNN_ResNet50_FPN_V2_Weights
from torchvision.utils import draw_bounding_boxes
from torchvision.transforms.functional import to_pil_image


# Base 64 dependencies
import base64
from io import BytesIO

def predict_image(image_data):
    tensor_data = torch.frombuffer(image_data, dtype=torch.uint8)
    img = decode_image(tensor_data)
    weights = ResNet50_Weights.DEFAULT
    model = resnet50(weights=weights)
    model.eval()
    preprocess = weights.transforms()

    # Step 3: Apply inference preprocessing transforms
    batch = preprocess(img).unsqueeze(0)
    prediction = model(batch).squeeze(0).softmax(0)
    class_id = prediction.argmax().item()
    score = prediction[class_id].item()
    category_name = weights.meta["categories"][class_id]
    return (category_name, score)


def detect_image(image_data):
    tensor_data = torch.frombuffer(image_data, dtype=torch.uint8)
    img = decode_image(tensor_data)

    # Step 1: Initialize model with the best available weights
    weights = FasterRCNN_ResNet50_FPN_V2_Weights.DEFAULT
    model = fasterrcnn_resnet50_fpn_v2(weights=weights, box_score_thresh=0.9)
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
                              font="arial",
                              width=4, font_size=30)
    im = to_pil_image(box.detach())
    buffered = BytesIO()
    im.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())
    return img_str

