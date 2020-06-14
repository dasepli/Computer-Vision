#!/usr/bin/env python3.7
# coding: utf-8

"""
这个文件依照同文件夹下的.tmpplate文件生成从Level-1到Level-3的prototxt文件
"""

import sys


nameDict = {
    's0': ['F'],  # face
    's1': ['EN', 'NM'], # EN & NM
    's2': ['LE1', 'LE2', 'RE1', 'RE2', 'N1', 'N2', 'LM1', 'LM2', 'RM1', 'RM2']}

def generate(network, level, names, mode='GPU'):
    """
        network: CNN type
        level: LEVEL
        names: CNN names
        mode: CPU or GPU
    """
    assert(mode == 'GPU' or mode == 'CPU')

    types = ['train', 'solver']
    for name in names:
        for t in types:
            tempalteFile = 'prototxt/{0}_{1}_prototxt.template'.format(network, t)
            with open(tempalteFile, 'r') as fd:
                template = fd.read()
                outputFile = 'prototxt/{0}_{1}_{2}.prototxt'.format(level, name, t)
                print (template.format(level=level, name=name, mode=mode))
                with open(outputFile, 'w') as fd:
                    fd.write(template.format(level=level, name=name, mode=mode))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        mode = 'GPU'
    else:
        mode = 'CPU'
    generate('s0', 1, nameDict['s0'], mode)
    generate('s1', 1, nameDict['s1'], mode)
    generate('s2', 2, nameDict['s2'], mode)
    generate('s2', 3, nameDict['s2'], mode)