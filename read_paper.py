from pypdf import PdfReader
import os

def read_all_papers(folder_path="papers"):
    all_text = ""
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            reader = PdfReader(os.path.join(folder_path, filename))
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            all_text += f"\n===== 论文：{filename} =====\n{text}"
    return all_text

if __name__ == "__main__":
    content = read_all_papers()
    with open("papers_summary.txt","w",encoding="utf-8") as f:
        f.write(content)
    print("✅ 全部PDF文字提取完成，保存到 papers_summary.txt")
