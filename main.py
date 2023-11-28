import keyboard
import time
import colorama
import os
import random


def main():
    global the_map
    global p1_pos
    global p2_pos
    global bullets
    global p1
    global p2
    global hp1
    global hp2
    while True:
        the_map[p1_pos[0]][p1_pos[1]] = p1
        the_map[p2_pos[0]][p2_pos[1]] = p2
        gui(the_map, hp1, hp2)

        handle_shooting("space", p1_pos)
        handle_shooting("control", p2_pos)

        if hp1 <= 0:
            winner = "p2"
            break
        if hp2 <= 0:
            winner = "p1"
            break

        bullets, the_map = handle_bullet_movement(bullets, "●", the_map)
        for bullet_pos in bullets:
            if (bullet_pos[0], bullet_pos[1]) == (p1_pos[0], p1_pos[1]):
                hp1 -= 10
            if (bullet_pos[0], bullet_pos[1]) == (p2_pos[0], p2_pos[1]):
                hp2 -= 10
        p1_pos, the_map = move_player("w", "s", "a", "d", p1, p1_pos, the_map, "f", "v", "c", "b")
        p2_pos, the_map = move_player("i", "k", "j", "l", p2, p2_pos, the_map, "up", "down", "left", "right")
    print(winner, "is the winner")


def handle_shooting(shoot_button, p_pos):
    global the_map
    global bullets

    if keyboard.is_pressed(shoot_button):
        bullets.append(p_pos.copy())


def handle_bullet_movement(bullets, bullet, a_map):

    for i, bullet_pos in enumerate(bullets):
        if None in bullet_pos:
            continue
        if (bullet_pos[0] == 0 and bullet_pos[2][0] == "u") or (bullet_pos[0] == 9 and bullet_pos[2][0] == "d") or (
                (bullet_pos[1] == 0 and bullet_pos[2][1] == "l")) or (bullet_pos[1] == 9 and bullet_pos[2][1] == "r"):
            bullets[i] = [None, None, ["n", "n"]]
            a_map[bullet_pos[0]][bullet_pos[1]] = " "
            continue

        the_map[bullet_pos[0]][bullet_pos[1]] = " "
        if bullet_pos[2][0] == "u":
            bullets[i][0] -= 1
            if bullet_pos[2][1] == "l":
                bullets[i][1] -= 1
            elif bullet_pos[2][1] == "r":
                bullets[i][1] += 1
        elif bullet_pos[2][0] == "d":
            bullets[i][0] += 1
            if bullet_pos[2][1] == "l":
                bullets[i][1] -= 1
            elif bullet_pos[2][1] == "r":
                bullets[i][1] += 1
        elif bullet_pos[2][1] == "l":
            bullets[i][1] -= 1
        elif bullet_pos[2][1] == "r":
            bullets[i][1] += 1
        a_map[bullet_pos[0]][bullet_pos[1]] = bullet

    return bullets, a_map


def move_player(up, down, left, right, player, pos, a_map, upl, downl, leftl, rightl):
    if keyboard.is_pressed(up):
        if pos[0] != 0:
            a_map[pos[0]][pos[1]] = " "
            pos[0] -= 1
            a_map[pos[0]][pos[1]] = player
        diagonals(left, player, pos, right, a_map)
    elif keyboard.is_pressed(down):
        if pos[0] != 9:
            a_map[pos[0]][pos[1]] = " "
            pos[0] += 1
            a_map[pos[0]][pos[1]] = player
        diagonals(left, player, pos, right, a_map)

    elif keyboard.is_pressed(left):
        if pos[1] != 0:
            a_map[pos[0]][pos[1]] = " "
            pos[1] -= 1
            a_map[pos[0]][pos[1]] = player
    elif keyboard.is_pressed(right):
        if pos[1] != 9:
            a_map[pos[0]][pos[1]] = " "
            pos[1] += 1
            a_map[pos[0]][pos[1]] = player

    if keyboard.is_pressed(upl):
        pos[2] = ["u", "n"]
        if keyboard.is_pressed(leftl):
            pos[2][1] = "l"
        elif keyboard.is_pressed(rightl):
            pos[2][1] = "r"
    elif keyboard.is_pressed(downl):
        pos[2] = ["d", "n"]
        if keyboard.is_pressed(leftl):
            pos[2][1] = "l"
        elif keyboard.is_pressed(rightl):
            pos[2][1] = "r"
    elif keyboard.is_pressed(leftl):
        pos[2] = ["n", "l"]
    elif keyboard.is_pressed(rightl):
        pos[2] = ["n", "r"]
    return pos, a_map


def diagonals(left, player, pos, right, the_map):
    if keyboard.is_pressed(left):
        if pos[1] != 0:
            the_map[pos[0]][pos[1]] = " "
            pos[1] -= 1
            the_map[pos[0]][pos[1]] = player
    elif keyboard.is_pressed(right):
        if pos[1] != 9:
            the_map[pos[0]][pos[1]] = " "
            pos[1] += 1
            the_map[pos[0]][pos[1]] = player


def gui(the_map: list, hp1: int, hp2: int):
    for i in the_map:
        for j in i:
            print(f"[{j}]", end=" ")
        print()
    print(f"HP1: {hp1}")
    print(f"HP2: {hp2}")
    time.sleep(0.1)
    os.system("cls")


if __name__ == '__main__':
    the_map = [
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    ]
    p1_pos: list = [0, 0, ["d", "r"]]  # first the up down diractions
    p2_pos: list = [9, 9, ["u", "l"]]  # then the left right
    bullets: list[list] = []  # [[x,y,[direction]],...]
    p1 = "X"
    p2 = "O"
    hp1 = 100
    hp2 = 100
    main()
