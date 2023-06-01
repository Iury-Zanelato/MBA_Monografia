# -*- coding: utf-8 -*-
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com
# @File    : plot_bdgd.py
# @Software: PyCharm

import geopandas as gpd
from shapely.geometry import Point, LineString, Polygon
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import folium

rootpath = os.getcwd()
CONJ_bv = [12729, 12731, 12727]
SUB_bv = ['5003365', '5003346', '5003405', '5003625', '5003406', '5003530', '5003345', '5003305', '5003585', '5003525']
TAB = ['ARAT.shp', 'CONJ.shp', 'SUB.shp', 'PONNOT.shp', 'UNTRAT.shp', 'UNTRMT.shp',
       'SSDAT.shp', 'SSDMT.shp', 'SSDBT.shp', 'UNSEAT.shp', 'UNSEMT.shp', 'UNSEBT.shp',
       'UNCRAT.shp', 'UNCRMT.shp', 'UNCRBT.shp', 'UNREAT.shp', 'UNREMT.shp']

path_shp = r"C:\Users\ppra005\Box\Documents_PC\PR\OpenDSS_Perdas\2-RoraimaFiles\BDGD e arquivos para análises\BDGD e arquivos para análises\BDGD\BDGD_SERVIDOR"

mun = '1400100'
conj = 12727
sub = '5003305'
ctmt = 'CE_AL2-04'
untrd = '1002408381'
untrs = 'TF_12244'
ssdbt = '55828180'
ssdmt = '55827571'
uncbt = '174120'  # objectid
ramlig = '157583'  # objectid
pip = '49416'  # objectid

# ----------------------------------------------------------------------------------------------------------------------
path_arat = os.path.join(path_shp, TAB[0])  # ARAT
path_conj = os.path.join(path_shp, TAB[1])  # CONJ
path_sub = os.path.join(path_shp, TAB[2])  # SUB
path_ponnot = os.path.join(path_shp, TAB[3])  # PONNOT
path_untrs = os.path.join(path_shp, TAB[4])  # UNTRS
path_untrd = os.path.join(path_shp, TAB[5])  # UNTRD
path_ssdat = os.path.join(path_shp, TAB[6])  # SSDAT
path_ssdmt = os.path.join(path_shp, TAB[7])  # SSDMT
path_ssdbt = os.path.join(path_shp, TAB[8])  # SSDBT

gdf_arat = gpd.read_file(path_arat)
gdf_sub = gpd.read_file(path_sub)
gdf_conj = gpd.read_file(path_conj)
gdf_ssdat = gpd.read_file(path_ssdat)
gdf_ssdmt = gpd.read_file(path_ssdmt)
gdf_ssdbt = gpd.read_file(path_ssdbt)
gdf_ponnot = gpd.read_file(path_ponnot)
gdf_untrd = gpd.read_file(path_untrd)
gdf_untrs = gpd.read_file(path_untrs)
# gdf2.geometry

# df_cc = pd.read_excel(os.path.join(rootpath, 'TIP_CC_20200821.xlsx'))

# ----------------------------------------------------------------------------------------------------------------------

# fig, ax = plt.subplots(figsize=(6.0, 3.0))
fig, ax = plt.subplots(figsize=(6.0, 6.0))

# ----------------------------------------------------------------------------------------------------------------------
# # df_cc[df_cc['CodCrvCrg'].str.contains('Com')]  # DU/ SA/ DO
# # df = df_cc[(df_cc['CodCrvCrg'] == 'B3_Com_Tipo 2') & (df_cc['TipoDia'] == 'DU')]
# # df = df_cc[(df_cc['CodCrvCrg'] == 'B3_Com_Tipo 2')]
# df = df_cc[(df_cc['CodCrvCrg'] == 'IP-Tipo1')]
# df.drop_duplicates(subset='TipoDia', inplace=True)
# CodCrvCrg = df['CodCrvCrg'].tolist()
# cc = df.iloc[:, 3:-1].T
# cc.columns = CodCrvCrg
# cc.index = pd.date_range(pd.Timestamp('2023-01-16 00:00'), periods=96, freq='15min')
# cc.plot(ax=ax)
# DiasSemana = ['DU', 'SA', 'DO']
# labels = ['{} - {}'.format(l, DiasSemana[i]) for i, l in enumerate(ax.get_legend_handles_labels()[1])]
# ax.legend(labels)
#
# ax.set_title('Curvas de cargas - 96 pontos', fontsize=10, weight="bold")
# ax.set_xlabel('Tempo [horas]', fontsize=10, weight="bold")
# ax.set_ylabel('Potência [kW]', fontsize=10, weight="bold")
# fig.subplots_adjust(left=0.09, bottom=0.22, right=0.983, top=0.926)

