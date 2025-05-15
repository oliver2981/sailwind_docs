# _*_ coding:utf-8 _*_
"""
:Author:Hugh
:Date  :2025/04/24
"""
import os
import re
import sys
import chardet
from bs4 import BeautifulSoup


def convert_table_to_markdown(html_table):
    """增强版HTML表格转换"""
    soup = BeautifulSoup(html_table, 'html.parser')
    rows = soup.find_all('tr')

    # 智能识别表头（处理<th>标签）
    headers = []
    for cell in rows[0].find_all(['th', 'td']):
        headers.append(cell.get_text(separator=' ', strip=True))

    # 构建数据行（自动填充缺失列）
    data_rows = []
    markdown_table = []
    for row in rows[1:]:
        cells = row.find_all(['td', 'th'])
        row_data = [cell.get_text(separator=' ', strip=True).replace('|', r'\|') for cell in cells]
        row_data += [''] * (len(headers) - len(row_data))  # 自动补全空列
        data_rows.append(row_data[:len(headers)])  # 截断多余列

        # 动态生成对齐线（支持中文表头）
        sep_row = '| ' + ' | '.join(
            ['---' if re.search(r'[\u4e00-\u9fff]', h) else '-' * len(h) for h in headers]) + ' |'

        # 组装Markdown表格
        markdown_table = [
            f"| {' | '.join(headers)} |",
            sep_row,
            *[f"| {' | '.join(row)} |" for row in data_rows]
        ]
    return '\n'.join(markdown_table)


def convert_file(input_path, output_path):
    """处理单个文件转换"""
    with open(input_path, 'rb') as f:
        raw = f.read()
        encoding = chardet.detect(raw)['encoding'] or 'utf-8'
    content = raw.decode(encoding)

    # 使用更精准的表格匹配正则
    pattern = re.compile(r'<table[\s\S]*?>[\s\S]*?</table>', re.IGNORECASE)
    new_content = pattern.sub(lambda m: convert_table_to_markdown(m.group()), content)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(new_content)


def process_directory(input_dir, output_dir):
    """处理目录转换"""
    for root, dirs, files in os.walk(input_dir):
        # 创建对应的输出目录结构
        relative_path = os.path.relpath(root, input_dir)
        dest_dir = os.path.join(output_dir, relative_path)
        os.makedirs(dest_dir, exist_ok=True)

        for file in files:
            if file.lower().endswith('.md'):
                src_file = os.path.join(root, file)
                dest_file = os.path.join(dest_dir, file)
                convert_file(src_file, dest_file)


if __name__ == "__main__":
    # 命令行参数配置
    import argparse

    parser = argparse.ArgumentParser(description='Markdown表格转换工具')
    parser.add_argument('-i', '--input', required=True, help='输入文件或目录路径')
    parser.add_argument('-o', '--output', required=True, help='输出文件或目录路径')
    args = parser.parse_args()

    # 路径验证
    if not os.path.exists(args.input):
        print(f"错误：输入路径 '{args.input}' 不存在")
        sys.exit(1)

    try:
        # 处理不同输入类型
        if os.path.isfile(args.input):
            # 文件到文件的转换
            if os.path.isdir(args.output):
                output_path = os.path.join(args.output, os.path.basename(args.input))
            else:
                output_path = args.output
            convert_file(args.input, output_path)
            print(f"成功转换文件：{args.input} -> {output_path}")

        elif os.path.isdir(args.input):
            # 目录到目录的转换
            if not os.path.exists(args.output):
                os.makedirs(args.output, exist_ok=True)
            process_directory(args.input, args.output)
            print(f"成功转换目录：{args.input} -> {args.output}")

    except Exception as e:
        print(f"转换失败：{str(e)}")
        sys.exit(1)
