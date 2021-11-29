import unittest
from utils import calculate_bmi,calculate_health_risk
from bmi_cal import process_data

class BMITest(unittest.TestCase):
    def test_check_bmi(self):
        sample_weight = 96
        sample_height = 171
        calculated_bmi = round(calculate_bmi(sample_weight,sample_height), 2)
        actual_bmi = 32.83
        self.assertEqual(calculated_bmi,actual_bmi)
    
    def test_health_risk(self):
        sample_bmi = 32.79
        actual_health_risk = ['Moderately obese',sample_bmi,'Medium Risk']
        calculated_health_risk = calculate_health_risk(sample_bmi)
        self.assertEqual(calculated_health_risk,actual_health_risk)

    def test_process_data(self):
        sample_data = [['Gender','Height(cm)','Weight (kg)'],['Female','166','62']]
        actual_health_risk_output = 'Low Risk'
        calculated_health_risk = process_data(sample_data)[0][-1]
        self.assertEqual(calculated_health_risk,actual_health_risk_output)
        
if __name__ == '__main__':
   print('hello')
   unittest.main()