shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

shop_menus.sort()

def is_available_to_order(menus, order):

    left_idx = 0
    mid_idx = len(shop_menus) // 2
    right_idx = len(shop_menus) - 1
    while left_idx <= right_idx:
        if shop_menus[mid_idx] == order:
            return True
        elif shop_menus[mid_idx] > order:
            right_idx = mid_idx - 1
        else:
            left_idx = mid_idx + 1
        mid_idx = ((right_idx + left_idx) // 2)

    return False

for shop_order in shop_orders:
    if not is_available_to_order(shop_menus, shop_order):
        print(False)
        break
else :
    print(True)