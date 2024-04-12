import os
import asyncio
import unittest

from production_code import Production

from unittest.mock import MagicMock


async def async_add(a, b):
    await asyncio.sleep(1)
    return a + b


class TestAsyncMethod(unittest.IsolatedAsyncioTestCase):
    async def test_add(self):
        """Add function test"""
        r = await async_add(2, 3)
        self.assertEqual(r, 5)


def devide_numbers(x, y):
    return x / y

def multiply_numbers(x, y):
    return x * y


class TestNumberOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # print('Start before all test')
        if not os.path.exists("logs"):
            os.mkdir("logs")


    @classmethod
    def tearDownClass(cls):
        # print('Start after all test')
        pass


    def setUp(self):
        self.logs = open(f"logs/{self._testMethodName}.log", mode='w', encoding="utf-8")

        self.prod = Production()
        self.prod.production_method = MagicMock(return_value="200")

        self.full_prod = MagicMock(spec=Production)


    def tearDown(self):
        self.logs.close()


    def test_multiply_two_positive_numbers(self):
        result = multiply_numbers(2, 3)

        self.logs.write(f"Very important log\n")

        self.assertEqual(result, 6)

        self.full_prod.production_method.return_value = "300"

        self.assertEqual(self.prod.production_method("123"), "200")
        self.assertEqual(self.full_prod.production_method("321"), "300")

        self.prod.production_method.assert_called_with("123")
        self.full_prod.production_method.assert_called_with("321")

        self.assertEqual(self.prod.non_mocked_production_method(), "202")
        # self.assertEqual(self.full_prod.non_mocked_production_method(), "202")


    def test_devide_two_positive_numbers(self):
        self.logs.write(f"Positive check starts\n")

        result = devide_numbers(3, 1)
        self.assertEqual(result, 3)

        with self.assertRaises(ZeroDivisionError) as context:
            devide_numbers(3, 0)


if __name__ == '__main__':
    unittest.main()
