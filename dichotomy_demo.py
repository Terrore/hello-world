#!/usr/bin/env python
# -*- coding: utf-8 -*-

target_list = [1, 6, 9, 15, 26, 38, 49, 57, 63, 77, 81, 93]


def dichotomy_query(num):
    # 记录数组的最高位和最低位
    minimum = 0
    maximum = len(target_list) - 1

    if num in target_list:
        while True:
            # 获取中位数，使用int以防止会出现浮点数
            center = int((minimum + maximum) / 2)
            if target_list[center] > num:  # num 在数组左边
                maximum = center - 1
            elif target_list[center] < num:  # num 在数组右边
                minimum = center + 1
            elif target_list[center] == num:
                print str(num) + "在数组里面的第" + str(center) + "个位置"
                return target_list[center]

    else:
        print "没有这个数字"


if __name__ == '__main__':
    rtn = dichotomy_query(6)

