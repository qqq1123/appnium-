
import unittest
from base.demo import RunMain
import json
import HTMLTESTRUNNER
from base.mock_demo import mock_test

class TestMethod(unittest.TestCase):
    def setUp(self):
        self.run = RunMain()
    def test_01(self):
        url = 'http://127.0.0.1:8000/login/'
        data = {
            'username':'lirundong',
            'password':'5621232'
        }
        #self.run.run_main = mock.Mock(return_value=data)
        res = mock_test(self.run.run_main,data,url,'POST',data)
        #res = self.run.run_main(url,'POST',data)
        print(res)
        self.assertEqual(res['password'],'5621232','测试通过')


    def test_02(self):
        url = 'http://127.0.0.1:8000/login2/?username=lirundong&password=123123&token=DSADSA1111'
        res = self.run.run_main(url,'GET')
        re = json.loads(res)
        self.assertEqual(re['user'], 'lirun2dong', '测试失败')
        print(re)

if __name__ == '__main__':
    pass
filepath = 'C:\\Users\\Administrator\\PycharmProjects\\api_test_star\\report\\htmltest1.html'
fp = open(filepath,'wb')
suite = unittest.TestSuite()
suite.addTest(TestMethod('test_01'))
suite.addTest(TestMethod('test_02'))
#unittest.TestSuite.run()
runner = HTMLTESTRUNNER.HTMLTestRunner(stream=fp,title='this is first report')
runner.run(suite)
fp.close()