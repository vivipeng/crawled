def validate_player(name, players):
    """验证玩家名称是否有效（大小写不敏感）"""
    return name.lower() in players

def process_transaction(payer, receiver, points, score_board):
    """处理分数交易"""
    # 统一使用小写名称
    payer = payer.lower()
    receiver = receiver.lower()
    
    score_board[receiver][payer] += points
    score_board[payer][receiver] -= points
    print(f"交易记录: {payer} -> {receiver} ({points}分)")

def print_rank(title, data):
    """打印排行榜"""
    print(f"\n{title}:")
    sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
    for i, (player, count) in enumerate(sorted_data, 1):
        print(f"{i}. {player}: {count}次")

def initialize_game():
    """初始化游戏设置"""
    while True:
        try:
            num_players = int(input("请输入玩家人数（3或4）: "))
            if num_players not in [3, 4]:
                print("玩家人数必须是3或4！")
                continue
            break
        except:
            print("输入无效，请重新输入数字")

    if num_players == 3:
        players = []
        for i in range(3):
            while True:
                name = input(f"请输入玩家{i+1}的名称: ").lower()
                if not name:
                    print("玩家名称不能为空！")
                    continue
                if name in players:
                    print("玩家名称不能重复！")
                    continue
                players.append(name)
                break
        current_players = players.copy()  # 3人游戏无候补
        current_waiting = None
    else:
        players = ['bb', 'mm', 'pw', 'wl']
        current_players = players[:3]  # 初始场上玩家
        current_waiting = players[3]   # 初始候补玩家

    # 初始化得分矩阵和统计数据
    score_board = {p: {op: 0 for op in players if op != p} for p in players}
    win_count = {p: 0 for p in players}  # 赢家次数统计
    luck_card_count = {p: 0 for p in players}  # 运气牌接收方次数统计

    return players, current_players, current_waiting, score_board, win_count, luck_card_count

def main():
    # 初始化游戏
    players, current_players, current_waiting, score_board, win_count, luck_card_count = initialize_game()

    while True:
        print("\n当前场上玩家:", current_players)
        if current_waiting:
            print("当前候补玩家:", current_waiting)
        
        # 输入赢家（自动转小写）
        winner = input("\n请输入本局赢家（输入q结束游戏）: ").lower()
        if winner == 'q':
            break
        if winner not in current_players:
            print(f"错误：玩家 {winner} 不在场上！")
            continue

        # 更新赢家次数
        win_count[winner] += 1

        # 处理基础得分
        losers = [p for p in current_players if p != winner]
        print(f"\n请依次输入每个输家给 {winner} 的分数：")
        for loser in losers:
            while True:
                try:
                    points = int(input(f"{loser} 给 {winner} 的分数: "))
                    process_transaction(loser, winner, points, score_board)
                    break
                except:
                    print("输入无效，请重新输入数字")

        # 处理运气牌
        print("\n是否需要处理运气牌？")
        while True:
            choice = input("输入'y'添加运气牌，其他键继续: ").lower()
            if choice != 'y':
                break
            
            print("\n请输入运气牌接收方：")
            while True:
                receiver = input("接收方玩家: ").lower()
                if not validate_player(receiver, players):
                    print("无效玩家，请重新输入")
                    continue
                
                # 更新运气牌接收方次数
                luck_card_count[receiver] += 1
                
                # 默认其他2位玩家为支付方
                payers = [p for p in current_players if p != receiver]
                if len(payers) != 2:
                    print("错误：场上玩家不足2人，无法处理运气牌")
                    continue
                
                # 输入交易分数
                try:
                    points = int(input("交易分数: "))
                except:
                    print("输入无效，请重新输入数字")
                    continue
                
                # 处理交易
                for payer in payers:
                    process_transaction(payer, receiver, points, score_board)
                break

        # 玩家轮换（仅4人游戏）
        if current_waiting:
            current_players.remove(winner)
            current_players.append(current_waiting)
            current_waiting = winner

    # 最终结果展示
    print("\n最终得分：")
    for player in players:
        total = sum(score_board[player].values())
        print(f"玩家 {player}: {total}分")

    # 得分详情矩阵
    print("\n得分详情矩阵：")
    header = " " * 4 + "".join([f"{p:^6}" for p in players])
    print(header)
    
    for p in players:
        row = [f"{score_board[p][op]:^6}" if op != p else "  --  " for op in players]
        print(f"{p} | " + "".join(row))

    # 赢家次数排行榜
    print_rank("赢家次数排行榜", win_count)

    # 运气牌接收方次数排行榜
    print_rank("运气牌接收方次数排行榜", luck_card_count)

if __name__ == "__main__":
    main()