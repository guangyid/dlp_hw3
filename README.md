# dlp_hw3

paper of tinaface: translate,reproduce&amp;change

1. report文件夹是与工程无关的，其中的log文件是训练时生成的loss文件，graph.ipynb是根据
这些log文件生成可视化loss曲线的,jpg2lmdb.ipynb是转化数据集为lmdb格式时使用的。
2. eval tools文件夹是WIDERFace数据集评估PR曲线的matlab程序
3. 其余文件夹均与训练相关

## Introduction

git clone from https://github.com/Media-Smart/vedadet
vedadet is a single stage object detector toolbox based on PyTorch.

### Requirements

- Linux
- Python 3.7+
- PyTorch 1.6.0 or higher
- CUDA 10.2 or higher

We have tested the following versions of OS and softwares:

- OS: Ubuntu 16.04.6 LTS
- CUDA: 10.2
- PyTorch 1.6.0
- Python 3.8.5

### Install vedadet

a. Create a conda virtual environment and activate it.

```shell

conda create -n vedadet python=3.8.5 -y

conda activate vedadet

```

b. Install PyTorch and torchvision following the [official instructions](https://pytorch.org/), *e.g.*,

```shell

conda install pytorch torchvision -c pytorch

```

c. Clone the vedadet repository.

```shell

git clone https://github.com/Media-Smart/vedadet.git

cd vedadet

vedadet_root=${PWD}

```

d. Install vedadet.

```shell

pip install -r requirements/build.txt

pip install -v -e .

```

## Train

a. Config

Modify some configuration accordingly in the config file like `configs/trainval/retinanet/retinanet.py`

b. Multi-GPUs training

```shell

tools/dist_trainval.sh configs/trainval/retinanet/retinanet.py "0,1"

```

c. Single GPU training

```shell

CUDA_VISIBLE_DEVICES="0" python tools/trainval.py configs/trainval/retinanet/retinanet.py

```

d. Bitahub Order
```shell
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements/build.txt 
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -v -e . 
bash /code/tools/dist_trainval.sh /code/configs/trainval/tinaface/tinaface_r50_fpn_gn_dcn.py "0,1" --workdir=/output
```

## Test

a. Config

Modify some configuration accordingly in the config file like `configs/trainval/retinanet/retinanet.py`

b. Test

```shell

CUDA_VISIBLE_DEVICES="0" python tools/test.py configs/trainval/retinanet/retinanet.py weight_path

```

c.Bitahub
```shell
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements/build.txt 
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -v -e . 
python /code/configs/trainval/tinaface/test_widerface.py /code/configs/trainval/tinaface/tinaface_r50_fpn_gn_dcn.py '/model/guangyid/reproduce/repro_e105.pth' --outdir=/output/work
```