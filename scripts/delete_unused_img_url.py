import os

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
docs_dir = os.path.join(root_dir, "docs")

img_path = os.path.join(docs_dir, "public",  "layout", "guide")
md_path = os.path.join(docs_dir, "v4", "layout", "guide")



img_paths  = []
for root, dirs, files in os.walk(img_path):
    for file in files:
        img_paths.append(os.path.join(root, file).split("public")[-1].replace("\\", "/"))

for md in os.listdir(md_path):
    md_file = os.path.join(md_path, md)
    with open(md_file, "r", encoding="utf-8") as f:
        md_content = f.readlines()
    new_md_content = []
    for line in md_content:
        if line.startswith("![]"):
            img_path_url = line.split("(")[1].split(")")[0]
            if img_path_url not in img_paths:
                continue
        new_md_content.append(line)

        print()