# -*- coding: utf-8 -*-

def extract_left_channel_data(input_file, output_file):
    left_data = []
    with open(input_file, "r", encoding="utf-8") as fin:
        for line in fin:
            if "Left channel:" in line:
                # ��ȡ16λ��Ƶ����
                parts = line.strip().split("Left channel:")
                if len(parts) > 1:
                    hex_data = parts[1].strip()
                    # ֻ�����Ϸ���16��������ͨ��Ϊ4��8λ��
                    if len(hex_data) == 8 or len(hex_data) == 4:
                        left_data.append(hex_data)
                    else:
                        # ����ʽΪ '0000fe4f' ������������
                        left_data.append(hex_data)
    # �ÿո����Ӳ�д���ļ�
    with open(output_file, "w", encoding="utf-8") as fout:
        fout.write(" ".join(left_data))

if __name__ == "__main__":
    extract_left_channel_data("0524_1402_i2s.txt", "left_channel_data.txt")