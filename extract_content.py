#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import json

def main():
    for line in sys.stdin:
        js=json.loads(line)
        print js['conteudo'].lower().encode("utf-8")
if __name__ == '__main__':
    sys.exit(main())
