#!/usr/bin/env python3
from lilaclib import *

update_on = [{'aur':None}, {'github':'houtianze/bypy'}]
build_prefix = 'extra-x86_64'
repo_depends = ['python-multiprocess']
pre_build = aur_pre_build
post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
