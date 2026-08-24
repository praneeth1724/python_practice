def rocket_countdown(n):
    print(f"countdown current number {n}")
    if n > 0:
        rocket_countdown(n-1)
    elif n == 0:
        print("🚀 Blast off!")


rocket_countdown(7)
