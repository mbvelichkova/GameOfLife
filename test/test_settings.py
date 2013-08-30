import unittest
from settings import Settings


class SettingsTest(unittest.TestCase):
    def test_set_up_default_settings(self):
        default_settings = Settings()
        self.assertEqual(default_settings.cell_stay_alive_list, [2, 3])
        self.assertEqual(default_settings.reproduce_cell_list, [3])

    def test_set_up_custom_settings(self):
        custom_settings = Settings([1, 3], 2)
        self.assertEqual(custom_settings.cell_stay_alive_list, [1, 3])
        self.assertEqual(custom_settings.reproduce_cell_list, [2])
