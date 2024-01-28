from django.test import TestCase


# Create your tests here.
class PaymentTestCase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_name_is_str(self):
        name = "John"
        self.assertEqual(name, "John")