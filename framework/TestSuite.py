from typing import List

from framework.logger import test_logger
from framework.TestCase import TestCase


class TestSuite:

    def _get_test_cases(self):
        return [getattr(self, item) for item in dir(self) if item.startswith('test_')]

    def execute(self):
        tests: List[TestCase] = self._get_test_cases()
        for test in tests:
            test_logger.info(f'Run test case: {test.name}')
            test.execute()