# ----------------------------------------------------------------------------------------------------------------------
# gdf_conj[gdf_conj['COD_ID'] == 12727].plot(ax=ax, facecolor='whitesmoke', edgecolor='black')
# gdf_sub[gdf_sub['COD_ID'] == sub].plot(ax=ax, color='black')
# gdf_ssdmt[gdf_ssdmt['CTMT'] == 'CE_AL2-04'].plot(ax=ax)
# gdf_untrd[gdf_untrd['CTMT'] == 'CE_AL2-04'].plot(ax=ax, marker='^', markersize=20, color='black')  # marker='*'
# gdf_ssdmt[gdf_ssdmt['COD_ID'] == ssdmt].plot(ax=ax, color='red')  # , legend=True
# ----------------------------------------------------------------------------------------------------------------------
# gdf_untrd[gdf_untrd['COD_ID'] == untrd].plot(ax=ax, marker='^', markersize=50, color='black')
# gdf_ssdbt[gdf_ssdbt['UNI_TR_MT'] == untrd].plot(ax=ax, color='blue', linewidth=2.0)
# gdf_ssdbt[gdf_ssdbt['COD_ID'] == ssdbt].plot(ax=ax, color='red', linewidth=2.0)
# ax.annotate("UNTRMT: {}\nCTMT: {}\nSUB: {}".format(untrd, ctmt, sub), (-60.675378, 2.825219),
#             xycoords='data',  # xycoords='axes fraction',
#             fontsize=8, color="black", weight="bold")
# ----------------------------------------------------------------------------------------------------------------------

# gdf_sub[gdf_sub['COD_ID'] == sub].plot(ax=ax, color='blue')
# # gdf_untrs[gdf_untrs['COD_ID'] == untrs].plot(ax=ax, color='yellow', marker='*', markersize=70)
#
# gdf_ssdmt[gdf_ssdmt['SUB'] == sub].plot(ax=ax, color='gray', linewidth=1.0)
# gdf_ssdmt[gdf_ssdmt['CTMT'] == ctmt].plot(ax=ax, color='red', linewidth=2.0)
# # ax.set_xlim(-60.468125, -60.465881)
# # ax.set_ylim(2.428088, 2.426083)
#
# # insere eixo interno no eixo ax ....
# axins = ax.inset_axes([0.60, 0.05, 0.5, 0.45])  # bounds=[x0, y0, width, height]/[-48.64, -1.51, 0.34, 0.51]
# axins.set_xlim(-60.68386, -60.67736)
# axins.set_ylim(2.82253, 2.82831)
# axins.set_xticklabels('')
# axins.set_yticklabels('')
# ax.indicate_inset_zoom(axins,
#                        edgecolor="black",
#                        alpha=1,
#                        linewidth=2.0,
#                        linestyle="--")
#
# gdf_sub[gdf_sub['COD_ID'] == sub].plot(ax=axins, color='blue')
# gdf_ssdmt[gdf_ssdmt['SUB'] == sub].plot(ax=axins, color='gray', linewidth=1.0)
# gdf_ssdmt[gdf_ssdmt['CTMT'] == ctmt].plot(ax=axins, color='red', linewidth=3.0)
# gdf_untrs[gdf_untrs['COD_ID'] == untrs].plot(ax=axins, color='yellow', marker='*', markersize=70)
#
# axins.annotate("SE: {}".format(sub), (-60.68008, 2.82263),
#                xycoords='data',  # xycoords='axes fraction',
#                fontsize=10, color="black", weight="bold")
#
# axins.annotate("UNTRAT: {}".format('PED_02T1'),
#                xy=(-60.67893, 2.82358), xytext=(-60.68258, 2.82570),
#                arrowprops=dict(arrowstyle="->", connectionstyle="arc3"),
#                xycoords='data',  # xycoords='axes fraction',
#                fontsize=8, color="black", weight="bold")
#
# axins.annotate("PAC: {}".format('12059-7022887'),
#                xy=(-60.679212, 2.824139), xytext=(-60.68258, 2.82629),
#                arrowprops=dict(arrowstyle="->", connectionstyle="arc3"),
#                xycoords='data',  # xycoords='axes fraction',
#                fontsize=8, color="black", weight="bold")

# ----------------------------------------------------------------------------------------------------------------------

