# MMA-MEETING

これは部会を楽にしようという部長のめんどくさい精神から生まれた web アプリです．

以下の機能があります．ほぼ Wiki からの引用．

-   今年度のすべての議題
-   直近の部会の議題
-   投票用の GoogleForm へのリンク，パスワード
-   部会の開催予定日時，教室

その他にも，`gas`を用いて，GoogleForm を自動で作成しています．

# Installation

## 1. Clone this repository

このリポジトリをクローンする．

```
git clone ssh://git@gitlab.mma.club.uec.ac.jp:2223/gae/mma-meeting.git
```

## 2. Install packages

Pipfile.lock があるので，以下のコマンドでインストールできる．

```
pipenv sync
```

## 3. Start the virtual environment

```
pipenv shell
```

## 4. Run the server

起動自体は以下のコマンドで行う．しかし，実際に動かすためには，`wiki`のユーザーやスプレッドシート編集用の`json`などの設定が必要になる．
今回は`datas`ディレクトリを設定ファイル保管場所にした．設定の方法はネットのいろんなところに書いてあるので，そちらを参照してください．

```
python server.py
```

### 参考

[Flask](https://msiz07-flask-docs-ja.readthedocs.io/ja/latest/)  
[ログインのいるサイトからのスクレイピング](https://zenn.dev/mamekko/articles/ea44fe8a77da7c)  
[Python で SpreadSheet を編集する](https://zenn.dev/eito_blog/articles/02c132bbc1c4bd)  
[Python でファイルの読み書き](https://zenn.dev/makio/articles/66e7e24d7c4478)
