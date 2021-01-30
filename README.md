<h1 align="center">Yutub Downloader</h1>

<p align="center">
  <img src="https://github.com/kurnyaannn/yutub-downloader/blob/master/yd-demo.gif?raw=true">
</p>

## Requirements
* python 3.8+
* pip
* pytube 10.4.1

## Config
> The default Dowload path is set to `$home/Downloads/Videos`. <br>

To change this you can simply configure the `file_path()` function
```python
def file_path():
    ...
    download_path = os.path.join(home, '$YOUR_PATH')
    ...
```

## Installation
* Clone this repository using `git clone` command (or just download the `zip` version).
* Install pytube using `pip`.
```bash
$ pip install pytube
```

## Usage
* On Project directory run
```bash
$ python yutub.py
```
* Copy & paste the YouTube URL

## License
As you can see Yutub Downloader is under MIT License

## About the Author
<a href="http://facebook.com/y21kurnia">Yayang Kurnia</a>.
