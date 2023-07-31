chigal={}

name = input("Oyuncunun adı: ")
surname = input("Oyuncunun soyadı: ")
nickname = input("Oyuncunun kullanıcı adı: ")
rank = input("Oyuncunun rütbesi: ")

chigal.update({
    nickname: {
        "ad":name,
        "soyad":surname,
        "rutbe":rank
    }
})
name = input("Oyuncunun adı: ")
surname = input("Oyuncunun soyadı: ")
nickname = input("Oyuncunun kullanıcı adı: ")
rank = input("Oyuncunun rütbesi: ")

chigal.update({
    nickname: {
        "ad":name,
        "soyad":surname,
        "rutbe":rank
    }
})
name = input("Oyuncunun adı: ")
surname = input("Oyuncunun soyadı: ")
nickname = input("Oyuncunun kullanıcı adı: ")
rank = input("Oyuncunun rütbesi: ")

chigal.update({
    nickname: {
        "ad":name,
        "soyad":surname,
        "rutbe":rank
    }
})
name = input("Oyuncunun adı: ")
surname = input("Oyuncunun soyadı: ")
nickname = input("Oyuncunun kullanıcı adı: ")
rank = input("Oyuncunun rütbesi: ")

chigal.update({
    nickname: {
        "ad":name,
        "soyad":surname,
        "rutbe":rank
    }
})


print(chigal)

nick = input("Aramak istediğiniz oyuncunun kullanıcı adını giriniz: ")
csgo = chigal[nick]

print(f"Aradığınız {nick} kullanıcı adlı oyuncunun adı {csgo['ad']} soyadı {csgo['soyad']} ve rütbesi {csgo['rutbe']}. ")


