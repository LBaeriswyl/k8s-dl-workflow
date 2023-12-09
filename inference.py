import mnist_net
import config
import torch
from torchvision import datasets, transforms
from flask import Flask, request, jsonify


app = Flask(__name__)


def create_test_set():
  transform=transforms.Compose([
      transforms.ToTensor(),
      transforms.Normalize((0.1307,), (0.3081,))
      ])

  test_set = datasets.MNIST(config.DATASET_PATH, train=False, transform=transform)
  return test_set


def load_inference_model():
  model = mnist_net.Net()
  model.load_state_dict(torch.load(config.MODEL_PATH))
  model.eval()
  return model


test_set = create_test_set()
model = load_inference_model()


@app.route('/predict/<int:index>', methods=['GET'])
def perform_inference(index):
  if index < 0 or index >= len(test_set):
    response = {"message": f"Index must be between 0 and {len(test_set)-1}"}
    return jsonify(response)
  
  image, true_label = test_set[index]

  with torch.no_grad():
    output = model(image.unsqueeze(0))
    prediction = output.argmax(dim=1, keepdim=True)


  response = {"message": f"The model predicted {prediction.item()} for the image with the label {true_label}"}
  return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
