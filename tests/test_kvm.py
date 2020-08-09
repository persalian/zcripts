import unittest
import kvm_stat


mock_list = {
    "in_data": """
 Id    Name                           State
----------------------------------------------------
 1     cloud9                         running
 2     cloud15                        running

""",
    "out_data": [{"name": "cloud9", "status": "running"},
                 {"name": "cloud15", "status": "running"}]
}


class Test_VM(unittest.TestCase):

    def test_kvm_list(self):
        vm_list = kvm_stat.kvm_list(mock_list["in_data"].split("\n"))
        self.assertListEqual(vm_list, mock_list["out_data"], "список VM определен неправильно")


if __name__ == '__main__':
    unittest.main()

