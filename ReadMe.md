﻿# このソフトウェアについて

PySDL2でTextEntryを表示する。

`TEXTENTRY`は、いわゆるテキストボックス。

# 開発環境

* Linux Mint 17.3 MATE 32bit
* [SDL2](http://ytyaru.hatenablog.com/entry/2018/12/09/000000) 2.0.2
* [pyenv](https://github.com/pylangstudy/201705/blob/master/27/Python%E5%AD%A6%E7%BF%92%E7%92%B0%E5%A2%83%E3%82%92%E7%94%A8%E6%84%8F%E3%81%99%E3%82%8B.md) 1.0.10
    * Python 3.6.1
        * [PySDL2](http://ytyaru.hatenablog.com/entry/2018/12/10/000000) 0.9.6
        
# 参考

* [http://pysdl2.readthedocs.io/en/rel_0_9_4/modules/sdl2ext_gui.html]

# 論外

`TEXTENTRY`は以下の問題点によりまったく使えない。これはひどい。

* そもそも文字列が表示されない
* IMEが無効になり日本語変換できない

テキスト入力としての最低限の機能すら満たせていない。
    
# 実行

```sh
$ python 1.py
```

![画像](https://cdn-ak.f.st-hatena.com/images/fotolife/y/ytyaru/20171121/20171121131741.png)

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

利用ライブラリのライセンスは以下。

Library|License|Copyright
-------|-------|---------
[SDL2](https://www.libsdl.org/license.php)|zlib|[github](https://github.com/letoram/SDL2/blob/master/debian/copyright)
[PySDL2](https://pysdl2.readthedocs.io/en/rel_0_9_6/)|[CC0](http://pysdl2.readthedocs.io/en/rel_0_9_4/copying.html)|[Copyright (C) 2012-2014 Marcus von Appen  marcus@sysfault.org](http://pysdl2.readthedocs.io/en/rel_0_9_4/copying.html)

