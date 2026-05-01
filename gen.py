import json
import random

TOTAL_DATA = 10000

categories = {
    "ayam_goreng": 107,
    "ayam_pop": 113,
    "daging_rendang": 104,
    "dendeng_batokok": 109,
    "gulai_ikan": 111,
    "gulai_tambusu": 103,
    "gulai_tunjang": 119,
    "telur_balado": 111,
    "telur_dadar": 116
}

name_prefix = [
    "Warung",
    "Rumah Makan",
    "Dapoer",
    "Kedai",
    "Pondok",
    "Lapau",
    "Depot",
    "Resto"
]

name_suffix = [
    "Minang Jaya",
    "Mak Uni",
    "Bundo Kanduang",
    "Sederhana",
    "Rasa Nikmat",
    "Mak Etek",
    "Padang Asli",
    "Pagi Sore",
    "Santan Emas",
    "Lamak Bana",
    "Dapur Nusantara",
    "Raso Bana"
]

streets = [
    "Jl. Sudirman",
    "Jl. Gatot Subroto",
    "Jl. Raya Hankam",
    "Jl. Merdeka",
    "Jl. Ahmad Yani",
    "Jl. Diponegoro",
    "Jl. Veteran",
    "Jl. Soekarno Hatta"
]

cities = [
    "Jakarta",
    "Bandung",
    "Bekasi",
    "Bogor",
    "Depok",
    "Surabaya",
    "Padang",
    "Medan",
    "Yogyakarta",
    "Semarang"
]

open_hours = [
    "07:00 - 15:00",
    "08:00 - 16:00",
    "09:00 - 18:00",
    "10:00 - 20:00",
    "24 Jam"
]


# =========================
# DESCRIPTION ENGINE
# =========================
def pretty_food(category):
    return category.replace("_", " ")


desc_opening = [
    "{name} menghadirkan sajian {food} dengan cita rasa autentik yang kaya akan rempah khas Indonesia.",
    "Bagi pecinta kuliner Nusantara, {name} menawarkan menu unggulan berupa {food} yang menggugah selera.",
    "{name} dikenal melalui hidangan {food} yang memiliki karakter rasa khas dan aroma yang menggoda.",
    "Mengusung konsep kuliner tradisional, {name} menyajikan menu {food} dengan kualitas rasa yang konsisten.",
    "{name} menjadi salah satu pilihan kuliner menarik dengan sajian andalan berupa {food}.",
    "Sebagai merchant kuliner lokal, {name} menghadirkan menu {food} dengan pengolahan yang matang dan penuh cita rasa."
]

desc_quality = [
    "Setiap hidangan dibuat menggunakan bahan pilihan yang segar dengan proses memasak yang memperhatikan kualitas rasa.",
    "Kombinasi bumbu yang seimbang menghasilkan rasa gurih, kaya aroma, dan cocok untuk berbagai selera.",
    "Pemilihan bahan baku berkualitas membuat setiap sajian memiliki rasa yang lebih fresh dan tekstur yang memuaskan.",
    "Proses pengolahan dilakukan secara teliti agar menghasilkan hidangan dengan rasa autentik dan konsisten.",
    "Setiap menu diracik menggunakan resep pilihan yang menjaga kekayaan rasa tradisional.",
    "Perpaduan teknik memasak yang tepat dan bahan berkualitas menghadirkan pengalaman rasa yang lebih berkesan."
]

desc_vibe = [
    "Suasana tempat yang nyaman menjadikannya cocok untuk makan bersama keluarga, teman, maupun rekan kerja.",
    "Merchant ini cocok dijadikan destinasi makan siang, makan malam, ataupun sekadar menikmati hidangan favorit.",
    "Dengan pelayanan yang ramah serta penyajian yang menarik, pengalaman bersantap menjadi semakin menyenangkan.",
    "Tempat ini menawarkan pengalaman kuliner yang sederhana namun tetap memberikan kesan yang memorable.",
    "Lingkungan yang bersih dan suasana yang hangat menambah kenyamanan saat menikmati hidangan.",
    "Cocok bagi pelanggan yang mencari pengalaman makan yang santai namun tetap berkualitas."
]

