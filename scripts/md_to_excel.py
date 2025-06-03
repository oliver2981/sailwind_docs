# _*_ coding:utf-8 _*_
"""
:Author:Hugh
:Date  :2025/05/12
"""

# 提示词：

"""

使用python实现以下需求：

输入：
   a、file_path，一个目录
   b、目录下包含多个.md文件
需求：
   1、输出字段为三个：需求名称、所属模块、需求说明
   2、列名顺序为：需求名称、所属模块、需求说明
   3、所属模块：用md内容的各级标题以/拼接而成
   4、需求名称：需求名为最末级的标题
   5、需求说明：需求说明为属于最末级标题下的正文内容
   6、按一个需求一行进行输出
   7、如果一级标题中有“🚧”，则将其替换为“”
   8、如果非一级标题中有“🚧”，则忽略此模块及其子模块，不需要输出此行
   9、一级标题及其内容输出，不需要输出此行
输出：
   将.md文件内容按需求输出到excel中


示例：

# 第 1 章 SailWind Logic 快速开始

SailWind Logic 是一种强大的多页原理图捕获解决方案，可为 SailWind Layout 构建有效的前端环境。

## 步骤 1 - 开始新设计

1、xxx

2、xxx

## 步骤 2 - 选择纸张尺寸

1、xxx

2、xxx

## 步骤 3 - 添加元件和连接器符号

您可以根据需要在设计中添加元件和连接器符号。

### 添加元件

1、xxx

2、xxx

### 添加连接器符号

1、xxx

2、xxx

## 步骤 4 - 添加总线

1、xxx

2、xxx


输出为：
| 需求名称              | 所属模块                                                     | 需求说明               |
| --------------------- | ------------------------------------------------------------ | ---------------------- |
| 步骤 1 - 开始新设计   | 第 1 章 SailWind Logic 快速开始/步骤 1 - 开始新设计          | 1、xxx<br/><br/>2、xxx |
| 步骤 2 - 选择纸张尺寸 | 第 1 章 SailWind Logic 快速开始/步骤 2 - 选择纸张尺寸        | 1、xxx<br/><br/>2、xxx |
| 添加元件              | 第 1 章 SailWind Logic 快速开始/步骤 3 - 添加元件和连接器符号/添加元件 | 1、xxx<br/><br/>2、xxx |
| 添加连接器符号        | 第 1 章 SailWind Logic 快速开始/步骤 3 - 添加元件和连接器符号/添加连接器符号 | 1、xxx<br/><br/>2、xxx |
| 步骤 4 - 添加总线     | 第 1 章 SailWind Logic 快速开始/步骤 4 - 添加总线            | 1、xxx<br/><br/>2、xxx |


备注：输出示例使用md表格表示，实际输出为写入excel文件

"""

import os
import re
from pathlib import Path

import pandas as pd


def parse_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 提取所有标题信息
    headings = []
    for line_num, line in enumerate(lines):
        match = re.match(r'^(#+)\s*(.*)$', line.strip())
        if match:
            level = len(match.group(1))
            title = match.group(2).strip()

            # 将一级标题中的"🚧"替换为“”
            if level == 1:
                title = title.replace("🚧", "") if "🚧" in title else title

            headings.append({
                'level': level,
                'title': title,
                'start_line': line_num,
                'end_line': None
            })

    # 确定每个标题的结束行
    for i in range(len(headings)):
        if i < len(headings) - 1:
            headings[i]['end_line'] = headings[i + 1]['start_line'] - 1
        else:
            headings[i]['end_line'] = len(lines) - 1

    # 判断是否为末级标题
    # 遍历所有标题，检查后续是否存在更高级或同级标题
    for i in range(len(headings)):
        current_level = headings[i]['level']
        is_last = True
        # 向后查找后续标题
        for j in range(i + 1, len(headings)):
            if headings[j]['level'] > current_level:
                # 发现子标题，说明当前标题不是末级
                is_last = False
                break
            elif headings[j]['level'] <= current_level:
                # 遇到同级或上级标题，表示当前标题已结束
                break
        headings[i]['is_last'] = is_last

    # 构建每个标题的路径
    current_levels = {}
    for heading in headings:
        level = heading['level']
        # 清除同级或更高层级
        keys_to_remove = [k for k in current_levels if k >= level]
        for k in keys_to_remove:
            del current_levels[k]
        current_levels[level] = heading['title']
        # 生成路径
        sorted_levels = sorted(current_levels.keys())
        path = '-'.join([current_levels[l] for l in sorted_levels])
        heading['path'] = path.replace(" ", "_").replace(">", "_").replace("/", "_").replace("\\", "_").replace("__", "_")

    # 收集末级标题的内容
    entries = []
    for heading in headings:
        # 跳过一级标题
        if heading['level'] == 1:
            continue

        # 跳过非一级标题中包含“🚧”的模块
        # if heading['level'] != 1 and "🚧" in heading['title']:
        #     continue

        if heading['is_last']:
            start = heading['start_line'] + 1
            end = heading['end_line'] + 1  # 切片需要包含最后一行
            content_lines = lines[start:end]
            content = ''.join(content_lines).strip()
            entries.append({
                '需求名称': heading['title'],
                '所属模块': heading['path'],
                '需求说明': content
            })

    return entries


def process_directory(file_path, output_excel, ignore_files):
    all_entries = []
    for root, _, files in os.walk(file_path):
        for file in files:
            if file.lower().endswith('.md') and (not ignore_files or file not in ignore_files):
                if file.endswith('.md'):
                    full_path = os.path.join(root, file)
                    entries = parse_md_file(full_path)
                    all_entries.extend(entries)

    # 创建DataFrame并保存Excel
    df = pd.DataFrame(all_entries, columns=['需求名称', '所属模块', '需求说明'])
    df.to_excel(output_excel, index=False, engine='openpyxl')


if __name__ == "__main__":
    file_path = Path(r"D:\hugh\code\sailwind3.0_docs\docs\layout\guide")
    output_file = Path(__file__).parent / "layout_guide.xlsx"
    ignore_files = [
        "20_zh.md",
        "22_zh.md",
        "23_zh.md",
        "33_zh.md",
        "42_zh.md",
        "43_zh.md",
        "44_zh.md",
        "46_zh.md",
        "47_zh.md",
        "48_zh.md",
        "49_zh.md",
        "50_zh.md",
        "51_zh.md",
        "52_zh.md",
        "53_zh.md",
        "54_zh.md",
        "55_zh.md",
    ]

    process_directory(file_path, output_file, ignore_files)

    print(f"处理完成，结果已保存至：{output_file}")
