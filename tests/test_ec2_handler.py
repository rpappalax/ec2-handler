import unittest
from ec2_handler.ec2_handler import EC2Handler

d = EC2Handler()


class EC2HandlerTestCase(unittest.TestCase):
    """Tests for `ec2_handler.py`."""

    def test_is_instance(self):
        """Does this function actually return False?"""
        region = 'us-east-1'
        aws_access_key_id = ''
        aws_secret_access_key = ''
        kwargs = {
            'aws_access_key_id': aws_access_key_id,
            'aws_secret_access_key': aws_secret_access_key
        }
        self.assertFalse(d.ec2_instance(region, kwargs))


if __name__ == '__main__':
    unittest.main()
