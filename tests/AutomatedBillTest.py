import os
import unittest
from unittest.mock import patch, Mock, MagicMock
import AutomatedBill


class AutomatedBillTest(unittest.TestCase):

    def setUp(self):
        os.environ["FILE_PATH"] = "/test/path"
        os.environ["LOGIN_USERNAME"] = "test_username"
        os.environ["LOGIN_PASSWORD"] = "test_password"

    def test_check_for_env_var(self):
        self.assertIsNone(AutomatedBill.check_for_env_var())

    def test_check_for_missing_env_var(self):
        os.environ["LOGIN_USERNAME"] = ""
        with self.assertRaises(EnvironmentError):
            AutomatedBill.check_for_env_var()

    @patch('AutomatedBill.glob.glob', return_value=['test_file1.pdf', 'test_file2.pdf', 'test_file3.pdf'])
    @patch('AutomatedBill.os.path.getmtime', side_effect=[1, 2, 3])
    def test_getting_latest_downloaded_folder(self, mock_list, mock_time):
        file_path = os.getenv("FILE_PATH")
        latest_file = AutomatedBill.getting_latest_downloaded_folder(file_path)
        self.assertEqual(latest_file, 'test_file3.pdf')

    # @patch('AutomatedBill.PdfReader')
    # def test_extracting_amount_due_from_pdf(self, mock_Pdfreader):
    #     file_path = os.getenv("FILE_PATH")
    #     mock_reader = MagicMock()
    #     mock_reader.pages[0].extract_text.return_value = "€79.50 Amount Due"
    #     mock_Pdfreader.return_value = mock_reader
    #     result = AutomatedBill.extracting_amount_due_from_pdf(file_path)
    #     self.assertEqual("€79.50 Amount Due", result)


if __name__ == '__main__':
    unittest.main()


