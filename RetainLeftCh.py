# -*- coding: utf-8 -*-

def extract_left_channel_data(input_file, output_file):
    left_data = []
    with open(input_file, "r", encoding="utf-8") as fin:
        for line in fin:
            if "Left channel:" in line:
                # 提取16位音频数据
                parts = line.strip().split("Left channel:")
                if len(parts) > 1:
                    hex_data = parts[1].strip()
                    # 只保留合法的16进制数（通常为4或8位）
                    if len(hex_data) == 8 or len(hex_data) == 4:
                        left_data.append(hex_data)
                    else:
                        # 若格式为 '0000fe4f' 这种正常长度
                        left_data.append(hex_data)
    # 用空格连接并写入文件
    with open(output_file, "w", encoding="utf-8") as fout:
        fout.write(" ".join(left_data))

if __name__ == "__main__":
    extract_left_channel_data("0524_1402_i2s.txt", "left_channel_data.txt")