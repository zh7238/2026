import random
import sys
from typing import List, Dict, Tuple
from enum import Enum
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QComboBox, QPushButton, QListWidget, QListWidgetItem,
    QGroupBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QColor


class MealTime(Enum):
    """用餐時間枚舉"""
    BREAKFAST = "早餐"
    LUNCH = "午餐"
    DINNER = "晚餐"
    SUPPER = "宵夜"


class CuisineType(Enum):
    """餐點類型枚舉"""
    UNLIMITED = "不限"
    CHINESE = "中式"
    WESTERN = "西式"
    FASTFOOD = "速食"
    BENTO = "便當"
    JAPANESE = "日式"
    THAI = "泰式"


# 中原大學徒步20分鐘以內（半徑約1.2km）的餐廳
RESTAURANTS = [
    {
        "name": "台風烤雞",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "麥當勞",
        "cuisine": CuisineType.WESTERN,
        "meal_times": [MealTime.BREAKFAST, MealTime.LUNCH, MealTime.DINNER, MealTime.SUPPER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "85度C",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.BREAKFAST, MealTime.LUNCH, MealTime.DINNER, MealTime.SUPPER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "湯品美味鍋-中原店",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "すき家",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "一番鍋",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "突點咖啡",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "摩斯漢堡",
        "cuisine": CuisineType.WESTERN,
        "meal_times": [MealTime.BREAKFAST, MealTime.LUNCH, MealTime.DINNER, MealTime.SUPPER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "CU部隊鍋&BBQ",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "東東麵館",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "信福炸豬排專賣店",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "Slobber思樂伯洋食總匯",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "22burger茶餐館",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "星巴克",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.BREAKFAST, MealTime.LUNCH, MealTime.DINNER, MealTime.SUPPER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "彭春妹客家麻糬",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "御冠園鮮肉湯包專賣店",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "世界豆漿店",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.BREAKFAST, MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "丘谷",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "八方雲集",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.BREAKFAST, MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "達美樂披薩",
        "cuisine": CuisineType.WESTERN,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER, MealTime.SUPPER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "月出販賣部",
        "cuisine": CuisineType.CHINESE,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "玩逗樹咖啡",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.BREAKFAST, MealTime.LUNCH, MealTime.DINNER, MealTime.SUPPER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "食玩天堂親子新樂園",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "阿英煎包",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "悠活早午餐",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.BREAKFAST, MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "麻子辣麻辣燙",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER, MealTime.SUPPER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "三家專業烤肉",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "發發",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "開源社香雞排",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER, MealTime.SUPPER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "味之屋",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "青蛙QQ黑糖粉圓專賣店",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER, MealTime.SUPPER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "姐妹麵館",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "鬼匠拉麵",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER, MealTime.SUPPER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "李記台中脆皮臭豆腐",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER, MealTime.SUPPER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "中原麵疙瘩",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "霸王基老闆油雞.醉雞",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "楚記福建炒麵",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "胖老爹美式炸雞",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER, MealTime.SUPPER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "飽福飯麵館",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "滝神 平價生魚片丼飯",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "罐罐鮮花烤奶茶",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "MR.CALETKA餐館",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "DAVID DINER 大衛好食",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "三顧茅廬麻辣滷味",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER, MealTime.SUPPER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "十三妹螺獅粉",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "台G店創始店",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "阿亮魯肉飯",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.BREAKFAST, MealTime.LUNCH, MealTime.DINNER, MealTime.SUPPER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "佰元鍋",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "168獨享鍋",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "Piepai Cafe’",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "廣東腸粉",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "小食光早餐店",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "大滷桶",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "粥大福",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "涮乃葉",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "散步咖啡",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "海頓咖啡",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "撈油水 港式菠蘿茶飲",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "餔饗麵對",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "大中華粥麵館",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "田野珈琲屋",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "Quán ăn Việt Nam",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "米炭火燒肉小酒館",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "弄塘bistro",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "蘇記大腸包小腸",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "金蘭小吃",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "胖嘟嘟現炸湯翅",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "馬來一哥",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "薯食好吃",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "滑龍粥",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "老師傅牛肉麵",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "一沐日",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "強尼兄弟健康廚房",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "Gray Room 灰房間",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "中埔烤肉",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "台南虱目魚",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "嘉義雞肉飯",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "食霸重慶麻辣火鍋",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "朝天椒麻辣鴛鴦火鍋店",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "隨主飡法式水煮專賣",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "珍味坊肉夾饃（老潼關)",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "吉焰串燒",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "鍋泰暖",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "小泰國海南雞飯",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "雷利咖喱",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "中原酥皮濃湯",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "陳記媽媽便當",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "海口鮮魚湯/朋淇早午餐",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "胖菓子pan.guozi",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "綠野鮮蹤",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "燒鳥串道",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "享檸專業手打檸檬茶",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "三串窟",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "阿忠豬血糕飲品",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "Y.J COFFEE 玉津咖啡",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "展翅當歸鴨",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "就是這味",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "排排坐 茶飲輕食",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "温馨早餐店",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "鄉堤早餐",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "Blue dream藍夢空間",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "阿恰烤飯糰",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "脆皮臭豆腐",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "簡單點",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "阿寶肉羹大王",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "大嗑",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "甘泉魚麵",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "小牧鍋minimoo",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "紅吱吱平價牛排館",
        "cuisine": CuisineType.WESTERN,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "パパ漢堡（88 Burger)",
        "cuisine": CuisineType.WESTERN,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "趙喜妹",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "無名小吃攤",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "大埔鐵板燒",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "吳記米粉湯",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "吾栖 Home Bistro",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "中原脆皮臭豆腐",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "壹玖柒玖",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "酉客棧 유주막 U Chicken Bistro",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "竹野燒肉飯",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "中原活蝦",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "橫濱牛排",
        "cuisine": CuisineType.WESTERN,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "杏好有仁",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "AGMA 烤肉工廠",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "茶瀚堂",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "大腸包小腸",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "SUNNY.3西班牙油條",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "炸雞的行家-半雞八兩",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "餵 湯泡飯",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "韓一館",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "煎茶苑",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "尚味早餐店",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "一品香滷味",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "陸予Logic Tea",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "味味香北平烤鴨",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "Chick輕客",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "一品 黑糖珍珠鮮奶",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "得來素蔬食早午餐",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "雞排一生",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "阿燁紅麵線",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "林永方手工湯包麵線",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "斗六當歸鴨",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "集英會牛肉麵館",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "巨林美而美",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "打爆豬韓式燒肉吃到飽",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "上官木桶鍋",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "笨港朝天雞",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "爭鮮",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "螺哩囉嗦",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "韓辛24H無人拉麵",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "中原第一家麻辣豆腐鴨血煲",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "唿唿哈點心專賣",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "孫東寶台式牛排",
        "cuisine": CuisineType.WESTERN,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "Q Burger",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "大A基隆廟口營養三明治",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "蚵嗲餅",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "泰愛了",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "阿秋鹹粥",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "小ㄚ頭早餐店",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "水餃小籠包",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "幽林",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "有一家麵店",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "拿坡里披薩",
        "cuisine": CuisineType.WESTERN,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "哈堡堡輕食早午餐",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "口吅品平價牛排",
        "cuisine": CuisineType.WESTERN,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "草地人牛排",
        "cuisine": CuisineType.WESTERN,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "鐵路沙威瑪",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "韓奶奶",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "斷腸人之大腸包小腸",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "喵宅MeowHouse",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "拉亞漢堡",
        "cuisine": CuisineType.WESTERN,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "亞美の豆漿大王",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "大漢草原 新彊羊肉串",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "吾饗麻辣臭豆腐",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "一品香便當",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "翻滾吧～糖炒栗子",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "美而美",
        "cuisine": CuisineType.WESTERN,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "瑞麟美而美",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "艾尚豆花",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "森沐日式食堂",
        "cuisine": CuisineType.JAPANESE,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "圓環肉羹",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "晨食司控",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "食麪",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "Master Of Tea 花茶大師",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "秋吉便當",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "大中原滷味",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "陽光煎匙",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "弘揚水餃牛肉麵館",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "這是你的Chill box",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "兆邑現炒館",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "APPLE活力早午餐",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "中福鍋燒麵",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "十盛奶茶專賣",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "六季鮮魚湯",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "尋MEAT炭火燒肉",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "頑餅",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "早啊早餐店",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "韓棧",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "豆花王",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "墨爾漢堡",
        "cuisine": CuisineType.WESTERN,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "咖喱就好啦",
        "cuisine": CuisineType.JAPANESE,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "愛妻先生",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "羽之鍋",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "原泰阿杜 音樂餐酒館",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "吃香喝辣福建炒麵",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "寶寶屋韓式料理",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "州味涼麵",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "萬名麵",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "尼好早午餐",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "慕森MuSen",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "找個地方cafe",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "小肥大馬餐室",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "豪秋吐司",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "TSU MI：啜麵",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "SU DAK 大口韓食",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "吉野烤肉飯",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "永和豆漿",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "8 Code鬆餅",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "漢堡邦",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "宜珍快餐",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "永祿小吃麵飯",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "粥品 飯糰 刈包",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "迷客夏",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "小木屋鬆餅",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "阿姨古早味蛋餅",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "川督極品麻辣臭豆腐",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "食厭世",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "食厭世",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "德式披薩",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "mymyfood麥麥屋 24H無人拉麵",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "中圓粥品&鍋燒",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "抖抖叫",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "奶奶的熊",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "茶學苑 Tea Arts",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "泰美味",
        "cuisine": CuisineType.THAI,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "功夫温泉",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "飲丹丘 In Dan Q",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "灶腳排骨",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "薰衣草-韓式海苔飯捲",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "東興素食",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "韓巷粉食小吃",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "不吃不可鹹水雞",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "餡實餃色",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "艿棠 Toast.cat早午餐",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "暖暖蒔光",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "點22",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "食搞玩",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "五桐號",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "御鼎牛排創意料理",
        "cuisine": CuisineType.WESTERN,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "龜記茗品",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "倆仁Two Bros 炒泡麵",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "藍色美而美",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "酒生閣",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "熊豆花",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "功夫茶 KUNGFUTEA",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "美焦咖啡",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "Amber 日式可麗餅&舒芙蕾",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "馥鄉蛋包飯",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "好了啦紅茶冰",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "路邊烤肉wildbbq",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "麻久製食所",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "拾參咖啡館",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "蕭大立米糕 排骨酥麵",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "六品閣 麵食館",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "有點東西",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "滿大碗滷味",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "妞妞雲泰美食",
        "cuisine": CuisineType.THAI,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "妞妞雲泰美食",
        "cuisine": CuisineType.THAI,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "樂富棧",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "翔大拉麵店",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "一起開丼&Ms.mo 奶酪小姐",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "双十八木",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "可不可熟成紅茶",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "兩把火干鍋",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "原萬名",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "素怡園素食自助餐",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "低欸賣甜點的",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "Robaku 印尼烤麵包",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "三媽臭臭鍋",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "焦糖楓串燒",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "吳家紅茶冰",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "扯厚腿",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "黑宅拉麵",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "熊樂火鍋",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "甯 咖啡 自家烘焙",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "紅茶大苑",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "樂野和風洋食屋",
        "cuisine": CuisineType.JAPANESE,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "八哥重慶酸辣粉",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "薇微一酵TAKE A SMILE",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "嘉香麵飯粥",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "Aniki阿尼基美式餐廳",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "好好早午餐",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "Verona 義式餐廳",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "阿迪早點",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "康櫻廣東粥",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "手工烤布蕾",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "香知有素",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "有飲 Youin",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "林記古意奶茶",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "亭仔腳",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "小螺莉螺螄粉",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "饗越食堂",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "菓點子",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "小米義式廚房",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "沐樂食堂",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "鐵三中螺螄粉 中原店",
        "cuisine": CuisineType.CHINESE,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "花田盛事築夢莊園",
        "cuisine": CuisineType.UNLIMITED,
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "price_range": (60, 350),
        "location": "桃園市中壢區"
    },
    {
        "name": "晨美好輕食早午餐",
        "cuisine": CuisineType.WESTERN,
        "meal_times": [MealTime.BREAKFAST, MealTime.LUNCH],
        "price_range": (80, 300),
        "location": "桃園市中壢區"
    },
]


def filter_restaurants(
    meal_time: MealTime,
    cuisine_type: CuisineType,
    budget_range: Tuple[int, int]
) -> List[Dict]:
    """根據條件篩選符合的餐廳"""
    filtered = []
    
    for restaurant in RESTAURANTS:
        # 檢查用餐時間
        if meal_time not in restaurant["meal_times"]:
            continue
        
        # 檢查餐點類型
        # 如果用戶選擇「不限」，或餐廳是「不限」，或餐廳類型與選擇相符，則通過
        restaurant_cuisine = restaurant["cuisine"]
        if (cuisine_type != CuisineType.UNLIMITED and 
            restaurant_cuisine != CuisineType.UNLIMITED and 
            cuisine_type != restaurant_cuisine):
            continue
        
        # 檢查預算範圍（檢查餐廳價格範圍是否與預算有重疊）
        rest_min, rest_max = restaurant["price_range"]
        budget_min, budget_max = budget_range
        if rest_min > budget_max or rest_max < budget_min:
            continue
        
        filtered.append(restaurant)
    
    return filtered


class RestaurantApp(QMainWindow):
    """餐廳推薦與隨機選擇系統 - PyQt6版本"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🍽️  餐廳推薦與隨機選擇系統")
        self.setGeometry(100, 100, 700, 700)
        self.current_filtered_restaurants = []
        self.init_ui()
    
    def init_ui(self):
        """初始化UI"""
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        # 標題
        title_label = QLabel("餐廳推薦與隨機選擇系統")
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title_label)
        
        # 選擇部分
        selection_group = QGroupBox("選擇條件")
        selection_layout = QVBoxLayout()
        
        # 用餐時間
        time_layout = QHBoxLayout()
        time_label = QLabel("用餐時間:")
        time_label.setMinimumWidth(80)
        self.meal_time_combo = QComboBox()
        self.meal_time_combo.addItems([meal.value for meal in MealTime])
        time_layout.addWidget(time_label)
        time_layout.addWidget(self.meal_time_combo)
        time_layout.addStretch()
        selection_layout.addLayout(time_layout)
        
        # 餐點類型
        cuisine_layout = QHBoxLayout()
        cuisine_label = QLabel("餐點類型:")
        cuisine_label.setMinimumWidth(80)
        self.cuisine_combo = QComboBox()
        self.cuisine_combo.addItems([cuisine.value for cuisine in CuisineType])
        cuisine_layout.addWidget(cuisine_label)
        cuisine_layout.addWidget(self.cuisine_combo)
        cuisine_layout.addStretch()
        selection_layout.addLayout(cuisine_layout)
        
        # 預算範圍
        budget_layout = QHBoxLayout()
        budget_label = QLabel("預算範圍:")
        budget_label.setMinimumWidth(80)
        self.budget_combo = QComboBox()
        self.budget_combo.addItems([
            "不限",
            "0-80元",
            "80-150元",
            "150-300元",
            "300元以上"
        ])
        self.budget_values = [
            (0, 10000),
            (0, 80),
            (80, 150),
            (150, 300),
            (300, 1000)
        ]
        budget_layout.addWidget(budget_label)
        budget_layout.addWidget(self.budget_combo)
        budget_layout.addStretch()
        selection_layout.addLayout(budget_layout)
        
        selection_group.setLayout(selection_layout)
        main_layout.addWidget(selection_group)
        
        # 按鈕部分
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)
        
        self.search_all_btn = QPushButton("全部列出")
        self.search_all_btn.clicked.connect(self.show_all_restaurants)
        self.search_all_btn.setMinimumHeight(35)
        button_layout.addWidget(self.search_all_btn)
        
        self.random_btn = QPushButton("隨機選擇")
        self.random_btn.clicked.connect(self.random_select)
        self.random_btn.setMinimumHeight(35)
        button_layout.addWidget(self.random_btn)
        
        self.clear_btn = QPushButton("清除結果")
        self.clear_btn.clicked.connect(self.clear_results)
        self.clear_btn.setMinimumHeight(35)
        button_layout.addWidget(self.clear_btn)
        
        main_layout.addLayout(button_layout)
        
        # 結果顯示區域
        result_group = QGroupBox("搜尋結果")
        result_layout = QVBoxLayout()
        
        self.result_list = QListWidget()
        self.result_list.setMinimumHeight(300)
        result_layout.addWidget(self.result_list)
        
        result_group.setLayout(result_layout)
        main_layout.addWidget(result_group)
        
        main_widget.setLayout(main_layout)
    
    def get_selected_conditions(self) -> Tuple[MealTime, CuisineType, Tuple[int, int]]:
        """取得用戶選擇的條件"""
        meal_time_text = self.meal_time_combo.currentText()
        meal_time = None
        for meal in MealTime:
            if meal.value == meal_time_text:
                meal_time = meal
                break
        
        cuisine_text = self.cuisine_combo.currentText()
        cuisine_type = None
        for cuisine in CuisineType:
            if cuisine.value == cuisine_text:
                cuisine_type = cuisine
                break
        
        budget_index = self.budget_combo.currentIndex()
        budget_range = self.budget_values[budget_index]
        
        return meal_time, cuisine_type, budget_range
    
    def show_all_restaurants(self):
        """全部列出模式"""
        meal_time, cuisine_type, budget_range = self.get_selected_conditions()
        
        filtered = filter_restaurants(meal_time, cuisine_type, budget_range)
        self.current_filtered_restaurants = filtered
        
        self.result_list.clear()
        
        if not filtered:
            item = QListWidgetItem("❌ 沒有符合條件的餐廳")
            item.setForeground(QColor("red"))
            self.result_list.addItem(item)
            return
        
        header = QListWidgetItem(f"✓ 找到 {len(filtered)} 家符合條件的餐廳\n")
        header_font = QFont()
        header_font.setBold(True)
        header.setFont(header_font)
        self.result_list.addItem(header)
        
        self.result_list.addItem("")  # 空行
        
        for i, restaurant in enumerate(filtered, 1):
            price_min, price_max = restaurant["price_range"]
            text = f"{i}. {restaurant['name']}\n   類型: {restaurant['cuisine'].value}\n   價格: {price_min}-{price_max}元"
            item = QListWidgetItem(text)
            self.result_list.addItem(item)
    
    def random_select(self):
        """隨機模式"""
        meal_time, cuisine_type, budget_range = self.get_selected_conditions()
        
        filtered = filter_restaurants(meal_time, cuisine_type, budget_range)
        self.current_filtered_restaurants = filtered
        
        self.result_list.clear()
        
        if not filtered:
            item = QListWidgetItem("❌ 沒有符合條件的餐廳")
            item.setForeground(QColor("red"))
            self.result_list.addItem(item)
            return
        
        restaurant = random.choice(filtered)
        price_min, price_max = restaurant["price_range"]
        
        result_text = f"✨ 系統為您隨機選擇：\n\n🎯 餐廳名稱: {restaurant['name']}\n\n🍲 餐點類型: {restaurant['cuisine'].value}\n\n💰 價格範圍: {price_min}-{price_max}元"
        
        item = QListWidgetItem(result_text)
        header_font = QFont()
        header_font.setPointSize(11)
        header_font.setBold(True)
        item.setFont(header_font)
        item.setForeground(QColor("darkgreen"))
        self.result_list.addItem(item)
    
    def clear_results(self):
        """清除結果"""
        self.result_list.clear()
        self.current_filtered_restaurants = []


def main():
    """主程序"""
    app = QApplication(sys.argv)
    window = RestaurantApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
