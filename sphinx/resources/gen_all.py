#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import re

def gen_all_sites():
    root_dir = '/wwwroot'
    script_path = os.path.abspath(__file__)
    script_path = os.path.dirname(script_path)
    file_name = os.path.join(script_path,'make_all.sh')
    dirs = os.listdir(root_dir)
    from common_config import host_pattern
    sites = 0
    with open(file_name,'w') as s:
        for k in dirs:
            if re.match(host_pattern, k):
                cur_dir = os.path.join(root_dir,k)
                s.write('cd {} && make html'.format(cur_dir))
                s.write('\n')
                sites += 1
    print('reload {} sites'.format(sites))

if __name__ == '__main__':
    gen_all_sites()