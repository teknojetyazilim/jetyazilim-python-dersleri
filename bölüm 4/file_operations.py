def write_to_file(filename,content):
    with open(filename,'w')as file:
        file.write(content)
    print(f"'{filename}'dosyasına yazıldı")

def read_from_file(filename):
    try:
        with open(filename,'r')as file:
            content = file.read()
        return content 
    except FileNotFoundError:
        return f"'{filename}'dosyası bulunamadı"