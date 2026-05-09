import json
from datetime import datetime

# 今日时间
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 模拟稀土价格数据（后续对接真实SMM接口）
data = {
    "update_time": now,
    "day": [
        {"name": "金属镨钕", "price": "95.00", "change": "▲ 0.56", "class": "up"},
        {"name": "氧化镨钕", "price": "77.25", "change": "▲ 0.67", "class": "up"},
        {"name": "氧化镨", "price": "83.00", "change": "▲ 0.25", "class": "up"},
        {"name": "氧化钕", "price": "82.50", "change": "▲ 0.25", "class": "up"},
        {"name": "氧化镝", "price": "137.50", "change": "▲ 0.09", "class": "up"},
        {"name": "氧化铽", "price": "610.14", "change": "▲ 0.54", "class": "up"},
        {"name": "氧化钇", "price": "25.75", "change": "--", "class": "flat"},
        {"name": "氧化钬", "price": "55.25", "change": "--", "class": "flat"}
    ],
    "week": [
        {"name": "金属镨钕", "change": "▲ 0.80", "class": "up"},
        {"name": "氧化镨钕", "change": "▲ 0.75", "class": "up"},
        {"name": "氧化镨", "change": "▲ 0.80", "class": "up"},
        {"name": "氧化钕", "change": "▲ 0.70", "class": "up"}
    ],
    "month": [
        {"name": "金属镨钕", "change": "▲ 1.50", "class": "up"},
        {"name": "氧化镨钕", "change": "▲ 1.25", "class": "up"},
        {"name": "氧化镨", "change": "▲ 1.50", "class": "up"},
        {"name": "氧化钕", "change": "▲ 1.70", "class": "up"}
    ]
}

# 写入 data.json
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ 数据更新完成：", now)
