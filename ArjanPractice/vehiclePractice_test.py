import unittest
from vehiclePractice import VehicleInfo

class TestVehicleInfo(unittest.TestCase):

    #tests must start with "test_" before 
    def test_compute_tax_non_electric(self):
        v = VehicleInfo("BMW", False, 10000)
        self.assertEqual(v.compute_tax(), 500)

    def test_compute_tax_electric(self):
        v = VehicleInfo("BMW", True, 10000)
        self.assertEqual(v.compute_tax(),200)

    def test_compute_tax_exemption(self):
        v = VehicleInfo("BMW", False, 10000)
        self.assertEqual(v.compute_tax(5000),250)

    def test_compute_tax_exemption_negative(self):
        v = VehicleInfo("BMW", False, 10000)
        self.assertRaises(ValueError, v.compute_tax, -5000)
    
    def test_can_lease_false(self):
        v = VehicleInfo("BMW", False, 10000)
    pass

unittest.main()