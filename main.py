import requests
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Referer": "http://www.google.com/"
        }
        self.setup()

    def setup(self):
        self.setWindowTitle("My Qt App")

        title = QLabel("Welcome to Newscraper! Insert your URl Below.")

        self.url_input = QLineEdit("https://www.reuters.com/world/global-hunger-crisis-deepens-major-nations-skimp-aid-2024-12-24/")
        button = QPushButton("Scrape")
        button.clicked.connect(self.scrape)

        master = QVBoxLayout()

        row1 = QHBoxLayout()
        row2 = QHBoxLayout()

        row1.addWidget(title)
        row2.addWidget(self.url_input)
        row2.addWidget(button)

        master.addLayout(row1)
        master.addLayout(row2)

        self.setLayout(master)

    def scrape(self):
        url = self.url_input.text()
        file = open("Export.txt", "w")
        r = requests.get(url=url, headers=self.headers)
        soup = BeautifulSoup(r.text, "html.parser")
        content = soup.findAll("div", attrs={"class": "text__text__1FZLe text__dark-grey__3Ml43 text__regular__2N1Xr text__small__1kGq2 body__full_width__ekUdw body__small_body__2vQyf article-body__paragraph__2-BtD"})
        for para in content:
            # file.write(title.text + "\n")
            file.write(para.text)
            file.write("\n \n")

        file.close()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
