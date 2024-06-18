import file_operations as fo
user_input = input("Dosyaya yazmak istediğiniz metni giriniz lütfen")

filename = "deneme.txt"

fo.write_to_file(filename,user_input)

file_contenct = fo.read_from_file(filename)
print( f"'{filename}'dosyanın içeriği \n {file_contenct}" )