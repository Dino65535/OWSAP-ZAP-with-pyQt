# OWSAP-ZAP-with-pyQt
寫一個簡單的UI來操作ZAP

## 環境
    Python    : 3.11.2
    pyQt5     : 5.15.9
    OWASP ZAP : 2.12.0
* [pyQt5](https://pypi.org/project/PyQt5/) 安裝 :: pip install PyQt5
* 使用 [Qt Designer](https://build-system.fman.io/qt-designer-download) 編輯

## 首次設定
* 將 ZAP Proixes Prot 改成 `8180` ， API Key 改成 `changeme` (或在 controller.py 裡將相關參數設定成自己環境的)

## 使用說明
* 在 Target URL 輸入想要掃描的目標網址，按下 `Scan` 開始掃描，掃描完後將自動顯示 Alert Summary。
* `Report` 可以匯出詳細報告，並在左側視窗顯示
* `Clear` 可以清除網址，Delete 可以清除 `Alert`

## Test
* 大概這樣 之後有想到或有新功能再補充
* 目前不防呆 所以亂按可能有bug(?
