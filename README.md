# lolqy

A very simple terminal tool about LOL CN player's information query.

##Install

```
pip install lolqy
```

## Usage

```
Usage: lolqy [OPTIONS] COMMAND [ARGS]...

Options:
  -r, --region TEXT  LOL region name
  -p, --page TEXT    Page
  -n, --name TEXT    Player name
  -d, --dan TEXT     Dan
  --help             Show this message and exit.

Commands:
  hero
  player
  rank
```

```
lolqy -r 艾欧尼亚 rank                      # query 艾欧尼亚 rank list
lolqy -r 艾欧尼亚 -p 2 rank                 # query page 2 
lolqy -r 艾欧尼亚 -n 战旗看毒纪直播  player # query player information
lolqy -r 艾欧尼亚 -d 全部 hero              # query favorite hero
```

## PS

Only support these regions:
* 艾欧尼亚
* 祖安
* 诺克萨斯
* 班德尔城
* 皮尔特沃夫
* 战争学院
* 巨神峰
* 雷瑟守备
* 裁决之地
* 黑色玫瑰
* 暗影岛
* 钢铁烈阳
* 均衡教派
* 水晶之痕
* 影流
* 守望之海
* 征服之海
* 卡拉曼达
* 皮城警备
* 比尔吉沃特
* 德玛西亚
* 弗雷尔卓德
* 无畏先锋
* 恕瑞玛
* 扭曲丛林
* 巨龙之巢
* 教育网专区

 
Only support these dans:
* 全部
* 王者
* 大师
* 钻石
* 铂金
* 黄金
* 白银
* 青铜
