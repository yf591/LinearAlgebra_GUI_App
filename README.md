# 行列計算用デスクトップアプリ

行列の基本的な演算をGUIで実行できるPythonアプリです。
行列のサイズを2x2から10x10まで選択でき、各種の行列計算とその解説を確認できます。

## 主な機能

- 行列サイズの選択（2x2 ～ 10x10）
- 以下の行列演算に対応:
  - 行列式
  - 逆行列
  - 対角化（固有値・固有ベクトル）
  - LU分解
  - QR分解
  - 特異値分解（SVD）
- 各演算結果に数学的な解説と応用例を表示
- 入力値の妥当性チェック機能

## インストール方法

1. リポジトリのクローン:
```bash
git clone https://github.com/yf591/LinearAlgebra_GUI_App.git
cd LinearAlgebra_GUI_App
```

2. 必要な依存関係をインストールします。
```bash
pip install -r requirements.txt
```

## 使用方法

アプリケーションを起動すると、行列のサイズを指定する入力フィールドが表示されます。行列サイズを入力し、行列の各値を入力した後、希望する行列演算を選択するとその結果が表示されます。

## 免責事項

このアプリケーションの使用によって生じたいかなる損害、損失、不利益などについて、開発者は一切の責任を負いません。自己責任でご使用ください。このアプリケーションは現状のまま提供され、いかなる保証もありません。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細については、LICENSEファイルを参照してください。
