try:
    with open('a.txt', 'r')as f:
        content = f.read()
except FileNotFoundError:
    print("Dosya Bulunamadı")