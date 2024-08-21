# 100exs = 10Books
# Price of 1exs = 5000
# 100exs <= No disc
# 100exs >= 200 5% first 100 15% next 100
# 200exs > 200 7% first 100 17% second 100 and 27% for the rest 100

ex = int(input('Jumlah Buku: '))*10

if ex<=100:
    pr = ex*5000
    print(f"Total harga: Rp.{pr:,}")
elif ex<=200:
    rexs = ex-100
    pr = ((100*5000)*0.95) + ((rexs*5000)*0.85)
    print(f"Total harga: Rp.{pr:,}")
else:
    rexs = ex-200
    pr = ((100*5000)*0.93) + ((100*5000)*0.83) + ((rexs*5000)*0.73)
    print(f"Total harga: Rp.{pr:,}")
