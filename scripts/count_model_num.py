import os
import re


def convert_md_headings(md_content):
    headings = []
    hierarchy = []

    for line in md_content.splitlines():
        line = line.strip()
        match = re.match(r'^(#+)\s*(.*)', line)
        if match:
            level = len(match.group(1))
            title = match.group(2).replace('🚧', '' if level == 1 else 'XXXX').strip()
            # 更新层级
            hierarchy = hierarchy[:level - 1] + [title]
            headings.append({'level': level, 'hierarchy': hierarchy.copy()})

    # 标记叶子节点
    for i, h in enumerate(headings):
        h['is_last'] = not any(
            hh['level'] > h['level'] and j > i and (
                all(headings[k]['level'] > h['level'] for k in range(i + 1, j))
            )
            for j, hh in enumerate(headings[i + 1:], start=i + 1)
        )

    # 生成结果
    return [
        " - ".join(filter(None, h['hierarchy']))
        for h in headings if h['is_last'] and h['level'] > 1
    ]


def process_directory(directory, ignore_files=None):
    all_rows = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.md') and (not ignore_files or file not in ignore_files):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        rows = convert_md_headings(f.read())
                    print(f"{file}，模块数：{len(rows)}")
                    all_rows.extend(rows)
                except Exception as e:
                    print(f"处理 {file_path} 出错: {e}")
    print(f"模块：{all_rows}")
    return all_rows


def export_to_csv(data, output_path):
    count = sum('XXXX' in row for row in data)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(data))
    print(f'导出 {len(data)} 行，其中包含"XXXX"的有 {count} 行')


if __name__ == "__main__":
    input_dir = r"D:\hugh\code\sailwind3.0_docs\docs\layout\guide"
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
    output_csv = "test.csv"
    results = process_directory(input_dir, ignore_files)
    export_to_csv(results, output_csv)
