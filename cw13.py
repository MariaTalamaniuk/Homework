def process_order(*items, **options):
    total = sum(items)

    discount = options.get('discount', 0)
    gift_card = options.get('gift_card', 0)
    free_shipping = options.get('free_shipping', False)

    if discount:
        discount_amount = total * (discount / 100)
        total -= discount_amount

    total -= gift_card

    if not free_shipping:
        shipping_cost = 50
        total += shipping_cost

    total = max(total, 0)

    return total


order_total = process_order(100, 200, 50, discount=10, gift_card=30, free_shipping=True)
print(f"Кінцева сума замовлення: {order_total} грн")
