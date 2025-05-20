import os
import re


def convert_md_headings(md_content):
    headers = []
    current_hierarchy = []

    lines = md_content.split('\n')

    for line in lines:
        line = line.strip()
        match = re.match(r'^(#+)(.+)', line)
        if match:
            level = len(match.group(1))
            original_title = match.group(2).strip()
            has_problem = '🚧' in original_title
            if level == 1 and has_problem:
                processed_title = original_title.replace('🚧', '').strip()
            else:
                processed_title = original_title.replace('🚧', 'XXXX').strip()

            # 维护层级结构
            current_hierarchy = current_hierarchy[:level - 1]
            processed_part = [processed_title]

            # 更新当前层级路径
            if level <= len(current_hierarchy):
                current_hierarchy = current_hierarchy[:level - 1]
            current_hierarchy = current_hierarchy[:level - 1] + processed_part

            headers.append({
                'level': level,
                'hierarchy': current_hierarchy.copy(),
                'original': original_title
            })

    # 判断叶子节点
    for i in range(len(headers)):
        current_level = headers[i]['level']
        is_leaf = True
        for j in range(i + 1, len(headers)):
            if headers[j]['level'] > current_level:
                is_leaf = False
                break
            elif headers[j]['level'] <= current_level:
                break
        headers[i]['is_leaf'] = is_leaf

    # 生成结果
    result = []
    for header in headers:
        if header['is_leaf'] and header['level'] > 1:
            # 清理最后可能的"这里有问题"前的空字符串
            clean_hierarchy = [part for part in header['hierarchy'] if part]
            result_line = " - ".join(clean_hierarchy)
            result.append(result_line)

    return result


def process_directory(directory):
    all_rows = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.md'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        md_content = f.read()
                    rows = convert_md_headings(md_content)
                    all_rows.extend(rows)
                except Exception as e:
                    print(f"Error processing {file_path}: {str(e)}")
    print(f"模块数：{all_rows}")
    return all_rows


def export_to_csv(data, output_path):
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        count = 0
        total_rows = len(data)
        print(f'Exporting {total_rows} rows')
        for row in data:
            f.write(row + '\n')
            if "XXXX" in row:
                count += 1
        print(f"{count} rows exported")


if __name__ == "__main__":
    input_dir = "layout/guide"
    output_csv = "test.csv"

    results = process_directory(input_dir)
    export_to_csv(results, output_csv)
