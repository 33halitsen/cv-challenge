import unittest
from unittest.mock import patch, MagicMock
import json
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import VisitorCounter


class TestLambdaFunction(unittest.TestCase):

    @patch("VisitorCounter.boto3.resource")
    def test_lambda_handler(self, mock_boto_resource):
        mock_table = MagicMock()
        mock_table.update_item.return_value = {"Attributes": {"visit_count": 5}}

        mock_dynamodb = MagicMock()
        mock_dynamodb.Table.return_value = mock_table
        mock_boto_resource.return_value = mock_dynamodb

        fake_event = {}
        fake_context = {}

        result = VisitorCounter.lambda_handler(fake_event, fake_context)

        self.assertEqual(result["statusCode"], 200)
        self.assertEqual(json.loads(result["body"])["visit_count"], 5)
        self.assertEqual(result["headers"]["Access-Control-Allow-Origin"], "*")

        mock_table.update_item.assert_called_once_with(
            Key={"id": "visitor_count"},
            UpdateExpression="ADD visit_count :inc",
            ExpressionAttributeValues={":inc": 1},
            ReturnValues="UPDATED_NEW",
        )


if __name__ == "__main__":
    unittest.main()
