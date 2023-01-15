FROM 10.11.3.8:5000/bitahub/pytorch:1.6-py3

RUN apt -y install zip && \
    pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple  opencv-python addict terminaltables yapf imagecorruptions Pillow 
