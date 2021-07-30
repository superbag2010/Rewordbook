# Rewordbook
create book of reviewing searched word:scrape dictionary search history using chrome history and export to CSV file

【概要】 
chrome履歴から日本語辞書の検索記録をスクレイピング
---

※　設計書管理
https://drive.google.com/drive/folders/1GgTkHDIJzjyVhHrT_bgQikksEt7q1gCQ?usp=sharing


※ 注意事項
・実行の時、ブラウザを終了しないとDBロックエラー発生。
⇒Chromeブラウザを終了しないとSQLiteで管理される履歴がロックされてる為、履歴を取得できない。


※ 使い方
1. 環境に合わせて変数設定(constants.py)
2. 必要プログラム
 - python3, plyvel(https://github.com/happynear/py-leveldb-windows)
 - windows
 - chrome
3. chromeを閉じてpython3でmain.py実行

TODO
１．削除モード
２．バッチ
３．FROM PLUGIN？SQLITE？
４．リンク遷移 with One click:GOOGLESPREADSHEET？
