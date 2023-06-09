# OWSAP-ZAP-with-pyQt
![UI img](https://github.com/Dino65535/OWSAP-ZAP-with-pyQt/blob/f41fb6b7120b6caa069c1c81010a5d7429a9b1af/img/UI.png "UI Window")
![Search img](https://github.com/Dino65535/OWSAP-ZAP-with-pyQt/blob/f41fb6b7120b6caa069c1c81010a5d7429a9b1af/img/CWE_Search.png "Search Window")

### 環境
    Python               : 3.11.2
    pyQt5                : 5.15.9
    OWASP ZAP Python API : 2.4
    OWASP ZAP            : 2.12.0
* [OWASP ZAP](https://www.zaproxy.org/download/)
* [PyQt5](https://pypi.org/project/PyQt5/) (pip install PyQt5)
* [zap-python-api](https://github.com/zaproxy/zap-api-python) (pip install python-owasp-zap-v2.4)
* 使用 [Qt Designer](https://build-system.fman.io/qt-designer-download) 編輯 (單純使用的話不需下載)

### 首次設定
* 將 ZAP 打開並把 ZAP Proixes Prot 改成 `8180` ， API Key 改成 `changeme` (或在 controller.py 裡將相關參數設定成自己環境的)
![Config img](https://github.com/Dino65535/OWSAP-ZAP-with-pyQt/blob/eb5dad03339d14adc081e34e7412490b1953abc0/img/config.png "Config")

### 檔案說明
* `.ui` 是用 Qt Designer 設計完 UI 的檔案，然後透過 pyQt5 轉成 `.py`
* `main_window.py` 是主畫面視窗，`search_window.py` 是搜尋畫面視窗
* `controller.py` 則是負責邏輯操作部分

## 使用說明
* 在 Target URL 輸入想要掃描的目標網址，按下 `Scan` 開始掃描，掃描完後將自動顯示 Alert Summary。
* `Report` 可以匯出詳細報告，並在左側視窗顯示
* `Clear` 可以清除網址，`Delete` 可以清除 Alert

## 隨便寫寫的小東西
* 不防呆 所以亂按可能有bug(?
* 由於換了專題題目的研究主題，所以應該不會在繼續更新

## 已知 Bug
* 不同裝置(解析度)上字體顯示可能會出錯 
