# 42Tokyoでよく使われるUbuntu 22.04をベースにする
FROM ubuntu:22.04

# パッケージのアップデートと、必要なツールのインストール
# (C言語コンパイラ、Make、Vim、Git、Pythonなどを一括で入れます)
RUN apt-get update && apt-get install -y \
    build-essential \
    clang \
    vim \
    git \
    python3 \
    python3-pip

# 42Tokyo独自のコーディング規約チェックツール「Norminette」をインストール
RUN pip3 install norminette

# コンテナに入った時の初期位置を設定
WORKDIR /workspace
