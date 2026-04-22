import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("シンプルRPG")
font = pygame.font.SysFont("yugothic", 28)

# データ
player = {"hp": 100, "mp": 30, "attack": 20, "magic": 35}
monster = {"name": "ドラゴン", "hp": 80, "attack": 15}
commands = ["攻撃", "魔法", "回復", "逃げる"]
selected = 0
log = "モンスターが現れた！"

def draw():
    screen.fill((255, 255, 255))
    font.render
    screen.blit(font.render(f"{monster['name']} HP:{monster['hp']}", True, (220, 50, 50)), (80, 60))
    screen.blit(font.render(f"勇者 HP:{player['hp']} MP:{player['mp']}", True, (50, 100, 220)), (80, 240))
    screen.blit(font.render(log, True, (0, 0, 0)), (80, 320))
    for i, cmd in enumerate(commands):
        color = (240, 200, 0) if i == selected else (180, 180, 180)
        pygame.draw.rect(screen, color, (60 + i * 130, 360, 110, 40), border_radius=6)
        screen.blit(font.render(cmd, True, (0, 0, 0)), (75 + i * 130, 368))
    pygame.display.flip()

def player_action():
    global log
    cmd = commands[selected]
    if cmd == "攻撃":
        monster["hp"] -= player["attack"]
        log = f"攻撃！{player['attack']}ダメージ！"
    elif cmd == "魔法":
        if player["mp"] >= 10:
            player["mp"] -= 10
            monster["hp"] -= player["magic"]
            log = f"魔法！{player['magic']}ダメージ！"
        else:
            log = "MPが足りない！"
            return
    elif cmd == "回復":
        player["hp"] = min(player["hp"] + 30, 100)
        log = "HPを30回復した！"
    elif cmd == "逃げる":
        print("逃げた！")
        pygame.quit(); sys.exit()

    # モンスターの反撃
    if monster["hp"] > 0:
        dmg = random.randint(10, 20)
        player["hp"] -= dmg
        log += f" ドラゴンの攻撃！{dmg}ダメージ！"

    # 勝敗チェック
    if monster["hp"] <= 0:
        print("勝利！"); pygame.quit(); sys.exit()
    if player["hp"] <= 0:
        print("敗北…"); pygame.quit(); sys.exit()

# メインループ
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                selected = (selected - 1) % len(commands)
            elif event.key == pygame.K_RIGHT:
                selected = (selected + 1) % len(commands)
            elif event.key == pygame.K_RETURN:
                player_action()
    draw()