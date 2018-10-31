#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import re

def gen_make_option(file_name,cmd_text):
    root_dir = '/wwwroot'
    script_path = os.path.abspath(__file__)
    script_path = os.path.dirname(script_path)
    file_name = os.path.join(script_path,file_name)
    dirs = os.listdir(root_dir)
    from common_config import host_pattern
    sites = 0
    with open(file_name,'w') as s:
        for k in dirs:
            if re.match(host_pattern, k):
                cur_dir = os.path.join(root_dir,k)
                s.write('cd {} && {}'.format(cur_dir,cmd_text))
                s.write('\n')
                sites += 1
    #print('reload {} sites with {}'.format(sites,cmd_text))

def gen_all_sites():
    gen_make_option('make_all.sh','make html')
    gen_make_option('clean_all.sh','make clean')

if __name__ == '__main__':
    gen_all_sites()