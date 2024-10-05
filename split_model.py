def split_file(file_path, chunk_size):
    """
    分割大文件为多个小文件
    :param file_path: 原始文件路径
    :param chunk_size: 每个分块的大小（字节）
    """
    with open(file_path, 'rb') as f:
        chunk_count = 0
        while True:
            # 读取文件块
            chunk = f.read(chunk_size)
            if not chunk:
                break
            # 将每个块保存为新的文件
            with open(f'{file_path}.part{chunk_count}', 'wb') as chunk_file:
                chunk_file.write(chunk)
            chunk_count += 1
    print(f'文件分割完成，总共分为 {chunk_count} 个部分。')

# 使用例子
split_file('./sam_vit_h_4b8939.pth', 1900 * 1024 * 1024)  # 将文件分割为 1900MB 的块