set1 = set(gdf_ssdmt[gdf_ssdmt['CTMT'] == ctmt]['PN_CON_1'].unique())
set2 = set(gdf_ssdmt[gdf_ssdmt['CTMT'] == ctmt]['PN_CON_2'].unique())
set = set1.union(set2)

# gdf_ponnot[gdf_ponnot['COD_ID'].isin(list(set))].plot(ax=ax, color='black', markersize=10)
# gdf_ponnot[gdf_ponnot['COD_ID'] == 'PG_9985830'].plot(ax=ax, color='red', markersize=10)
# gdf_ponnot[gdf_ponnot['COD_ID'] == 'PG_9986266'].plot(ax=ax, color='red', markersize=10)

# insere eixo interno no eixo ax ....
axins = ax.inset_axes([0.01, 0.05, 0.40, 0.4])  # bounds=[x0, y0, width, height]/[-48.64, -1.51, 0.34, 0.51]
axins.set_xlim(-60.675767, -60.674796)
axins.set_ylim(2.825115, 2.825936)
axins.set_xticklabels('')
axins.set_yticklabels('')
ax.indicate_inset_zoom(axins,
                       edgecolor="black",
                       alpha=1,
                       linewidth=2.0,
                       linestyle="--")
gdf_ssdmt[gdf_ssdmt['CTMT'] == ctmt].plot(ax=axins, color='gray', linewidth=1.0)
gdf_ponnot[gdf_ponnot['COD_ID'].isin(list(set))].plot(ax=axins, color='black', markersize=30)
gdf_ponnot[gdf_ponnot['COD_ID'] == 'PG_9985830'].plot(ax=axins, color='red', markersize=30)
gdf_ponnot[gdf_ponnot['COD_ID'] == 'PG_9986266'].plot(ax=axins, color='red', markersize=30)
axins.annotate("COD_ID: {}".format('PG_9985830'), (-60.675619, 2.825709),
               xycoords='data',  # xycoords='axes fraction',
               fontsize=8, color="black", weight="bold")
axins.annotate("COD_ID: {}".format('PG_9986266'), (-60.675439, 2.825247),
               xycoords='data',  # xycoords='axes fraction',
               fontsize=8, color="black", weight="bold")

# ----------------------------------------------------------------------------------------------------------------------

# # gdf_ssdat[gdf_ssdat['CONJ'].isin(CONJ_blm)].plot(ax=ax)
# gdf_ssdat.plot(ax=ax)
# gdf_sub[gdf_sub['COD_ID'].isin(SUB_blm)].plot(ax=ax, color='black')

# ----------------------------------------------------------------------------------------------------------------------

# gdf_ssdbt[gdf_ssdbt['UNI_TR_D'] == untrd].plot(ax=ax)
# gdf_ssdbt[gdf_ssdbt['COD_ID'] == ssdbt].plot(ax=ax, color='red', linewidth=3.0)
# gdf_untrd[gdf_untrd['COD_ID'] == untrd].plot(ax=ax, marker='^', markersize=50, color='black')  # marker='*'
# ax.annotate("UNTRD: {}\nCTMT: {}\nSUB: {}".format(untrd, ctmt, sub), (-48.4643, -1.434),
#             xycoords='data',  # xycoords='axes fraction',
#             fontsize=8, color="black", weight="bold")

# -------------------------------------------------------------------------------------------------------

# gdf_sub[gdf_sub['COD_ID'] == sub].plot(ax=ax)
# gdf_ssdmt[gdf_ssdmt['CTMT'] == ctmt].plot(ax=ax)
# gdf_untrd[gdf_untrd['CTMT'] == ctmt].plot(ax=ax, marker='^', markersize=20, color='black')  # marker='*'
# gdf_ssdmt[gdf_ssdmt['COD_ID'] == ssdmt].plot(ax=ax, color='red', linewidth=3.0)
# ax.set_xlim(-60.68029, -60.67184)
# ax.set_ylim(2.82280, 2.82895)
# ax.annotate("SUB: {}\nCTMT: {}".format(sub, ctmt), (-60.67808, 2.82342),
#             xycoords='data',  # xycoords='axes fraction',
#             fontsize=8, color="black", weight="bold")

# ----------------------------------------------------------------------------------------------------------------------

