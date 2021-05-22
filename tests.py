import time
from pathlib import Path

import psutil

from framework.TestCase import TestException, PrepException, TestCase
from framework.TestSuite import TestSuite
from framework.logger import test_logger


class test_1(TestCase):

    def prep(self):
        current_time = time.time()
        if int(current_time) % 2 != 0:
            raise PrepException('Current time is not even')

    def run(self):
        files = []
        for item in Path.home().iterdir():
            if item.is_file():
                files.append(item.name)
        files_str = "\n".join(files)
        test_logger.info(f'Files in home dir:\n'
                         f'{files_str}')


class test_2(TestCase):

    ONE_KB = 1024
    ONE_GB = ONE_KB * 1024 * 1024
    EXPECTED_SIZE = 1024
    TEST_FILE = 'test'

    def prep(self):
        ram = psutil.virtual_memory()[0]
        if ram < self.ONE_GB:
            raise PrepException('Memory size less than 1GB!')

    def run(self):
        with open('test', 'wb') as f:
            for _ in range(1024 * self.ONE_KB):
                f.write(b'1')
        size = Path('test').stat().st_size / self.ONE_KB
        if size != self.EXPECTED_SIZE:
            raise TestException(f'Size of created file should be `{self.EXPECTED_SIZE}` KB.'
                                f' Now is {size}')

    def clean_up(self):
        if Path(self.TEST_FILE).exists():
            Path(self.TEST_FILE).unlink(missing_ok=True)


class SuiteForTask3(TestSuite):
    test_1 = test_1(tc_id=1, name='test_1')
    test_2 = test_2(tc_id=2, name='test_2')


if __name__ == '__main__':
    SuiteForTask3().execute()


