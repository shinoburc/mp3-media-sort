LEVIN X26 MP3 Player Sort
===================

## About

LEVIN X26 という安い MP3 Player を買って、Blutooth イヤホンが使えたり、SD カードで容量拡張できたり、
音質も申し分ないのだけれども、何をお考えなのか mp3 リストの「ソート機能」がないということに衝撃を受けました。

mp3 リストはどうも本体に書き込んだ順で表示されているようです。このプロダクトを世に出すことに誰も異を唱えなかったのでしょうか。

それでこんなことになりました。

これは LEVIN X26 から全ての mp3 ファイルを取り出し、ソートして書き戻すプログラムです。

ありがとうございました。

たぶん、同様の機器にも使えるはずです。

## Setup

```sh
$ git clone git@github.com:shinoburc/mp3-media-sort.git
$ cd mp3-media-sort
$ python sort.py <LEVIN-X26-MOUNT-POINT-DIRECTORY> <TEMPORARY-DIRECTORY>
```

example

```sh
$ python sort.py /media/dot/X26/ ./tmp
```

OMG
