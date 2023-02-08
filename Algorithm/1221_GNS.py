import sys
sys.stdin = open("GNS_test_input.txt", "r")

def word_to_num(word_list):
    change_list = []
    for i in range(len(word_list)):
        if word_list[i] == 'ZRO':
            change_list.append(0)
        elif word_list[i] == 'ONE':
            change_list.append(1)
        elif word_list[i] == 'TWO':
            change_list.append(2)
        elif word_list[i] == 'THR':
            change_list.append(3)
        elif word_list[i] == 'FOR':
            change_list.append(4)
        elif word_list[i] == 'FIV':
            change_list.append(5)
        elif word_list[i] == 'SIX':
            change_list.append(6)
        elif word_list[i] == 'SVN':
            change_list.append(7)
        elif word_list[i] == 'EGT':
            change_list.append(8)
        elif word_list[i] == 'NIN':
            change_list.append(9)
        else:
            pass
    return change_list

def num_to_word(num_list):
    change_list = []
    for i in range(len(num_list)):
        if num_list[i] == 0:
            change_list.append('ZRO')
        elif num_list[i] == 1:
            change_list.append('ONE')
        elif num_list[i] == 2:
            change_list.append('TWO')
        elif num_list[i] == 3:
            change_list.append('THR')
        elif num_list[i] == 4:
            change_list.append('FOR')
        elif num_list[i] == 5:
            change_list.append('FIV')
        elif num_list[i] == 6:
            change_list.append('SIX')
        elif num_list[i] == 7:
            change_list.append('SVN')
        elif num_list[i] == 8:
            change_list.append('EGT')
        elif num_list[i] == 9:
            change_list.append('NIN')
        else:
            pass
    return change_list

test_case = int(input())
for tc in range(test_case):
    q, n = input().split()
    GNS = list(map(str,input().split()))
    newlist = word_to_num(GNS)
    newlist.sort()
    GNSlist = num_to_word(newlist)
    print(q)
    print(*GNSlist)
