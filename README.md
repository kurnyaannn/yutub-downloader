<h1 align="center">Yutub Downloader</h1>

<p align="center">
  <img src="https://github.com/kurnyaannn/yutub-downloader/blob/master/yd-demo.gif?raw=true">
</p>

## Requirements
* python 3.8+
* pip
* pytube 10.4.1

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

## Config
* Download Path
  > The default Dowload path is set to `$home/Downloads/Videos`. <br>

  To change this you can simply configure the `file_path()` function
  ```python
  def file_path():
      ...
      download_path = os.path.join(home, '$YOUR_PATH')
      ...
  ```
* Tips <br>
  Make an alias in your shell / bash to make it more flexible, for example in my zsh
  ```bash
  #! $home/.zshrc
  alias your-alias="python /dir/to/this/project/yutub.py"
  ```
  Restart the shell and run
  ```bash
  $ your-alias
  ```

## License
As you can see Yutub Downloader is under MIT License

## About the Author
<a href="http://facebook.com/y21kurnia">Yayang Kurnia</a>.
