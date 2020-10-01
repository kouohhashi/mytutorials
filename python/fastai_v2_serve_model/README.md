# fastai v2で学習させたモデルの公開

## ステップ1  
export.pklをmodelsディレクトリに配置  
学習の手順は下記チュートリアルを参考にしてください。
https://github.com/fastai/fastbook/blob/master/02_production.ipynb

## ステップ2
python test_api_v2.py で簡易ウェブサーバーを起動。  
ポート番号8000で起動します。  
http://127.0.0.1:8000/classify-url?url=https://images-na.ssl-images-amazon.com/images/I/51YBi4WPGuL.jpg
