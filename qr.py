import pyqrcode
url="https://www.linkedin.com/in/priya-parthasarthi-a5429b257/"
k=pyqrcode.create(url)
k.svg('Qr.svg',scale=10)