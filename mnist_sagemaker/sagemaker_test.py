import gzip
import numpy as np
import random
import os
import sagemaker
import json
import matplotlib.pyplot as plt
from torchvision import transforms, datasets

from mnist_sagemaker import config


def download_data():
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))])

    datasets.MNIST('data', train=True, download=True, transform=transform)
    datasets.MNIST('data', train=False, download=True, transform=transform)


def get_random_number():
    data_dir = "data/MNIST/raw"
    with gzip.open(os.path.join(data_dir, "t10k-images-idx3-ubyte.gz"), "rb") as f:
        images = np.frombuffer(f.read(), np.uint8, offset=16).reshape(-1, 28, 28).astype(np.float32)

    mask = random.sample(range(len(images)), 16)
    mask = np.array(mask, dtype=np.int32)
    data = images[mask]

    plt.imshow(data[0])
    plt.show()

    payload = np.expand_dims(data, axis=1)
    payload = json.dumps(payload.tolist())

    return payload


def parse_response(response):
    response_parsed = json.loads(str(response).replace("b", "").replace("'", ""))
    labeled_predictions = list(zip(range(10), response_parsed[0]))
    labeled_predictions.sort(key=lambda label_and_prob: 1.0 - label_and_prob[1])
    print("Most likely answer: {}".format(labeled_predictions[0][0]))


def main():

    download_data()
    payload = get_random_number()

    predictor = sagemaker.predictor.Predictor(endpoint_name=config.endpoint_name)
    response = predictor.predict(payload, initial_args={'ContentType': 'application/json'})

    parse_response(response)


if __name__ == "__main__":
    main()
