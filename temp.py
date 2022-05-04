import paddlehub as hub
from pathlib import Path

paths = [str(i) for i in Path('.').glob('*.png')]  # 当前路径下所有.jpg文件
human_seg = hub.Module(name='deeplabv3p_xception65_humanseg')
results = human_seg.segmentation(paths=paths, visualization=True, output_dir='output')
# results = human_seg.segmentation(paths=paths, use_gpu=True, visualization=True, output_dir='output')  # 使用GPU
print(results)
