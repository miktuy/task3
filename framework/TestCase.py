from framework.logger import test_logger


class TestException(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        test_logger.error(f'\tTest Fail: {message}')


class PrepException(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        test_logger.error(f'\tPrecondition Fail: {message}')


class TestCase:
    def __init__(self, tc_id: int, name: str):
        self.tc_id = tc_id
        self.name = name

    def prep(self):
        raise NotImplementedError

    def run(self):
        ...

    def clean_up(self):
        raise NotImplementedError

    def execute(self):
        try:
            self.prep()
            test_logger.info(f'\t{self.name}: Precondition is done')
            self.run()
        except (PrepException, TestException, NotImplementedError):
            pass  # PrepException, TestException is expected situation during the test
        except Exception as e:
            test_logger.error(f'\t{self.name}: Error in test !!!')
            raise e
        else:
            test_logger.info(f'\t{self.name}: TEST PASS !!!')
        finally:
            try:
                self.clean_up()
            except NotImplementedError:
                pass
            except Exception as e:
                test_logger.error(f'Error during clean up!!!: {e}')
            else:
                test_logger.info(f'\t{self.name}: Clean up is done')

