from flask import json
from api import app
import unittest

class FlaskApiTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_predict_endpoint(self):
        # Sample payload matching the structure your API expects 
        payload = {
            "battery_power": 842,
            "blue": 0,
            "clock_speed": 2.2,
            "dual_sim": 0,
            "fc": 1,
            "four_g": 0,
            "int_memory": 7,
            "m_dep": 0.6,
            "mobile_wt": 188,
            "n_cores": 2,
            "pc": 2,
            "px_height": 20,
            "px_width": 756,
            "ram": 2549,
            "sc_h": 9,
            "sc_w": 7,
            "talk_time": 19,
            "three_g": 0,
            "touch_screen": 0,
            "wifi": 1
        }

        response = self.app.post('/predict', data=json.dumps(payload), content_type='application/json')
        data = json.loads(response.get_data(as_text=True))

        # Assuming '1' is the expected prediction for the given payload
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['price_range'], 1)

if __name__ == '__main__':
    unittest.main()
