"""
寫入測試 Log 到檔案中
"""
import os
import argparse

from datetime import datetime, timezone
from os.path import join as pjoin


parser = argparse.ArgumentParser(description='Write test logs')
parser.add_argument('-n', '--line-num', type=int,
                    dest='log_num', default=1000, help='Line numbers')
parser.add_argument('-p', '--path', type=str, dest='path',
                    default=pjoin(os.path.dirname(os.path.abspath(__file__)), 'logs'), help='output path')

args = parser.parse_args()

log_num = args.log_num
path = args.path

date = datetime.now(timezone.utc).date()

file_name = "{:04d}-{:02d}-{:02d}-fake.log".format(
    date.year, date.month, date.day)
file_path = pjoin(path, file_name)

os.makedirs(os.path.dirname(file_path), exist_ok=True)
with open(file_path, 'a') as f:
    for n in range(log_num):
        t = datetime.now(timezone.utc)
        log = '[{}]    fakelogs={{"index":"{}", "microseconds":"{}"}}\n'.format(
            t.isoformat(), n, t.microsecond)
        f.write(log)
