with open("newfile.txt","r",encoding="utf-8") as file:
    content = file.read()
    print(content)
    file.seek(0) #cursoru parantezdeki konuma yollar.
    print(file.tell()) #cursorun konumu
    