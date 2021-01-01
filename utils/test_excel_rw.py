from ddt import ddt,data,unpack
from execel_rw import Execel_rw
import unittest
import time

apis = []
data_all = Execel_rw('api.xlsx', 'Sheet1')
max_row = data_all.max_row()
# print(max_row)
for i in range(1,max_row):
    row_1 = []
    for cell in list(data_all.rows())[i]:
        row_1.append(cell.value)
    apis.append(row_1)

@ddt
class Test_rw(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.exe = Execel_rw('api.xlsx', 'Sheet1')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.exe.save()

    @data(*apis)
    def test_1(self,x):
        row = int(x[0])
        if row % 2 == 0:
            self.exe.cell_pass(row+1,9)
        else:
            self.exe.cell_fail(row+1, 9)

if __name__ == '__main__':
    unittest.main()



# for x in apis:
#     exe = Execel_rw('api.xlsx', 'Sheet')
#     exe.cell(x[0] + 1,9,'pass')
#     exe.save()