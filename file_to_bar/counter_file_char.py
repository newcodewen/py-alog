# -*- coding: utf-8 -*-
# @Time    : 2020/11/26 17:31

def counter_file_char(file_path: str):
    """
    统计文件中字符的个数
    :param file_path: 文件路径
    :return: 每个字符的统计个数
    """
    countDict = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        # 遍历文档
        for char in content:
          if char == '\n' or char == ' ':
              continue
          # 小写化
          char = char.lower()
          if char in countDict:
              countDict[char] += 1
          else:
              countDict[char] = 1
              
    return countDict
  
countDict = counter_file_char('/Users/wenfucheng/Documents/projects/py-alog/file_to_bar/test.txt')
print(countDict)
  

