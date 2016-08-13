#!/usr/bin/env python
# encoding: utf-8

import requests
import json
import sys
import urllib
from utils import region_dict, dan_dict

reload(sys)
sys.setdefaultencoding('utf-8')

__author__ = "corazon"


DATA_NONE_MSG= 'There is empty to display.'
TIMEOUT_MSG = 'Network timeout, please try once later.'


def fetch_rank(obj):
    try:
        reg = region_dict[obj['REGION']]
    except KeyError, e:
        msg = "Please input correct region!"
        return 'error', msg

    url = 'http://api.lolbox.duowan.com/api/v2/rank/ranked/' + reg + '/'

    params = {
        'page_num': obj['PAGE'],
        'page_items': '20',
    }

    headers = {
        'Referer': 'http://lolbox.duowan.com/frontend/rankScoreRank.html',
        'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    }
    try:
        rep = requests.get(url, headers=headers, params=params, timeout=5)
    except Exception, e:
        msg = TIMEOUT_MSG
        return 'error', msg

    if rep.status_code == 200:
        res = json.loads(rep.content)['results']
        rank_list = []

        for player in res:
            rank_list.append([
                player['idx'],
                player['player']['pn'],
                player['player']['game_zone']['alias'],
                player['player']['tier_rank']['tier']['full_name_cn'],
                player['player']['league_points'],
                player['player']['box_score'],
            ])

        return 'success', rank_list
    else:
        msg = DATA_NONE_MSG
        return 'error', msg


def fetch_hero_rank(obj):
    try:
        dan = dan_dict[obj['DAN']]
    except KeyError, e:
        msg = 'Please input correct dan!'
        return 'error', msg

    url = 'http://api.lolbox.duowan.com/api/v2/rank/champion_present_rate/' + dan + '/'
    headers = {
        'Referer': 'http://lolbox.duowan.com/frontend/championRank.html',
        'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }

    try:
        rep = requests.get(url, headers=headers, timeout=5)
    except Exception, e:
        msg = TIMEOUT_MSG
        return 'error', msg

    if rep.status_code == 200:
        res = json.loads(rep.content)['results']
        hero_rank_list = []

        for hero in res:
            hero_rank_list.append([
                hero['idx'],
                hero['champion_present_rate']['champion']['display_name'],
                str(hero['champion_present_rate']['present_rate']) + '%',
                str(hero['champion_present_rate']['win_rate']) + '%',
                hero['champion_present_rate']['total_present'],
                hero['champion_present_rate']['champion']['positions'][0]['position_in_cn'],
                hero['champion_present_rate']['champion']['roles'][0]['role_in_cn'],
                hero['champion_present_rate']['champion']['roles'][0]['desc']
            ])

        return 'success', hero_rank_list
    else:
        msg = DATA_NONE_MSG
        return 'error', msg


def fetch_player(obj):
    try:
        reg = region_dict[obj['REGION']]
        player_name = obj['NAME']
        if player_name == '':
            msg = 'Please input player name!'
            return 'error', msg
    except KeyError, e:
        msg = "Please input corrent region!"
        return 'error', msg

    url = 'http://api.lolbox.duowan.com/api/v2/player/search/'
    headers = {
        'Referer': 'http://lolbox.duowan.com/frontend/playerList.html?' + urllib.urlencode({'sn': 'all','pn': player_name}),
        'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    }
    params = {
        'player_name_list': player_name
    }

    try:
        rep = requests.get(url, params=params, headers=headers)
    except Exception, e:
        msg = TIMEOUT_MSG
        return 'error', msg

    if rep.status_code == 200:
        player_list = json.loads(rep.content)['player_list']

        user_info = dict()
        for player in player_list:
            if player['game_zone']['alias'] == obj['REGION']:
                user_info['user_id'] = str(player['user_id'])
                user_info['server_name'] = player['game_zone']['server_name']
                user_info['game_zone'] = player['game_zone']['pinyin']
                user_info['player_name'] = player['pn']
                break

        if user_info:
            url = 'http://api.lolbox.duowan.com/api/v2/player/' + reg + '/' + user_info['user_id'] + '/'
            referer = urllib.urlencode({
                'serverName': user_info['server_name'],
                'playerName': user_info['player_name'],
                'userId': user_info['user_id'],
                'gameZone': user_info['game_zone'],
            })
            headers['Referer'] = 'http://lolbox.duowan.com/frontend/playerDetail.html?' + referer

            rep = requests.get(url, headers=headers)

            if rep.status_code == 200:
                player_info = json.loads(rep.content)['player_list'][0]

                game_recent_list = []

                for game in player_info['game_recent_list']:
                    game_recent_list.append({
                        'champion': game['champion']['display_name'],
                        'created': game['created'].replace('T', ' '),
                        'game_type': game['game_type']['name_cn'],
                        'mvp': game['flag_mvp_carry'],
                        'battle_result': '胜利' if game['battle_result'] else '失败',
                    })

                champion_performance_list = '/'.join([p['champion']['title'] for p in player_info['champion_performance_list']][:5])

                stat_position = '/'.join([
                    str(player_info['stat_position']['top']),
                    str(player_info['stat_position']['jungler']),
                    str(player_info['stat_position']['mid']),
                    str(player_info['stat_position']['adc']),
                    str(player_info['stat_position']['support']),
                ])

                best_kill = '/'.join([
                    str(player_info['stat_kda']['triple_kills']),
                    str(player_info['stat_kda']['quadra_kills']),
                    str(player_info['stat_kda']['penta_kills']),
                    # str(player_info['stat_kda']['best_kill']),
                ])

                kda = '/'.join([
                    str(player_info['stat_kda']['average_kda']),
                    str(player_info['stat_kda']['average_k']),
                    str(player_info['stat_kda']['average_d']),
                    str(player_info['stat_kda']['average_a']),
                ])

                player = {
                    'name': player_info['pn'],
                    'tier': player_info['tier_rank']['tier']['name_cn'],
                    'league_points': player_info['tier_rank']['league_points'],
                    'last_modified': player_info['last_modified'].replace('T', ' '),
                    'champion_performance_list': champion_performance_list,
                    'kda': kda,
                    'stat_position': stat_position,
                    'best_kill': best_kill,
                    'average_win_rate': str(player_info['stat_kda']['average_win_rate']) + '%',
                    'game_recent_list': game_recent_list,
                }

                return 'success', player
            else:
                msg = DATA_NONE_MSG
                return 'error', msg
        else:
            msg = 'There is no such person, please try one more time.'
            return 'error', msg
    else:
        msg = DATA_NONE_MSG
        return 'error', msg

if __name__ == '__main__':
    pass