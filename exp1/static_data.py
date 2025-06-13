from collections import defaultdict

def count_labels(file_path):
    # 使用defaultdict来统计标签数量
    label_counts = defaultdict(int)
    
    with open(file_path, 'r') as file:
        for line in file:
            # 分割每行，获取标签（最后一个元素）
            parts = line.strip().split()
            if len(parts) < 2:
                continue  # 跳过格式不正确的行
            label = parts[-1]
            label_counts[label] += 1
    
    return dict(label_counts)

# 使用示例
# file_path = './txt/target_amazon_opda.txt'  # 替换为你的文件路径
file_path = './txt/target_webcam_imbalance_opda.txt'
label_counts = count_labels(file_path)

# 打印统计结果
print("标签统计结果：")
for label, count in sorted(label_counts.items(), key=lambda x: int(x[0])):
    print(f"标签 {label}: {count}")

# 打印总计
print(f"\n总计: {sum(label_counts.values())} 张图片")