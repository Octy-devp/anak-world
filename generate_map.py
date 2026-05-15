#!/usr/bin/env python3
# 安納克大陸 ASCII 地形圖生成器 v9 (final)

W, H = 120, 48
grid = [['≈' for _ in range(W)] for _ in range(H)]

def fill_rect(y1, y2, x1, x2, ch):
    for y in range(max(0,y1), min(H,y2)):
        for x in range(max(0,x1), min(W,x2)):
            grid[y][x] = ch
def draw_line_h(y, x1, x2, ch):
    for x in range(max(0,x1), min(W,x2)):
        grid[y][x] = ch
def draw_line_v(x, y1, y2, ch):
    for y in range(max(0,y1), min(H,y2)):
        grid[y][x] = ch
def draw_text(y, x, text):
    for i, ch in enumerate(text):
        if 0 <= x+i < W and 0 <= y < H:
            grid[y][x+i] = ch
def set_ch(y, x, ch):
    if 0 <= y < H and 0 <= x < W:
        grid[y][x] = ch

# 大陸基底
fill_rect(0, 5, 70, 116, '*')
fill_rect(0, 5, 4, 70, ':')
fill_rect(5, 8, 4, 116, '▲')
fill_rect(8, 43, 4, 58, '·')
fill_rect(8, 43, 66, 115, ',')
fill_rect(8, 41, 58, 66, '▲')
fill_rect(20, 23, 60, 64, '·')
fill_rect(20, 23, 64, 66, ',')
fill_rect(24, 32, 12, 55, '·')
fill_rect(29, 36, 45, 58, '≋')
fill_rect(34, 43, 4, 24, '░')
fill_rect(36, 43, 66, 90, ',')
fill_rect(43, 46, 4, 115, '▲')
fill_rect(46, 48, 4, 95, '▓')

# 河流
draw_line_h(8, 40, 58, '~')
draw_line_v(50, 5, 20, '~')
draw_line_h(20, 42, 60, '~')
draw_line_h(21, 18, 60, '~')
draw_line_v(58, 21, 24, '~')
draw_line_h(24, 12, 66, '~')
draw_line_h(27, 66, 82, '~')
draw_line_h(37, 82, 95, '~')
draw_line_h(40, 88, 108, '~')
draw_line_h(43, 98, 116, '~')
draw_line_h(38, 18, 28, '~')
draw_line_h(35, 24, 34, '~')

# 城市/地標
set_ch(3,  20, '●')
set_ch(21, 25, '●')
set_ch(21, 80, '●')
set_ch(47, 100, '●')   # 塔拉薩
set_ch(2,  55, '○')
set_ch(11, 35, '○')
set_ch(17, 20, '○')
set_ch(19, 42, '○')
set_ch(25, 48, '○')
set_ch(29, 22, '○')
set_ch(37, 28, '○')
set_ch(39, 38, '○')
set_ch(40, 12, '○')
set_ch(15, 85, '○')
set_ch(19, 95, '○')
set_ch(23, 102, '○')
set_ch(38, 75, '○')
set_ch(9, 45, '◎')
set_ch(40, 8,  '◎')
set_ch(42, 14, '○')

# 標籤
labels = [
    (1, 82, "阿爾比諾克拉西亞（白霜）"),
    (2, 88, "Albinocracy"),
    (2, 10, "【北境概念區】"),
    (3, 12, "Northlands"),
    (4, 14, "霍羅托里亞"),
    (2, 57, "伯格施米德"),
    (6, 35, "約恩維德山脈"),
    (7, 38, "Jarnvid Mtns"),
    (10, 28, "銀霜邊疆"),
    (11, 30, "Silberfrost"),
    (15, 8,  "塞拉菲昂神聖帝國"),
    (16, 10, "Holy Empire"),
    (15, 72, "凱撒里克帝國"),
    (16, 76, "Caesaric Empire"),
    (18, 60, "怒嘯山脈"),
    (19, 61, "Howling Peaks"),
    (24, 50, "【魯普圖斯隘口】"),
    (26, 8,  "中央沖積平原"),
    (31, 46, "帕魯斯沼澤"),
    (32, 48, "Palus Nebulae"),
    (35, 6,  "銀葉林"),
    (36, 7,  "Silva Argentea"),
    (41, 4,  "艾爾達拉秘境"),
    (42, 5,  "Secret Eldara"),
    (44, 38, "塔爾塔魯斯山脈"),
    (45, 42, "Tartarus Mtns"),
    (46, 42, "阿比蘇斯深淵"),
    (47, 45, "The Abyssus"),
    (46, 96, "風息群島"),
    (47, 104, "Wind Isles"),   # 避開塔拉薩●(x=102)
    (10, 42, "鏡湖"),
    (12, 33, "霜堡"),
    (17, 12, "劍誓池"),
    (18, 44, "雙子門市"),
    (20, 22, "維特魯斯"),
    (24, 42, "焰紋市"),
    (28, 24, "金穗堡"),
    (36, 26, "鹽白城"),        # 移開河流(y=35有希爾薇恩河)
    (38, 40, "潮音宮"),
    (39, 14, "拉迪克斯守望"),
    (14, 72, "霜落城"),
    (18, 86, "雪山堡"),
    (22, 92, "銀鱗港"),
    (20, 77, "奧斯堡"),
    (36, 70, "灰燼商道"),
    (37, 72, "Ash Road"),
    (28, 72, "奧魯姆河→"),
    (23, 52, "傑米努斯大河→"),
]

for y, x, text in labels:
    draw_text(y, x, text)

lines = []
lines.append("═" * W)
lines.append(" " * 48 + "安納克大陸（Ankora）地形圖")
lines.append("═" * W)
lines.append(" " * 56 + "北 ↑")
for y in range(H):
    lines.append(''.join(grid[y]))
lines.append("─" * W)
lines.append("圖例：▲山脈 ~河流 ░森林/秘境 ≋沼澤 ≈海洋 *冰雪/白霜 :北境凍土 ·塞拉菲昂 ,凱撒里克 ▓深淵")
lines.append("       ●首都 ◎特殊地標/秘境 ○重要城市/要塞")
lines.append("─" * W)
lines.append("Geography：1.怒嘯山脈 2.約恩維德山脈 3.塔爾塔魯斯山脈 4.傑米努斯大河 5.奧魯姆河 6.約恩維德河")
lines.append("  7.中央沖積平原 8.鏡湖 9.銀葉林 10.帕魯斯沼澤 11.世界樹 12.深淵 13.風息群島")
lines.append("─" * W)

print('\n'.join(lines))
