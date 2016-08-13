#!/usr/bin/env python
# encoding: utf-8

import click
import sys
from fetch import fetch_rank, fetch_hero_rank, fetch_player
from utils import make_chart, make_player_chart

reload(sys)
sys.setdefaultencoding('utf-8')

__author__ = 'corazon'


@click.group()
@click.option('--region', '-r', default="", help="LOL region name")
@click.option('--page', '-p', default='1', type=str, help='Page')
@click.option('--name', '-n', default='', help="Player name")
@click.option('--dan', '-d', default='', help="Dan")
@click.pass_context
def lol_qy(ctx, region, page, name, dan):
    ctx.obj['REGION'] = region.encode('utf-8')
    ctx.obj['PAGE'] = page
    ctx.obj['NAME'] = name.encode('utf-8')
    ctx.obj['DAN'] = dan.encode('utf-8')


@lol_qy.command()
@click.pass_context
def rank(ctx):
    try:
        click.echo("Collecting magician information, please wait...\xF0\x9F\x98\x81")
    except:
        click.echo("Collecting magician information, please wait...")

    rank_list = fetch_rank(ctx.obj)
    if rank_list[0] != 'error':
        field_names = ['排名', '玩家名称', '大区', '段位', '胜点', '战斗力']
        res = make_chart(field_names, rank_list[1])
    else:
        res = rank_list[1]
    click.echo(res)


@lol_qy.command()
@click.pass_context
def hero(ctx):
    try:
        click.echo("Collecting magician information, please wait...\xF0\x9F\x98\x81")
    except:
        click.echo("Collecting magician information, please wait...")
    hero_rank_list = fetch_hero_rank(ctx.obj)
    if hero_rank_list[0] != 'error':
        field_names = ['排名', '英雄', '出场率', '胜率', '出场次数', '位置', '角色', '描述']
        res = make_chart(field_names, hero_rank_list[1])
    else:
        res = hero_rank_list[1]
    click.echo(res)


@lol_qy.command()
@click.pass_context
def player(ctx):
    try:
        click.echo("Collecting magician information, please wait...\xF0\x9F\x98\x81")
    except:
        click.echo("Collecting magician information, please wait...")
    player_info = fetch_player(ctx.obj)
    if player_info[0] != 'error':
        player_info, recent_game = make_player_chart(player_info[1])
        click.echo(player_info)
        click.echo(recent_game)
    else:
        res = player_info[1]
        click.echo(res)

if __name__ == "__main__":
    lol_qy(obj={})