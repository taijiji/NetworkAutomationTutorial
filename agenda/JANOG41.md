# JANOG41
JApan Network Operators' Group: the largest conference for Network Operators in Japan
- https://www.janog.gr.jp/meeting/janog41/

# Title
## English
Let's get started Network Automation from tomorrow!

## Japanese
明日からはじめるネットワーク運用自動化

# Schedule
- Jan/25/2018 10:00-11:00JST
- 60 minites, include 10 minitues discussion time

# Abstruct
## English
Automation for infrastructure operation is getting desired from also network operation, as with server operation and software development.

However, Network Engineering Team is worried about some issues as follows;
- No people who can develop software in Network Engineering Team.
- No enough skill sets and knowledge to develop software for Automation.
- No support and understanding for Automation from the organization.

To get started to develop Network Automation from tomorrow, this presentation introduces some practical technique of programming, some useful library, and many sample codes.

I hope this presentation has taken you one step closer to improve your network operation work.

## Japanese
インフラ運用の自動化は、アプリケーション開発やサーバ運用だけでなく、
ネットワーク運用現場においても求められるようになってきました。  
しかし実際のネットワーク運用現場からは  
「開発ができる人材がいない」  
「自動化開発のための知識やスキルセットが不足している」  
「自動化に対する組織の理解/サポートが足りない」  
といった様々な悩みの声が聞こえてきます。  
本発表では、ネットワークエンジニアが「明日から自動化開発をはじめる」ために、具体的なプログラミングテクニックや
開発に役立つOSSライブラリ、サンプルコードを共有することで、皆様の職場のネットワーク運用業務を改善するきっかけに
していただきたいです。

# Target Audience
## Engilish
- People who interested in development for Network Automation.
- Network Engineer, or Beginner at programming
- Executive or Team Leader who consider for tackling Network Automation as a business issue.

## Japanese
- ネットワーク運用の自動化開発に興味のある方、挑戦してみたい方
- 開発経験の無いネットワークエンジニアの方、プログラミング初心者の方 
  (ただし発表時間の都合上、プログラミング基礎解説は最小限に留めます)
- 経営課題としてネットワーク運用自動化に取り組むべきか悩んでいる運用リーダーの方、管理職の方

# Table of Contents
## English
- Trends of Automation for Infrastructure Automation
- Case studies of Network Automation
- How to fail at Network Automation
- Why Python?
- Python Tutorial
  - Variables
    - Number
    - String
    - list
    - dictionary
  - If
  - For
  - Function
  - Class
  - File read/write
  - Use library
  - UnitTest
  - JSON
  - Template Engine
  - Regular Expression
- Try writing a code of Network Automation
  - Login a router from program
  - Extract the result of "show command" using a regular expression.
  - Configure a router from program
- Open Sourced Library for Network Automation
  - Vendor official library
  - Third party library
- Sample code for Network Automation: BGP Peering


## Japanese
本発表では、プログラミング言語としてPython(3系)を例にして進めます。
- インフラ自動化のトレンド
- ネットワーク運用自動化の事例
- ネットワーク運用自動化 失敗パターン
- なぜPython?
- Python入門 おさらい
  - 変数
    - 数値型
    - 文字列型
    - リスト型
    - 辞書型
- if: 条件分岐処理
- for: 繰り返し処理
- 関数
- クラス
- ファイル入出力
- テスト
- ライブラリの利用
- JSONの利用
- やってみようネットワーク自動化
  - プログラムからルータにログイン
  - showコマンド結果を正規表現で抽出
  - プログラムからルータにコンフィグ投入
- 開発に便利なOSSライブラリ/ツールの紹介
  - メーカー公式ライブラリ
  - サードパーティライブラリ
- 自動化サンプルコード: BGP Peering作業を自動化する

# Time Management
- 自己紹介(1min)
- インフラ自動化のトレンド(1min)
- ネットワーク運用現場での声(1min)
- 本発表のねらい(1min)
- ネットワーク運用自動化の事例(3min)
- ネットワーク運用自動化 失敗パターン(2min)
- なぜPython?(1min)  
- --- 10 min have passed ----

- Python入門 おさらい(total 10min)
  - 変数 (2分)
   - 数値型
   - 文字列型
   - リスト型
   - 辞書型
  - if文(1min)
  - for文(1min)
  - 関数(1min)
  - クラス(1min)
  - ファイル入出力(1min)
  - json(1min)
  - テンプレートエンジン(3min)
- --- 20 min have passed ----

- やってみようネットワーク自動化(total 10min)
  - プログラムからルータにログイン(3min)
  - showコマンド結果を正規表現で抽出(3min)
  - プログラムからルータにコンフィグ投入(4min)
- --- 30 min have passed ----

- 開発に便利なOSSライブラリ/ツールの紹介(total 11min)
  - メーカー公式ライブラリ(3min)
  - サードパーティライブラリ
    - NAPALM(3min)
    - Textfm(3min)
    - Ansible(2min)
- --- 41 min have passed ----

- 自動化サンプルコード: BGP Peering作業を自動化する(total 6min)
  - demo (2min)
- --- 47 min have passed ----

- (TBD)検証環境の構築 (total 3min)
- --- 50 min have passed ----

- Q&A, discussion (total 10min)
- --- 60 min have passed ----

# TODO
- p2「インフラ運用への要望」
  - 課題のリストアップは妥当か
  - 図にする(best effort)
- p3「ネットワーク運用現場の声」
  - 図にする
- p4「本発表のねらい」
  - 図にする
  - 改善のアプローチまで記載する
- p4「ネットワーク運用自動化の事例」
  - 抽象的なので、表現をブラッシュアップ
  - できればすべてに参考文献を追加したい。
- 質疑応答の対応
 - なぜPythonを覚える必要があるのか
   pythonを覚えずに自動化する手段は無いのか
   - ネットワーク設定に限れば、Ansible/CiscoNSOでもプログラミングなしである程度は行ける。
  - 自動化したい項目が増えてきたときに、プログラムを書かざるをえない部分がでてくる
  　- 構成管理の自動化。データ取得部分
    - 既存ルータでは実現できない機能の追加
    - 回線運用のLSP コントロール等
 - Ansibleなら、プログラミング書かずに実現できるのでは？
  - あとAnsibleでもできないことは多い。
  - TODO: リストアップ
