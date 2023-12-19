#!/bin/bash

echo "##############################################################"
echo "現在のpoetry.lockから各環境用のrequirements.txtを出力します"
echo "##############################################################"
poetry export -f requirements.txt --output requirements.txt --without-hashes
echo "dev環境用パッケージの出力が完了..."
echo "エクスポートが正常に終了しました"
