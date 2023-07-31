website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

courseLen = len(course)

print(courseLen)
print(website[7:10])
print(website[-3:courseLen-1])
print(course[0:15]+" " +course[-15:])
print(course[::-1])

name, surname, age, job = "Bora", "Yılmaz", 32, "mühendis"

print(f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}.")

s = "Hello world"


#print(s[:6]+"W"+s[7:])
print(s.replace("w","W"))


string = "abc" * 3

print(string)
