from boto3 import client

from helper_functions.logger import logger


class AWSClient:
    """Class to initiate AWS ssm client.

    >>> AWSClient

    """

    def __init__(self):
        self.client = client('ssm')

    def put_parameters(self, name: str, value: str):
        """Uses boto3 to update credentials in AWS and returns 200 if successful.

        Args:
            name: Name of the parameter that has to dropped in AWS.
            value: Value of the parameter that has to dropped in AWS as SecureString.

        """
        response_put = self.client.put_parameter(Name=name, Value=value, Type='SecureString', Overwrite=True)
        if response_put['ResponseMetadata']['HTTPStatusCode'] == 200:
            logger.critical(f'Parameter {name} has been updated on SSM parameter store.')
        else:
            logger.error(f'Parameter {name} WAS NOT added to SSM parameter store.')