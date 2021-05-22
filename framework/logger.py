import logging
import sys


test_logger = logging.getLogger('test')

format_ = logging.Formatter(fmt="""--------------------------------------------------------------------
{asctime}: {message}
--------------------------------------------------------------------""", style="{")

console_handler = logging.StreamHandler(sys.stdout)
console_handler.flush = sys.stdout.flush
console_handler.setFormatter(format_)
test_logger.addHandler(console_handler)

file_handler = logging.FileHandler("test.log", "w")
test_logger.addHandler(file_handler)
file_handler.setFormatter(format_)

test_logger.setLevel("INFO")

