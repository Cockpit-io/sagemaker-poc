from sagemaker.predictor import Predictor
from mnist_sagemaker import config


def main():
    predictor = Predictor(endpoint_name=config.endpoint_name)

    predictor.delete_model()
    predictor.delete_endpoint(delete_endpoint_config=True)
    print(f"Endpoint {config.endpoint_name} has been deleted")


if __name__ == "__main__":
    main()
