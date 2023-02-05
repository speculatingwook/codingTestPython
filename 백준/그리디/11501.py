def solution(T):
    for _ in range(T):
        stock_count = int(input())
        stock_price_list = list(map(int, input().split(" ")))
        print(get_max_profit(stock_price_list))


def get_max_profit(stock_list):
    total_profit = 0

    for current in range(len(stock_list)):
        difference = [0] * len(stock_list)

        for future in range(current + 1, len(stock_list)):
            difference[future] = stock_list[future] - stock_list[current]

            if difference[future] < 0:
                difference[future] = 0

        total_profit += max(difference)
    return total_profit


TestCase = int(input())
solution(TestCase)