desc_extra = [
    "Selain menu utama, tersedia pula berbagai pilihan pelengkap yang menambah variasi pengalaman bersantap.",
    "Porsi yang disajikan juga dirancang cukup memuaskan sehingga cocok dinikmati dalam berbagai kesempatan.",
    "Merchant ini juga dikenal menjaga konsistensi rasa pada setiap sajian yang dihidangkan.",
    "Fokus pada kualitas dan kepuasan pelanggan menjadi salah satu nilai utama merchant ini.",
    "Cita rasa yang khas membuat sajian di tempat ini mudah dikenali oleh para pelanggan setianya.",
    ""
]

desc_closing = [
    "Tidak heran apabila merchant ini menjadi salah satu pilihan favorit banyak pelanggan.",
    "Kombinasi rasa, kualitas, dan kenyamanan membuat tempat ini memiliki daya tarik tersendiri.",
    "Dengan kualitas yang terus dijaga, merchant ini layak menjadi referensi kuliner pilihan.",
    "Hal tersebut menjadikan merchant ini menarik untuk dikunjungi kembali di kesempatan berikutnya.",
    "Perpaduan seluruh elemen tersebut menjadikan pengalaman kuliner terasa lebih lengkap.",
    "Semua unsur tersebut membuat merchant ini tampil sebagai salah satu destinasi kuliner yang patut dicoba."
]


def make_description(name, category):
    food = pretty_food(category)

    parts = [
        random.choice(desc_opening).format(name=name, food=food),
        random.choice(desc_quality),
        random.choice(desc_vibe),
    ]

    if random.random() < 0.65:
        extra = random.choice(desc_extra)
        if extra:
            parts.append(extra)

    parts.append(random.choice(desc_closing))

    return " ".join(parts)


# =========================
# GENERATOR ENGINE
# =========================
def random_price():
    low = random.randint(8, 40)
    high = random.randint(low + 5, low + 80)
    return f"Rp{low}k - Rp{high}k"


def indo_coordinate():
    lat = random.uniform(-11.0, 6.0)
    lng = random.uniform(95.0, 141.0)
    return lat, lng


def img_path(category):
    max_file = categories[category]
    n = random.randint(1, max_file)
    return f"img/{category}/{category} ({n}).jpg"


def make_gallery(category):
    count = random.randint(2, 5)
    return [img_path(category) for _ in range(count)]


def make_name():
    return f"{random.choice(name_prefix)} {random.choice(name_suffix)}"


def make_address():
    return (
        f"{random.choice(streets)} No.{random.randint(1,250)}, "
        f"{random.choice(cities)}"
    )


# =========================
# BUILD DATA
# =========================
personnel = {}

for i in range(1, TOTAL_DATA + 1):
    sn = f"FD{i:03}"
    category = random.choice(list(categories.keys()))
    merchant_name = make_name()

    premium = random.random() < 0.25
    lat, lng = indo_coordinate()

    profile = img_path(category)

    if premium:
        banner = img_path(category)
        gallery = make_gallery(category)
        tier = "premium"
    else:
        banner = ""
        gallery = []
        tier = "free"

    personnel[sn] = {
        "name": merchant_name,
        "sn": sn,
        "tier": tier,
        "verified": random.random() < 0.35,

        "profile": profile,
        "banner": banner,
        "gallery": gallery,

        "description": make_description(merchant_name, category),

        "address": make_address(),
        "openHours": random.choice(open_hours),
        "category": category,
        "priceRange": random_price(),

        "lat": lat,
        "lng": lng
    }


data = {
    "personnel": personnel
}

with open(
    r"C:\Users\Furru\Downloads\dummy_foodnet.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("done -> dummy_foodnet.json")