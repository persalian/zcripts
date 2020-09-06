import unittest
import cert
import datetime

mock = {
    'info_in': ['            Not Before: Aug 29 21:52:48 2020 GMT',
                '            Not After : Nov 27 21:52:48 2020 GMT'],
    'info_out': {'start': '2020-08-29', 'end': '2020-11-27'},
    'info_rest': {'days': 82}
}


class TestCert(unittest.TestCase):

    def test_cert_valid(self):
        tested_res = {'start': datetime.datetime.strptime(mock['info_out']['start'], '%Y-%m-%d').date(),
               'end': datetime.datetime.strptime(mock['info_out']['end'],   '%Y-%m-%d').date()
             }
        res = cert.valid_period(mock['info_in'])
        self.assertDictEqual(res, tested_res)

    def test_crt_rest_of_days(self):
        tested_now = datetime.datetime(2020, 9, 6).date()
        res = cert.rest_of_days(tested_now, mock['info_in'])
        self.assertEqual(res, mock['info_rest']['days'])


if __name__ == '__main__':
    unittest.main()
