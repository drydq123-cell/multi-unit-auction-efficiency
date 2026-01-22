# 多单元统一价格拍卖模拟代码
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def uniform_price_auction(bidders, units, bids):
    """
    统一价格拍卖模拟：计算成交价格和中标分配
    :param bidders: 投标人数量
    :param units: 待拍卖物品数量
    :param bids: 每个投标人的报价列表
    :return: 成交价格、各投标人中标数量
    """
    # 整理所有报价（投标人ID + 报价）
    all_bids = []
    for i, bid in enumerate(bids):
        for b in bid:
            all_bids.append((i, b))
    
    # 按报价从高到低排序
    all_bids_sorted = sorted(all_bids, key=lambda x: x[1], reverse=True)
    
    # 确定成交价格
    if len(all_bids_sorted) >= units:
        clearing_price = all_bids_sorted[units-1][1]
    else:
        clearing_price = min([b for _, b in all_bids_sorted]) if all_bids_sorted else 0
    
    # 计算每个投标人的中标数量
    allocation = {}
    for bidder_id in range(bidders):
        valid_bids = [b for b in bids[bidder_id] if b >= clearing_price]
        allocation[bidder_id] = len(valid_bids)
    
    return clearing_price, allocation

# 测试代码（运行后会输出结果并画图）
if __name__ == "__main__":
    # 模拟5个投标人、拍卖3个单位，每个投标人报2个价格
    bidders = 5
    units = 3
    bids = [[100,95], [98,90], [99,92], [97,88], [96,85]]
    
    # 运行拍卖模拟
    clearing_price, allocation = uniform_price_auction(bidders, units, bids)
    
    # 打印结果
    print(f"成交价格: {clearing_price}")
    print("各投标人中标数量:")
    for bidder, count in allocation.items():
        print(f"投标人{bidder+1}: {count}个")
    
    # 生成可视化图表
    plt.bar(range(1, bidders+1), [sum(b) for b in bids])
    plt.axhline(y=clearing_price, color='r', linestyle='--', label=f'成交价格: {clearing_price}')
    plt.xlabel('投标人ID')
    plt.ylabel('总报价')
    plt.title('多单元统一价格拍卖结果')
    plt.legend()
    plt.show()