# gdf_arat.plot(ax=ax, facecolor='whitesmoke', edgecolor='black')
# gdf_conj[gdf_conj['COD_ID'].isin(CONJ_bv)].plot(ax=ax, facecolor='lightblue', edgecolor='black')
# gdf_conj[gdf_conj['COD_ID'] == conj].plot(ax=ax, facecolor='red', edgecolor='black')
# # gdf_conj[gdf_conj['COD_ID'].isin(CONJ_blm)].plot(column='COD_ID', ax=ax, legend=True)
#
# # insere eixo interno no eixo ax ....
# axins = ax.inset_axes([0.10, 0.10, 0.35, 0.51])  # bounds=[x0, y0, width, height]/[-48.64, -1.51, 0.34, 0.51]
# axins.set_xlim(-61.035, -60.271)
# axins.set_ylim(2.418, 3.632)
# axins.set_xticklabels('')
# axins.set_yticklabels('')
# ax.indicate_inset_zoom(axins,
#                        edgecolor="black",
#                        alpha=1,
#                        linewidth=2.0,
#                        linestyle="--")
# gdf_conj[gdf_conj['COD_ID'].isin(CONJ_bv)].plot(ax=axins, facecolor='lightblue', edgecolor='black')
# gdf_conj[gdf_conj['COD_ID'] == conj].plot(ax=axins, facecolor='red', edgecolor='black')
# # gdf_conj[gdf_conj['COD_ID'].isin(CONJ_blm)].plot(column='COD_ID', ax=axins)
# # axins.grid(True)

# -----------------------------------------------------------------

# gdf_sub[gdf_sub['COD_ID'] == sub].plot(ax=ax, color='black')
# # gdf_conj[gdf_conj['NOM'] == 'PEDREIRA'].plot(ax=ax, facecolor='white', edgecolor='black', linewidth=2.0)
# gdax = gdf_ssdmt.plot(column='CTMT', ax=ax,  # cmap=color_steps,
#                  legend=True,
#                  legend_kwds={'loc': 'upper right',  # ncol=2, bbox_to_anchor=(0,0)
#                               'title': 'CTMT:',
#                               'markerscale': 0.5,
#                               'title_fontproperties': {'size': 'medium', 'weight': 'bold'},
#                               'fontsize': 'small',  # xx-small/x-small/small/medium/large/x-large/xx-large
#                               # 'prop': {'size': 'small', 'weight': 'bold'}
#                               }
#                  )
# # gdf_ponnot.plot(ax=ax, markersize=0.5, color='gray', label='PONNOT', legend=True,)
# ax.annotate("SUB: {}".format(sub), (-48.4659, -1.4274),
#             xycoords='data',  # xycoords='axes fraction',
#             fontsize=9, color="black", weight="bold")

# ---------------------------------------------------------------------------------------------------------

# gdf_sub[gdf_sub['COD_ID'] == sub].plot(ax=ax, color='black')
# gdf_ssdmt[gdf_ssdmt['SUB'] == sub].plot(column='CTMT', ax=ax,
#                       legend=True,
#                       legend_kwds={'loc': 'upper right',  # ncol=2, bbox_to_anchor=(0,0)
#                               'title': 'CTMT:',
#                               'markerscale': 0.5,
#                               'title_fontproperties': {'size': 'medium', 'weight': 'bold'},
#                               'fontsize': 'small',  # xx-small/x-small/small/medium/large/x-large/xx-large
#                               # 'prop': {'size': 'small', 'weight': 'bold'}
#                               }
#                       )
# # gdf_ponnot.plot(ax=ax, markersize=0.5, color='gray', label='PONNOT', legend=True,)
# ax.annotate("SUB: {}".format(sub), (-48.4659, -1.4274),
#             xycoords='data',  # xycoords='axes fraction',
#             fontsize=9, color="black", weight="bold")
# # insere eixo interno no eixo ax ....
# axins = ax.inset_axes([0.01, 0.60, 0.35, 0.35])  # bounds=[x0, y0, width, height]/[-48.64, -1.51, 0.34, 0.51]
# axins.set_xlim(-60.680405, -60.6777804)
# axins.set_ylim(2.822634, 2.826286)
# axins.set_xticklabels('')
# axins.set_yticklabels('')
# ax.indicate_inset_zoom(axins,
#                        edgecolor="black",
#                        alpha=1,
#                        linewidth=2.0,
#                        linestyle="--")
# gdf_sub[gdf_sub['COD_ID'] == sub].plot(ax=axins, color='black')
# gdf_ssdmt.plot(column='CTMT', ax=axins)

# ---------------------------------------------------------------------------------------------------------

