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


※ 使い方(google accountのエクスポート利用)
1. 環境に合わせて変数設定(constants.py)：OUTPUT_URL、GOOGLE_ACCOUNT_HISTORY_PATH
2. google accountのエクスポート利用して「BrowserHistory.json」出力、配置
3. chromeを閉じてpython3でgetFromBrowserHistory.py実行

※ シンボル
1. 覚えてない：'x'
2. 一回覚えたと思う：'1'
3. 覚えた：'o'
4. 間違った検索語：'-'

※ 重複チェック
・各グループ中で行う