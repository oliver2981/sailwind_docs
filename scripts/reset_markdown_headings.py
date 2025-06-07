# _*_ coding:utf-8 _*_
"""
:Author:Hugh
:Date  :2025/04/24
"""

import re
import fitz  # PyMuPDF
import os
import shutil
import argparse
from pathlib import Path
from datetime import datetime

project_path = Path(__file__).parent.parent


def clean_heading_text(text):
    """清理标题文本，去除加粗标记和前后空格"""
    # 去除Markdown加粗语法：**bold** 或 __bold__
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'__(.+?)__', r'\1', text)
    return text.strip()


def get_pdf_heading_structure(pdf_file):
    """
    获取PDF文件的标题结构
    返回: (完整标题结构字典, 按一级标题分组的结构字典, 一级标题列表)
    """
    doc = fitz.open(pdf_file)
    toc = doc.get_toc()

    full_structure = {}
    chapter_structures = {}
    chapter_titles = []
    current_chapter = None

    for level, title, page in toc:
        # 清理标题中的特殊字符和前后空格
        title = clean_heading_text(title.replace("\u2028", ""))

        full_structure[title] = level

        if level == 1:
            current_chapter = title
            chapter_structures[current_chapter] = {title: level}
            chapter_titles.append(current_chapter)
        elif current_chapter:
            chapter_structures[current_chapter][title] = level

    return full_structure, chapter_structures, chapter_titles


def backup_directory(src_dir, backup_dir):
    """创建目录的完整备份"""
    if os.path.exists(backup_dir):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dir = f"{backup_dir}_{timestamp}"

    shutil.copytree(src_dir, backup_dir)
    return backup_dir


def find_markdown_files(directory):
    """递归查找目录下的所有Markdown文件"""
    return list(Path(directory).rglob('*.md'))


def get_first_level1_heading(md_file):
    """
    获取Markdown文件的第一个一级标题（清理加粗标记后）
    返回: (原始标题内容, 清理后的标题内容, 是否找到)
    """
    with open(md_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            match = re.match(r'^#\s+(.+)$', line)
            if match:
                original_title = match.group(1)
                cleaned_title = clean_heading_text(original_title)
                return original_title, cleaned_title, True
    return None, None, False


def reset_markdown_headings(heading_structure, input_file, output_file=None, first_heading=None):
    """
    根据标题结构重置Markdown标题层级
    output_file为None时直接覆盖原文件
    """
    if output_file is None:
        output_file = input_file

    heading_levels = {clean_heading_text(title): level for title, level in heading_structure.items()}

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    processed_lines = []
    first_heading_processed = False

    for line in lines:
        if "<span id=" in line:
            line = re.sub(r"\<span id\=.+\/span\>", "", line)  # 去除 <span id=...> 标签
        match = re.match(r'^(#+)\s+(.+)$', line)
        if match:
            hashes, title = match.groups()
            stripped_title = title.strip()
            cleaned_title = clean_heading_text(stripped_title)
            current_level = len(hashes)

            # 如果是第一个一级标题且已经处理过，跳过特殊处理
            if current_level == 1 and cleaned_title == first_heading:
                if first_heading_processed:
                    # 后续的一级标题保持原样
                    processed_lines.append(line)
                    continue
                first_heading_processed = True

            if cleaned_title in heading_levels:
                desired_level = heading_levels[cleaned_title]
                new_hashes = '#' * desired_level
                processed_lines.append(f"{new_hashes} {cleaned_title}")
            else:
                processed_lines.append(f"**{cleaned_title}**\n")
        else:
            processed_lines.append(line)

    # 确保输出目录存在
    os.makedirs(os.path.dirname(output_file) or '.', exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(processed_lines)


def process_markdown_files(pdf_path, markdown_dir, output_dir=None, backup=True):
    """
    处理目录及其子目录下的所有Markdown文件

    参数:
        pdf_path: PDF文件路径
        markdown_dir: Markdown文件根目录
        output_dir: 输出目录(None则覆盖原文件)
        backup: 是否创建备份
    """
    # 创建备份
    if backup and output_dir is None:
        backup_dir = backup_directory(markdown_dir, f"{markdown_dir}_backup")
        print(f"已创建备份目录: {backup_dir}")

    # 获取PDF结构信息
    full_structure, chapter_structures, chapter_titles = get_pdf_heading_structure(pdf_path)

    # 查找所有Markdown文件
    md_files = find_markdown_files(markdown_dir)

    # 统计信息
    processed = 0
    skipped = 0
    no_heading = 0

    for md_file in md_files:
        # 获取文件的第一个一级标题（原始内容和清理后内容）
        original_title, cleaned_title, found = get_first_level1_heading(md_file)

        if not found:
            print(f"警告: 文件 {md_file} 没有一级标题，跳过处理")
            no_heading += 1
            continue

        # 查找匹配的章节（使用清理后的标题）
        matched_chapter = None
        for chapter in chapter_titles:
            if chapter.lower() == cleaned_title.lower():
                matched_chapter = chapter
                break

        if matched_chapter and matched_chapter in chapter_structures:
            # 确定输出路径
            rel_path = os.path.relpath(md_file, markdown_dir)
            if output_dir:
                output_path = os.path.join(output_dir, rel_path)
            else:
                output_path = md_file

            print(f"处理文件: {md_file} (匹配章节: {matched_chapter})")
            reset_markdown_headings(chapter_structures[matched_chapter], md_file, output_path, cleaned_title)
            processed += 1
        else:
            print(f"警告: 文件 {md_file} 没有匹配的PDF章节，跳过处理")
            skipped += 1

    print(f"\n处理完成统计:")
    print(f"- 成功处理: {processed} 个文件")
    print(f"- 跳过无匹配章节: {skipped} 个文件")
    print(f"- 跳过无一级标题: {no_heading} 个文件")


if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description="将 PDF 转换为 Markdown 或覆盖现有文件")
    #
    # # 必选参数
    # parser.add_argument(
    #     "--pdf",
    #     type=Path,
    #     required=True,
    #     help="PDF 文件路径（如 sailwindlayout_gd.pdf）",
    # )
    # parser.add_argument(
    #     "--markdown_dir",
    #     type=Path,
    #     required=True,
    #     help="Markdown 根目录（如 docs/v4/layout/guide）",
    # )
    #
    # # 可选参数（--output 不提供时，默认覆盖原文件）
    # parser.add_argument(
    #     "--output_dir",
    #     type=Path,
    #     default=None,
    #     help="输出目录（如不提供，则覆盖原文件）",
    # )
    #
    # args = parser.parse_args()

    # pdf = args.pdf  # 替换为您的PDF路径
    # markdown_dir = args.markdown_dir  # Markdown根目录
    # output_dir = args.output_dir  # 设为None覆盖原文件，或指定输出目录

    pdf = r"C:\Users\Administrator\Desktop\code\sailwind3.0_docs\docs\public\pdf\sailwindrouter_gd.pdf"  # 替换为您的PDF路径
    markdown_dir = r"C:\Users\Administrator\Desktop\code\sailwind3.0_docs\docs\router\guide"  # Markdown根目录
    output_dir = None  # 设为 None 覆盖原文件，或指定输出目录

    # 处理文件
    process_markdown_files(
        pdf_path=pdf,
        markdown_dir=project_path / markdown_dir,
        output_dir=output_dir,
        backup=True
    )
