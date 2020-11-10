# Author:xqkang
# Date:2020/9/19 下午6:40
China = {
    "beijing": {
        "fengtai": ["beida", "beike"],
        "haidianqu": "qinghua",
        "fangshanqu": "beili",
    },
    "hebie": {
        "tangshan": "huali",
        "shijiazhuang": "tiedao",
    },
    "tianjin": {
        "hebei": "asd",
        "binhai": "tieddsaao",
    }
}

print(China)

China["beijing"]["fengtai"][1] = "shifan"

print(China)

print(China.keys())

print(China.values())

# setdefault有则不变，没有则添加
China.setdefault("being", { 1, 2 })
print(China)
