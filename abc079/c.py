A, B, C, D = map(int, list(input()))

for op1 in ['+', '-']:
    for op2 in ['+', '-']:
        for op3 in ['+', '-']:
            ans = A + B if op1 == '+' else A - B
            ans = ans + C if op2 == '+' else ans - C
            ans = ans + D if op3 == '+' else ans - D
            if ans == 7:
                print(f"{A}{op1}{B}{op2}{C}{op3}{D}=7")
                exit(0)
