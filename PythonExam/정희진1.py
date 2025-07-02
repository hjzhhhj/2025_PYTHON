t = ("가", 170), ("나", 165), ("다", 180), ("라", 160)
d = dict(t)

for k, v in d.items():
    if d[k] >= 170:
        print(f"{k} ({v})")
