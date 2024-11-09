#!/usr/bin/env python3
#! vim:set filetype=python
# -*- coding: utf-8 -*-
# -*- mode: python -*-
# MIT License = 'Copyright (c) 2024 Anoduck'
# This software is released under the MIT License.
# https://anoduck.mit-license.org
# -----------------------------------------------------
import os
import argparse
import re


def ret_lines(file):
    lines = []
    with open(file, 'r') as rf:
        for line in rf.read():
            lines.append(line)
    return lines


def gen_nlist(mddir):
    nlist = []
    filelist = os.listdir(mddir)
    for i in filelist:
        ilst = i.split('.')
        label = ilst[:-2]
        nlist.append(label)
    return nlist


def check_index(index, mddir):
    lines = ret_lines(index)
    nlist = gen_nlist(mddir)
    for line in lines:


def main(**kwargs):
    parser = argparse.ArgumentParser(prog='connect_check',
            description='A link connection checker.'
            usage='%(prog)s -d wiki -i readme.md'
            epilog='Checks directory of mdfiles and makes sure each file has a link.')
    parser.add_argument('-d', '--dirpath', help='Path to directory containing md file, needs to be relative')
    parser.add_argument('-i', '--index', help='The index page or readme file that containing links')
    args = parser.parse_args()
    mddir = args.dirpath
    index = args.index
    mdlink_pat = re.compile(r'\[\w*\]\(\w*\)')
    check_index(index, mddir)


if __name__ is "__main__":
    main()
