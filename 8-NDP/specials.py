class Movie():
    def __init__(self, title, dir, duration):
        self.title = title
        self.dir = dir
        self.duration = duration
    
    def __str__(self):
        return f"{self.title} by {self.dir}"
    
    def __len__(self):
        return self.duration
    
    def __del__(self):
        print("Film silindi")



m = Movie("Django Unchained","Tarantino",3)

print(str(m))
print(len(m))
del m
