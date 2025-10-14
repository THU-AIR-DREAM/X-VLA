import os
import sys
import cairosvg

def pdf_to_svg(input_pdf, output_dir="svgs"):
    """
    将 PDF 文件转换为 SVG 文件（仅第一页）
    """
    if not os.path.exists(input_pdf):
        print(f"❌ 文件不存在: {input_pdf}")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_svg = os.path.join(output_dir, os.path.splitext(os.path.basename(input_pdf))[0] + ".svg")

    try:
        cairosvg.pdf2svg(url=input_pdf, write_to=output_svg)
        print(f"✅ 已生成: {output_svg}")
    except Exception as e:
        print("❌ 转换失败:", e)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python pdf_to_svg.py input.pdf [output_dir]")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "svgs"

    pdf_to_svg(input_pdf, output_dir)

