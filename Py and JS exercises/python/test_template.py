import os
import unittest
from pathlib import Path

from template import *


def test_freeFall():
    assert freeFall(1,True) == 0.45
    assert freeFall(0.45,False) == 0.99


def test_RPS():
    assert RPS('RPS') == 'PSR'
    assert RPS('PRSPRR') == 'SPRSPP'


def test_list2str():
    assert list2str(['a',['b','c']]) == '[a[bc]]'
    assert list2str(['a',['b',['c']]]) == '[a[b[c]]]'


def test_textPreprocessing():
    case = unittest.TestCase()
    case.assertCountEqual(textPreprocessing('I think, therefore I am.'), ['think', 'therefore'])
    case.assertCountEqual(textPreprocessing('When life gives you lemons, make lemonade.'), ['life', 'give', 'you', 'lemon', 'make', 'lemonade'])


def test_isGreaterThan():
    assert isGreaterThan({'a':1,'b':2},{'a':1,'b':1}) == True
    assert isGreaterThan({'a':1,'b':1},{'a':1,'b':1}) == False
    assert isGreaterThan({'a':1,'b':0},{'a':0,'b':1}) == False


def test_CSVsum():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file1 = Path(script_dir, 'test_data', 'table1.csv')
    input_file2 = Path(script_dir, 'test_data', 'table2.csv')
    assert CSVsum(input_file1) == [5.0, 8.0, 6.0]
    assert CSVsum(input_file2) == [57.0, 518.0]


def test_str2list():
    case = unittest.TestCase()
    case.assertCountEqual(str2list('[a[bc]]'), ['a',['b','c']])
    case.assertCountEqual(str2list('[a[b[c]]]'), ['a',['b',['c']]])


def test_spacemonSim():
    assert spacemonSim([('Earth',100,10), ('Earth',100,10)], [('Mercury',80,10), ('Venus',80,10)]) == False
    assert spacemonSim([('Earth',100,10)], [('Mercury',80,10), ('Mars',80,10)]) == True


def test_rewardShortPath():
    assert rewardShortPath([['A','X','R','R','R'],['O','O','O','X','B'],['O','O','O','O','R']]) == (7,3)
    assert rewardShortPath([['A','X','R','R','R'],['O','O','O','X','R'],['O','O','O','B','R']]) == (5,0)


def test_cliqueCounter():
    network1 = [[0,1,1,0,0,0,0],
            [1,0,1,1,0,0,0],
            [1,1,0,0,0,0,0],
            [0,1,0,0,1,1,1],
            [0,0,0,1,0,1,0],
            [0,0,0,1,1,0,1],
            [0,0,0,1,0,1,0]]

    network2 = [[0,1,0,0,0,0,1],
            [1,0,0,0,0,0,1],
            [0,0,0,1,0,0,1],
            [0,0,1,0,0,0,1],
            [0,0,0,0,0,1,1],
            [0,0,0,0,1,0,1],
            [1,1,1,1,1,1,0]]


    assert cliqueCounter(network1) == [1, 2, 1, 3, 1, 2, 1]
    assert cliqueCounter(network2) == [1, 1, 1, 1, 1, 1, 3]

