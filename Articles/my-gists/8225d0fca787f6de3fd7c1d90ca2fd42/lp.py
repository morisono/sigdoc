import typer
from scipy.optimize import linprog

def calculate_min_payment(items):
    num_items = len(items)

    # 商品価格
    prices = [item["price"] for item in items]

    # 為替レート
    rate_usd_jpy = 151.30

    # チェックアウト時の通貨ごとの支払額
    prices_usd = [price if i == 0 or i == 3 else price / rate_usd_jpy for i, price in enumerate(prices)]
    prices_jpy = [price * rate_usd_jpy if i == 1 or i == 2 else price for i, price in enumerate(prices)]

    # 線形計画問題を解く
    result_usd = linprog(prices_usd, method='simplex', bounds=[(0, None)] * num_items,
                         A_ub=[[-min_purchase_usd[j] if i == j else 0 for j in range(num_items)] for i in range(len(min_purchase_usd))],
                         b_ub=[-discount for discount in discounts_usd])

    result_jpy = linprog(prices_jpy, method='simplex', bounds=[(0, None)] * num_items,
                         A_ub=[[-min_purchase_jpy[j] if i == j else 0 for j in range(num_items)] for i in range(len(min_purchase_jpy))],
                         b_ub=[-discount for discount in discounts_jpy])

    return result_usd, result_jpy

def main():
    typer.echo("Enter information for each item. Type 'done' when finished.")

    items = []
    while True:
        item_name = typer.prompt("Enter item name:")
        if item_name.lower() == 'done':
            break

        item_price = typer.prompt("Enter item price:")
        items.append({"name": item_name, "price": float(item_price)})

    result_usd, result_jpy = calculate_min_payment(items)

    typer.echo("\nUSD Result:")
    typer.echo(result_usd)

    typer.echo("\nJPY Result:")
    typer.echo(result_jpy)

if __name__ == "__main__":
    typer.run(main)
