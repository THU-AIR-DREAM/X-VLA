#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess

def convert_svg_to_png(root_dir, dpi=300):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.lower().endswith(".svg"):
                svg_path = os.path.join(dirpath, filename)
                png_path = os.path.splitext(svg_path)[0] + ".png"
                try:
                    subprocess.run(
                        ["rsvg-convert", "-d", str(dpi), "-p", str(dpi), svg_path, "-o", png_path],
                        check=True
                    )
                    print(f"✅ 已转换: {svg_path} → {png_path}")
                except subprocess.CalledProcessError as e:
                    print(f"❌ 转换失败: {svg_path}\n   错误: {e}")

if __name__ == "__main__":
    target_dir = input("请输入要转换的目录路径（默认当前目录）: ").strip() or "."
    convert_svg_to_png(target_dir)
    print("\n🎉 全部转换完成！")
