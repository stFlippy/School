#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

from pprint import pprint

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

Moscow = sites['Moscow']
London = sites['London']
Paris = sites['Paris']

M_L = ((Moscow[0]-London[0])**2+ (Moscow[1]-London[1])**2)**0.5
M_P = ((Moscow[0]-Paris[0])**2 + (Moscow[1]-Paris[1])**2)**0.5
L_P = ((Paris[0]-London[0])**2 + (Paris[1]-London[1])**2)**0.5


distances = {'Moscow': {'London': M_L, 'Paris': M_P},
             'Paris': {'London': L_P, 'Moscow': M_P},
             'London': {'Moscow': M_L, 'Paris': L_P}}




# TODO здесь заполнение словаря

pprint(distances[input()][input()])





