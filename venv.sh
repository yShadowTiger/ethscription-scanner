#!/bin/sh
python -m venv venv && \
source venv/bin/activate && \
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -U pip && \
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -U setuptools && \
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -U wheel && \
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

