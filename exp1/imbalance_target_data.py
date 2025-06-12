import random
from collections import defaultdict

def filter_images_custom_ratio(
    input_file, 
    output_file, 
    label_ratio_dict,  # 格式：{"9": 0.5, "20": 0.3}，表示标签9保留50%，标签20保留30%
    min_samples=1,     # 每个类别至少保留的样本数
    shuffle=True       # 是否打乱顺序
):
    """
    按照自定义的类别比例筛选数据
    
    参数:
        input_file: 输入文件路径
        output_file: 输出文件路径
        label_ratio_dict: 字典，指定每个标签的采样比例（如 {"9": 0.5, "20": 0.3}）
        min_samples: 每个类别至少保留的样本数（即使比例计算后少于该值）
        shuffle: 是否打乱输出顺序
    """
    # 1. 读取数据并按标签分类
    label_to_images = defaultdict(list)
    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                path, label = line.rsplit(' ', 1)
                label_to_images[label].append((path, label))
    
    # 2. 检查是否有未指定比例的标签
    all_labels = set(label_to_images.keys())
    specified_labels = set(label_ratio_dict.keys())
    unspecified_labels = all_labels - specified_labels
    
    if unspecified_labels:
        print(f"警告：以下标签未指定采样比例，将全部保留：{unspecified_labels}")
        for label in unspecified_labels:
            label_ratio_dict[label] = 1.0  # 默认全部保留
    
    # 3. 按比例筛选每个类别的数据
    selected_images = []
    for label, images in label_to_images.items():
        ratio = label_ratio_dict.get(label, 1.0)  # 默认1.0（全部保留）
        select_count = max(min_samples, int(len(images) * ratio))
        selected = random.sample(images, select_count)
        selected_images.extend(selected)
    
    # 4. 打乱顺序后写入文件（可选）
    if shuffle:
        random.shuffle(selected_images)
    
    with open(output_file, 'w') as f:
        for path, label in selected_images:
            f.write(f"{path} {label}\n")

# 使用示例
input_file = "./txt/target_webcam_opda.txt"  # 输入文件
output_file = "./txt/target_webcam_imbalance_opda.txt"  # 输出文件

# 定义每个类别的采样比例（标签: 比例）
label_ratio_dict = {str(i):0.1 for i in range(5, 10)}  # 标签5-9保留10%，其余默认全部保留

filter_images_custom_ratio(input_file, output_file, label_ratio_dict)
print(f"自定义比例筛选完成！结果保存至 {output_file}")