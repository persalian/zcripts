import unittest
import kvm_list


mock_list = {
    "in_data": """
Id    Name                           State
----------------------------------------------------
 1     cloud13                        running
 2     cloud10                        running
 5     cloud5                         running
 -     cloud11                        shut off

""",
    "out_data": [{"name": "cloud9", "status": "running"},
                 {"name": "cloud15", "status": "running"}]
}

mock_dominfo = {
    "in_data" : """
Id:             1
Name:           cloud9
UUID:           2f7518ce-e58b-4caa-9528-177cde040e3e
OS Type:        hvm
State:          running
CPU(s):         5
CPU time:       379713.1s
Max memory:     20971520 KiB
Used memory:    20871520 KiB
Persistent:     yes
Autostart:      enable
Managed save:   no
Security model: none
Security DOI:   0
    """,
    "out_data": {
        "name":"cloud9",
        "state":"running",
        "cpu":5,
        "max_mem": 20971520,
        "cur_mem": 20871520
    }
}

class Test_VM(unittest.TestCase):

    def test_kvm_list(self):
        vm_list = kvm_list.kvm_list(mock_list["in_data"].split("\n"))
        self.assertListEqual(vm_list, mock_list["out_data"], "список VM определен неправильно")


if __name__ == '__main__':
    unittest.main()

