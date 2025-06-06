import os
import unittest
from pytplot import data_exists
import pyspedas
from pytplot import del_data


class LoadTestCases(unittest.TestCase):
    def tearDown(self):
        del_data('*')

    def test_downloadonly(self):
        files = pyspedas.projects.image.mena(downloadonly=True)
        self.assertTrue(os.path.exists(files[0]))

    def test_load_notplot(self):
        mena_vars = pyspedas.projects.image.mena(notplot=True)
        self.assertTrue('Image0' in mena_vars)

    def test_load_lena_data(self):
        lena_vars = pyspedas.projects.image.lena(time_clip=True)
        self.assertTrue(data_exists('Image0'))

    def test_load_mena_data(self):
        mena_vars = pyspedas.projects.image.mena()
        self.assertTrue(data_exists('Image0'))

    def test_load_hena_data(self):
        hena_vars = pyspedas.projects.image.hena()
        self.assertTrue(data_exists('Image0'))

    def test_load_rpi_data(self):
        rpi_vars = pyspedas.projects.image.rpi()
        self.assertTrue(data_exists('Amplitude'))

    def test_load_euv_data(self):
        euv_vars = pyspedas.projects.image.euv()
        self.assertTrue(data_exists('IMAGE'))

    def test_load_fuv_data(self):
        fuv_vars = pyspedas.projects.image.fuv()
        self.assertTrue(data_exists('WIC_PIXELS'))

    def test_load_orb_data(self):
        orb_vars = pyspedas.projects.image.orbit()
        self.assertTrue(data_exists('GSM_POS'))
        self.assertTrue(data_exists('GSM_VEL'))

    def test_load_preorb_data(self):
        orb_vars = pyspedas.projects.image.orbit(datatype='pre_or')
        self.assertTrue(data_exists('GSM_POS'))
        self.assertTrue(data_exists('GSM_VEL'))


if __name__ == '__main__':
    unittest.main()
