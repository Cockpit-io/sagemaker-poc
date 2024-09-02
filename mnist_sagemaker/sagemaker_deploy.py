import argparse
from sagemaker.pytorch import PyTorchModel
from mnist_sagemaker import config


def sagemaker_deploy(model_data, sourcedir_data):
    model = PyTorchModel(
        model_data=model_data,
        source_dir=sourcedir_data,
        role=config.role,
        framework_version="2.3.0",
        py_version="py311",
        entry_point="mnist.py"
    )

    predictor = model.deploy(initial_instance_count=1, instance_type="ml.c5.2xlarge", endpoint_name=config.endpoint_name)

    print(f"\n Endpoint name: {predictor.endpoint_name} \n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("model_data", help="Path to the model in S3", type=str)
    parser.add_argument("sourcedir_data", help="Path to the source code in S3", type=str)
    args = parser.parse_args()

    sagemaker_deploy(args.model_data, args.sourcedir_data)
