#!/usr/bin/env python
# encoding: utf-8

from prettytable import PrettyTable

region_dict = {
    '艾欧尼亚': 'dx1',
    '祖安': 'dx2',
    '诺克萨斯': 'dx3',
    '班德尔城': 'dx4',
    '皮尔特沃夫': 'dx5',
    '战争学院': 'dx6',
    '巨神峰': 'dx7',
    '雷瑟守备': 'dx8',
    '裁决之地': 'dx9',
    '黑色玫瑰': 'dx10',
    '暗影岛': 'dx11',
    '钢铁烈阳': 'dx12',
    '均衡教派': 'dx13',
    '水晶之痕': 'dx14',
    '影流': 'dx15',
    '守望之海': 'dx16',
    '征服之海': 'dx17',
    '卡拉曼达': 'dx18',
    '皮城警备': 'dx19',
    '比尔吉沃特': 'wt1',
    '德玛西亚': 'wt2',
    '弗雷尔卓德': 'wt3',
    '无畏先锋': 'wt4',
    '恕瑞玛': 'wt5',
    '扭曲丛林': 'wt6',
    '巨龙之巢': 'wt7',
    '教育网专区': 'jy1',
}

dan_dict = {
    '全部': 'all',
    '王者': 'challenger',
    '大师': 'master',
    '钻石': 'diamond',
    '铂金': 'platinum',
    '黄金': 'gold',
    '白银': 'silver',
    '青铜': 'bronze',
}


def make_chart(field_names, fields):
    x = PrettyTable()

    x._set_field_names(field_names)

    for field in fields:
        x.add_row(field)

    return x


def make_player_chart(player_info):
    field_names = ['玩家名称', '段位', '胜点', '最后登录时间', '擅长英雄', 'KDA/击杀/死亡/助攻', '上单/打野/中单/ADC/辅助', '三杀/四杀/五杀', '胜率']

    x = PrettyTable()
    x._set_field_names(field_names)

    x.add_row([
        player_info['name'],
        player_info['tier'],
        player_info['league_points'],
        player_info['last_modified'],
        player_info['champion_performance_list'],
        player_info['kda'],
        player_info['stat_position'],
        player_info['best_kill'],
        player_info['average_win_rate'],
    ])

    recent_game = PrettyTable()
    recent_game._set_field_names(['英雄', '开始时间', '模式', 'MVP', '胜负'])

    for game in player_info['game_recent_list']:
        recent_game.add_row([
            game['champion'],
            game['created'],
            game['game_type'],
            game['mvp'],
            game['battle_result'],
        ])
        
    return x, recent_game































