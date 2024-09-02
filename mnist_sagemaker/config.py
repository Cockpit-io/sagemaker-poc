import os
import datetime
import sagemaker

sagemaker_session = sagemaker.Session()

region = os.environ["SAGEMAKER_REGION"]
role = os.environ["SAGEMAKER_ROLE_ARN"]
bucket_name = os.environ["SAGEMAKER_BUCKET_NAME"]
prefix_name = os.environ["SAGEMAKER_PREFIX_NAME"]

current_datetime = datetime.datetime.now().strftime("%H-%M-%S-%d-%m-%Y")
training_job_name = f"{prefix_name}-{current_datetime}"
endpoint_name = f"{prefix_name}"

assert region is not None, "SAGEMAKER_REGION environment variable is not set"
assert role is not None, "SAGEMAKER_ROLE_ARN environment variable is not set"
assert bucket_name is not None, "SAGEMAKER_BUCKET_NAME environment variable is not set"
assert prefix_name is not None, "SAGEMAKER_PREFIX_NAME environment variable is not set"
