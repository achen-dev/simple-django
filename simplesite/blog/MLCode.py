from torchvision.models import resnet50, ResNet50_Weights
from torchvision.io import decode_image
import torch

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