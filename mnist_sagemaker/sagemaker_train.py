from sagemaker.pytorch import PyTorch
from mnist_sagemaker import config


def sagemaker_train():
    pyversion = "py311"
    framework_version = "2.3.0"
    hyperparameters = {"epochs": 1}
    instance_type = "ml.c5.2xlarge"

    print("Starting Sagemaker training")
    estimator = PyTorch(
        entry_point="mnist.py",
        py_version=pyversion,
        framework_version=framework_version,
        role=config.role,
        instance_count=1,
        instance_type=instance_type,
        hyperparameters=hyperparameters,
        output_path=f"s3://{config.bucket_name}/"
    )

    estimator.fit(job_name=config.training_job_name)

    print(f"Model data: {estimator.model_data} \n")
    print(f"Sourcedir: {estimator.uploaded_code.s3_prefix} \n")


if __name__ == "__main__":
    sagemaker_train()

