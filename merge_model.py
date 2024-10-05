def merge_files(output_file, part_files):
    """
    将多个分割的文件合并为一个文件
    :param output_file: 合并后的文件路径
    :param part_files: 分割文件的列表，按顺序排列
    """
    with open(output_file, 'wb') as f:
        for part_file in part_files:
            with open(part_file, 'rb') as pf:
                f.write(pf.read())
    print(f'文件合并完成，已生成 {output_file}.')

# 使用例子
part_files = ['./sam_vit_h_4b8939.pth.part0', './sam_vit_h_4b8939.pth.part1']  # 按顺序列出所有分割文件
merge_files('merged_sam_vit_h_4b8939.pth', part_files)
