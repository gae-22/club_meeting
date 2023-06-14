# MMA-MEETING

これは部会を楽にしようという部長のめんどくさい精神から生まれた web アプリです．

以下の機能があります．ほぼ Wiki からの引用．

-   今年度のすべての議題
-   直近の部会の議題
-   投票用の GoogleForm
-   部会の開催予定日時，教室

pipenv を用いて仮想環境を構築し，Flask を用いて web アプリの練習のついでに作成した．Wiki からの Scraping には BeautifulSoup を用いた．

# Installation

## 1. Clone this repository

このリポジトリをクローンする．

```
git clone ssh://git@gitlab.mma.club.uec.ac.jp:2223/gae/mma-meeting.git
```

## 2. Install packages

Pipfile があるので，以下のコマンドでインストールできる．

```
pipenv sync
```

## 3. Web サーバーの起動

以下のコマンドで起動する．

```
pipenv shell
python server.py
```
