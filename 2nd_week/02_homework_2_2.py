shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

shop_menus_set = set(shop_menus)

def is_available_to_order(menus, order):
    return order in menus

for shop_order in shop_orders:
    if not is_available_to_order(shop_menus_set, shop_order):
        print(False)
        break
else :
    print(True)