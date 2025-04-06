import os
import shutil
import random
from pathlib import Path

# Paths
SOURCE_DIR = "C:/Users/adity/Downloads/archive (15)/The IQ-OTHNCCD lung cancer dataset/The IQ-OTHNCCD lung cancer dataset"         # Your original dataset folder
DEST_DIR = "C:/Users/adity/Downloads/split_dataset"     # Where train/test folders will be created
SPLIT_RATIO = 0.8              # 80% train, 20% test
SEED = 42

random.seed(SEED)

# Prepare train/test directories
for subset in ["train", "test"]:
    subset_path = Path(DEST_DIR) / subset
    subset_path.mkdir(parents=True, exist_ok=True)

# Iterate over each class folder
for class_name in os.listdir(SOURCE_DIR):
    class_path = Path(SOURCE_DIR) / class_name
    if not class_path.is_dir():
        continue

    images = list(class_path.iterdir())
    random.shuffle(images)

    split_idx = int(len(images) * SPLIT_RATIO)
    train_imgs = images[:split_idx]
    test_imgs = images[split_idx:]

    for subset, subset_imgs in [("train", train_imgs), ("test", test_imgs)]:
        subset_class_dir = Path(DEST_DIR) / subset / class_name
        subset_class_dir.mkdir(parents=True, exist_ok=True)

        for img_path in subset_imgs:
            shutil.copy2(img_path, subset_class_dir)

print("✅ Dataset split complete. Check the 'split_dataset/train' and 'split_dataset/test' folders.")
