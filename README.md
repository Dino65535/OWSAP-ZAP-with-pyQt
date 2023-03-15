# OWSAP-ZAP-with-pyQt
寫一個簡單的UI來操作ZAP  
![UI img](https://github.com/Dino65535/OWSAP-ZAP-with-pyQt/blob/eb5dad03339d14adc081e34e7412490b1953abc0/img/UI.png "UI")

### 環境
    Python               : 3.11.2
    pyQt5                : 5.15.9
    OWASP ZAP Python API : 2.4
    OWASP ZAP            : 2.12.0
* [PyQt5](https://pypi.org/project/PyQt5/) (pip install PyQt5)
* [zap-python-api](https://github.com/zaproxy/zap-api-python) (pip install python-owasp-zap-v2.4)
* 使用 [Qt Designer](https://build-system.fman.io/qt-designer-download) 編輯 (單純使用不需下載)

### 首次設定
* 將 ZAP 打開並把 ZAP Proixes Prot 改成 `8180` ， API Key 改成 `changeme` (或在 controller.py 裡將相關參數設定成自己環境的)
![Config img](https://github.com/Dino65535/OWSAP-ZAP-with-pyQt/blob/eb5dad03339d14adc081e34e7412490b1953abc0/img/config.png "Config")

### 檔案說明
* `pyqt.ui` 是用 Qt Designer 設計完UI的檔案，然後透過 pyQt5 轉成 `UI.py`
* `controller.py` 則是負責邏輯操作部分

## 使用說明
* 在 Target URL 輸入想要掃描的目標網址，按下 `Scan` 開始掃描，掃描完後將自動顯示 Alert Summary。
* `Report` 可以匯出詳細報告，並在左側視窗顯示
* `Clear` 可以清除網址，`Delete` 可以清除 Alert

## Test
* 大概這樣 之後有想到或有新功能再補充
* 目前不防呆 所以亂按可能有bug(?
