rates = {"ARS": 0.82, "HNL": 0.17, "AUD": 1.9622, "MAD": 0.208}

wallet = float(input())

for i in rates:
    print(f"I will get {round(rates[i] * wallet, 2)} {i} from the sale of {wallet} conicoins.")