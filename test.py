import pyupbit

access = "prNX10DVghhC7hp5ofPCNRk9EDkb81VNN0oLiFlB"  # 본인 값으로 변경
secret = "FnnkfXwxI5oxxzOuf0gjfDOOaH8bmFTndjKgYZsq"  # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-trx"))  # KRW-XRP 조회
print(upbit.get_balance("KRW"))  # 보유 현금 조회
