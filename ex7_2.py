#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Viết 1 một trò chơi đánh đối kháng giữa 2 nhân vật. Mỗi nhân vật có tên (str),
máu (int), vũ khí.
Vũ khí chọn random khi tạo nhân vật, có damage (int) bằng lượng máu trừ đi
khi đánh trúng.

Cho 2 nhân vật lần lượt đánh nhau, print kết quả mỗi lượt đánh, print người
thắng.

'''


class Fighter():
    def __init__(self, name, HP):
        import random
        self.name = random.choice(['Ty','Suu','Dan','Meo'],)
        self.HP = random.choice([100,110,120])


    def __str__(self):
        return "{} (HP {})".format(self.name, self.HP)
class Weapon():
    def __init__(self):
        import random
        self.name = random.choice(['Dao','Kiem','Bua'])
        self.damage = random.choice([30,32,34])
    def __str__(self):
        return "su dung {} cung vs {} damage".format(self.name,self.damage)
    def solve(player1, player2):
        import random
        player1 = Fighter()
        player2 = Fighter()
        player1_weapon = Weapon()
        player2_weapon = Weapon()
        player1_turn = random.randrange(10)
        player2_turn = random.randrange(10)
        round_num = 0
        print ('Play 1\'s fighter is', player1,player1_weapon)
        print ('Play 2\'s fighter is', player2,player2_weapon)
        if player1_turn>player2_turn:
            print ('nguoi 1 danh nguoi 2 truoc')
            while player1.HP >0 and player2.HP >0:
                round_num += 1
                player2.HP = player2.HP - player1_weapon.damage
                if player2.HP <= 0:
                    result = (player1, player1.HP)
                    break
                print (
                    'Round number', round_num,':',
                    'nguoi choi 1\' con lai HP:{}'.format(player1.HP)
                )
                print (
                    'Round number', round_num,':',
                    'nguoi choi 2\' con lai HP:{}'.format(player2.HP)
                )
            else:
                print ('nguoi choi 2 danh nguoi choi 1 truoc')
                while player1.HP >0 and player2.HP >0:
                    round_num += 1
                    player1.HP = player1.HP - player2_weapon.damage
                    if player1.HP<=0:
                        result = ('nguoi choi 2',player2.HP)
                        break
                    player2.HP = player2.HP - player1_weapon.damage
                    if player2.HP<=0:
                        result = ('nguoi choi 1',player1.HP)
                        break
                    print (
                        'round number', round_num,':',
                        'nguoi choi 1\'s con lai HP:{}'.format(player1.HP)
                    )
                    print (
                        'round number', round_num,':',
                        'nguoi choi 2\'s con lai HP:{}'.format(player2.HP)
                    )
            print (
                'nguoi thang la {} con lai {} HP'.format(result[0],result[1])
            )
            return result




    # Add more if needed


# class Weapon():
#     pass
#
#
# def solve(player1, player2):
#     '''Trả về tuple tên người thắng cuộc và lượng máu còn lại (int)'''
#     result = ('', 0)

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Học viên chưa làm bài này")
    #
    # return result


# def main():
#     # Thay đổi các dòng sau cho phù hợp
#     player1 = Fighter()
#     player2 = Fighter()
#     print(solve(player1, player2))
#
#
# if __name__ == "__main__":
#     main()
