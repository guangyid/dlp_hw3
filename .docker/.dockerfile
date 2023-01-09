FROM pytorch/pytorch:1.7.0-cuda11.0-cudnn8-runtime

RUN rm /etc/apt/sources.list.d/cuda.list /etc/apt/sources.list.d/nvidia-ml.list; \
    sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list && apt update && \
    apt -y install build-essential gcc g++ gdb binutils pciutils net-tools iputils-ping iproute2 git vim wget curl make openssh-server openssh-client tmux tree man unzip unrar nvidia-cuda-toolkit&& \
    pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple jupyterlab cython numpy addict terminaltables opencv-python yapf imagecorruptions mmpycocotools scipy scikit_image matplotlib networkx PyWavelets imageio tifffile pyparsing kiwisolver contourpy fonttools

ENV PATH=/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/nvidia/bin