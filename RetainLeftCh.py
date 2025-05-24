# -*- coding: utf-8 -*-
# 该脚本读取0524_1402_i2s.txt文件，只保留左声道（Left channel）数据，并保存到新文件left_channel.txt

input_file = "0524_1402_i2s.txt"
output_file = "left_channel.txt"

with open(input_file, "r", encoding="utf-8") as fin, open(output_file, "w", encoding="utf-8") as fout:
    for line in fin:
        if "Left channel:" in line:
            fout.write(line)