# sub = '5003365'
# ctmt = 'FT_AL2-10'
# mun = '1505502'
# unremt = '5801162'
# untrs = 'TF_12841'
#
# path_sub_par = os.path.join(path_shp, TAB[2])  # SUB
# path_ssdmt_par = os.path.join(path_shp, TAB[7])  # SSDMT
# path_unremt_par = os.path.join(path_shp, TAB[16])  # UNREMT
# gdf_sub_par = gpd.read_file(path_sub_par)
# gdf_unremt_par = gpd.read_file(path_unremt_par)
# gdf_ssdmt_par = gpd.read_file(path_ssdmt_par)
#
# gdf_sub_par[gdf_sub_par['COD_ID'] == sub].plot(ax=ax, color='black')
# gdf_ssdmt_par[gdf_ssdmt_par['CTMT'] == ctmt].plot(ax=ax)
# gdf_unremt_par[gdf_unremt_par['CTMT'] == ctmt].plot(ax=ax, color='red')
#
# # insere eixo interno no eixo ax ....
# axins = ax.inset_axes([0.5, 0.15, 0.40, 0.6])  # bounds=[x0, y0, width, height]/[-48.64, -1.51, 0.34, 0.51]
# axins.set_xlim(-60.71466, -60.70639)
# axins.set_ylim(2.82562, 2.83051)
# axins.set_xticklabels('')
# axins.set_yticklabels('')
# ax.indicate_inset_zoom(axins,
#                        edgecolor="black",
#                        alpha=1,
#                        linewidth=2.0,
#                        linestyle="--")
# gdf_sub_par[gdf_sub_par['COD_ID'] == sub].plot(ax=axins, color='black')
# gdf_ssdmt_par[gdf_ssdmt_par['CTMT'] == ctmt].plot(ax=axins)
#
# axins.annotate("SUB: {} \nCTMT: {}".format(sub, ctmt), (-60.71297, 2.82583),
#                xycoords='data',  # xycoords='axes fraction',
#                fontsize=9, color="black", weight="bold")

# ---------------------------------------------------------------------------------------------------------
# gdf_ssdmt.plot(ax=ax, color='blue', label='SSDMT')
# gdf2.plot(ax=ax, color='red', label='SSDMT')
# gdf3.plot(ax=ax, color='green', label='UNTRD')
# gdf.plot(column='CONJ', legend=True)


# ----------------------------------------------------------------------------------------------------------------------
# ax.legend()
# fig.subplots_adjust(left=0.086, bottom=0.045, right=1.0, top=0.964,
#                     wspace=0.0, hspace=0.348)
plt.show()
# fig.savefig("CurvasCargas_IP-Tipo1.png", dpi=300, format="png")
# fig.savefig("PONNOT.png", dpi=300, format="png")
# --------------------------------------------------
# # gdf = gpd.read_file(path, driver='GeoJSON')
# # Cria um mapa simples usando pacote folium
# fmap = folium.Map()
# feat_gejson = folium.features.GeoJson(gdf)
# fmap.add_child(feat_gejson)
# fmap.show_in_browser()
# --------------------------------------------------

# list(ponto.coords)
# ponto.x
# ponto.y
# dist = ponto1.distance(ponto2)
# linha = LineString([ponto1, ponto2])
# list(linha.coords) # [(0,0), (1,1)]


# ax.annotate("Min: {}".format(min_value), (0, 0.95), xycoords='axes fraction',
#             fontsize=8, color="black", weight="bold")
# boxes = [PVbox, HPbox, Housebox, Substationbox]
# intros = [
#     "PV Owner",
#     "Heat Pump Owner",
#     "No LCTs",
#     "Secondary Substation",
# ]
# plt.annotate("Legend", (500, 415), fontsize=10, color="black", weight="bold")
# for i in range(0, 4):
#     plt.annotate(intros[i], (515, 400 - offset[i] * 3), fontsize=9, color="black")
#     ab = AnnotationBbox(boxes[i], [500, (400 - offset[i] * 3)], frameon=False, pad=0)
#     ax.add_artist(ab)
#
# ab = AnnotationBbox(boxes[3], [Coords['X'][0], Coords['Y'][0]], frameon=False, pad=0)
# ax.add_artist(ab)

# SSDMT:
# 12059_13500073
# 12059_8250830
# 12059_13512520
# 12059_13512516
# 12059_8250831
# 12059_8250832
# 12059_8250833
# 12059_8250824
# 12059_8250687
# 12059_8250764
# 12059_8250834
# 12059_8250688
# 12059_8250803
# ----------------------
# UNTRMT: 2142553
# ----------------------
# USSDBT:
# 2142553_8251037
# 2142553_8251038
# 2142553_8251036
#
# PONNOT: 108290700

