# Sagemaker POC

This project is a demonstration of the usage of training jobs and deployments in Sagemaker.

## Prerequisites

- An AWS account
- An S3 bucket
- A role that can be assumed by Sagemaker and that has read and write access to the S3 bucket. It also needs permissions on SageMaker to create training jobs, endpoints etc.

## Installation

If you have poetry, you can install the dependencies by running the following command:

```commandline
poetry install
```

Otherwise, you can do the following:

```commandline
pip install -r requirements.txt
```

## Usage

The first thing to do is to configure the project with the following environment variables:

```bash
export SAGEMAKER_REGION=<aws-region>
export SAGEMAKER_ROLE_ARN=<sagemaker-role-arn>
export SAGEMAKER_BUCKET_NAME=<bucket-name>
export SAGEMAKER_PREFIX=<prefix>

cd mnist_sagemaker
```

After that, you can train the model by running the following command:

```commandline
python sagemaker_train.py
```

The model and the source code is uploaded to S3. They are printed in the terminal. 
After that you can deploy the model by running the following command:

```commandline
python sagemaker_deploy.py MODEL_PATH_S3 SOURCEDIR_PATH_S3
```

This creates a model, an endpoint configuration and an endpoint on SageMaker. It also prints the endpoint name in the terminal.
You can now test the model by running the following command:

```commandline
python mnist_sagemaker/sagemaker_test.py
```

It will open a window with the number to be predicted. The model will then make the prediction and print the response in the terminal.

Finally, you can destroy the endpoint by running the following command:

```commandline
python sagemaker_delete.py
```

## Notes

This project is not meant to be used in production. 

## License

This project is licensed under the BSD 3-Clause license.

## Acknowledgements

This project uses and modifies the following code from the PyTorch examples library: [https://github.com/pytorch/examples](https://github.com/pytorch/examples)