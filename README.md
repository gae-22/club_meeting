# MMA-MEETING

これは部会を楽にしようという部長のめんどくさい精神から生まれた web アプリです．

以下の機能があります．ほぼ Wiki からの引用．

-   今年度のすべての議題
-   直近の部会の議題
-   投票用の GoogleForm へのリンク，パスワード
-   部会の開催予定日時，教室

その他にも，`gas`を用いて，GoogleFormを自動で作成しています．

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
```
python server.py
```
