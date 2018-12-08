#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
f = open("/Users/Alihanniba/Documents/reset.txt", encoding='utf-16')
line = f.readline()
while line:
    index = int(line) % 101
    print("update comminfo.userprofile_%d set face_status = 0 where uid = %s limit 1;" % (
        index, line))
    line = f.readline()
f.close()
