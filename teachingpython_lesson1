# 我的數位夥伴製造機 - Python 教學專案
# 目標：理解 self 和取得屬性 (get attribute)

# --- 階段一：我是誰？我的名字是？ ---
print("--- 階段一：基本夥伴 ---")
class DigitalPal_V1:
    # __init__ 方法就像是小夥伴的「出生」過程
    # 當一個新的 DigitalPal_V1 被創造時，這個方法會自動執行
    # `self` 代表「這個正在被創造出來的小夥伴實體」
    # `name_param` 是我們給小夥伴取的名字參數
    def __init__(self, name_param):
        print(f"[V1 LOG] 一個新的數位夥伴誕生了！正在設定名字...")
        # 這裡，我們告訴「這個小夥伴」(self)，
        # 「你的名字」(self.name) 就是我們給你的 `name_param`
        # 這就是在「設定屬性」(defining an attribute)
        self.name = name_param
        print(f"[V1 LOG] 太棒了！{self.name} 準備好了！")

# 製造第一個小夥伴
# 這時候，DigitalPal_V1 裡面的 `self` 就會指向 `pal1_v1` 這個實體
# "皮皮" 這個字串會傳給 `__init__` 方法中的 `name_param`
pal1_v1 = DigitalPal_V1("皮皮")

# 從外部取得 pal1_v1 這個物件的 name 屬性
# 這就是「取得屬性」(getting an attribute)
print(f"我第一個夥伴的名字是: {pal1_v1.name}")
print("-" * 30 + "\n")


# --- 階段二：我的夥伴不只名字，還有超能力！ ---
print("--- 階段二：更多特色的夥伴 ---")
class DigitalPal_V2:
    def __init__(self, name_param, species_param, color_param):
        print(f"[V2 LOG] 開始創造新的數位夥伴...")
        # `self` 代表這個正在被創造的夥伴
        # 設定這個夥伴的名字
        self.name = name_param
        # 設定這個夥伴的種類
        self.species = species_param
        # 設定這個夥伴的顏色
        self.color = color_param
        print(f"[V2 LOG] 夥伴 {self.name} ({self.species}, {self.color}色) 創造完畢！")

# 製造更多不同的小夥伴
pal_cat_v2 = DigitalPal_V2("咪咪", "貓咪", "橘色")
pal_dog_v2 = DigitalPal_V2("旺財", "狗狗", "黑色")

# 看看他們各自的特色 (取得多個屬性)
print(f"{pal_cat_v2.name} 是一隻 {pal_cat_v2.color}的 {pal_cat_v2.species}。")
print(f"{pal_dog_v2.name} 是一隻 {pal_dog_v2.color}的 {pal_dog_v2.species}。")
# 強調：`self` 讓每個物件都能管理好「自己的」資料，不會混淆。
# pal_cat_v2.species 是咪咪的種類，因為在創造咪咪時，self.species 的 self 指向咪咪。
# pal_dog_v2.species 是旺財的種類，因為在創造旺財時，self.species 的 self 指向旺財。
print("-" * 30 + "\n")


# --- 階段三：夥伴的自我介紹 ---
print("--- 階段三：夥伴的自我介紹方法 ---")
class DigitalPal_V3:
    def __init__(self, name_param, species_param, color_param):
        self.name = name_param
        self.species = species_param
        self.color = color_param
        print(f"[V3 LOG] 夥伴 {self.name} ({self.species}, {self.color}色) 創造完畢！")

    # 這是一個「方法」(method)，是物件可以做的事情
    # 注意第一個參數還是 `self`！
    # 這表示當物件呼叫這個方法時，它知道是在對「自己」操作
    def introduce_myself(self):
        # 在方法內部，使用 `self.attribute_name` 來取得「自己的」屬性
        print(f"大家好！我是 {self.name}，")
        print(f"我是一隻可愛的 {self.color}色 {self.species}。")

pal_cat_v3 = DigitalPal_V3("咪咪", "貓咪", "橘色")
pal_dog_v3 = DigitalPal_V3("旺財", "狗狗", "黑色")

print("\n--- 咪咪的自我介紹 (V3) ---")
# 當呼叫 pal_cat_v3.introduce_myself() 時：
# Python 會自動把 pal_cat_v3 這個物件傳給 introduce_myself 方法的 self 參數
# 所以在 introduce_myself 內部，self.name 就會是 pal_cat_v3 的名字 "咪咪"
pal_cat_v3.introduce_myself()

print("\n--- 旺財的自我介紹 (V3) ---")
# 同樣地，當呼叫 pal_dog_v3.introduce_myself() 時：
# introduce_myself 內部的 self 會是 pal_dog_v3 這個物件
pal_dog_v3.introduce_myself()
print("-" * 30 + "\n")


# --- 階段四：夥伴的秘密檔案 (Getter 方法) ---
print("--- 階段四：透過 Getter 方法取得屬性 ---")
class DigitalPal_V4:
    def __init__(self, name_param, species_param, color_param):
        self.name = name_param
        self.species = species_param
        self.color = color_param
        # 假設夥伴有一個秘密的「能量值」，不希望外面直接改動或看到原始數值
        # 前面加底線 `_` 通常表示這是一個「內部使用」或「受保護」的屬性 (慣例)
        self._energy = 100
        print(f"[V4 LOG] 夥伴 {self.name} ({self.species}, {self.color}色, 初始能量: {self._energy}) 創造完畢！")


    def introduce_myself(self):
        print(f"大家好！我是 {self.name}，我是一隻可愛的 {self.color}色 {self.species}。")

    # 官方通道 (Getter Method)：取得名字
    def get_name(self):
        # 在這裡，`self` 指向呼叫這個方法的物件
        # 它回傳「自己的」名字
        print(f"[V4 Getter] {self.name} 正在透過 get_name() 提供名字...")
        return self.name

    # 官方通道 (Getter Method)：取得種類
    def get_species(self):
        print(f"[V4 Getter] {self.name} 正在透過 get_species() 提供種類...")
        return self.species

    # 官方通道 (Getter Method)：取得顏色
    def get_color(self):
        print(f"[V4 Getter] {self.name} 正在透過 get_color() 提供顏色...")
        return self.color

    # 官方通道 (Getter Method)：取得能量狀態 (不是直接回傳數值)
    def get_energy_status(self):
        print(f"[V4 Getter] {self.name} 正在透過 get_energy_status() 提供能量狀態...")
        if self._energy > 70:
            return f"{self.name} 現在活力充沛！(能量 > 70)"
        elif self._energy > 30:
            return f"{self.name} 有點累了...(能量 31-70)"
        else:
            return f"{self.name} 快沒電了！(能量 <= 30)"

    # 假設有一個方法會消耗能量
    def perform_trick(self, trick_name):
        if self._energy >= 20:
            print(f"{self.name} 表演了 {trick_name}！消耗了 20 點能量。")
            self._energy -= 20
        else:
            print(f"{self.name} 能量不足，無法表演 {trick_name}。")


pal_hero_v4 = DigitalPal_V4("奇異果", "超級英雄鳥", "綠色")

# 透過 getter 方法取得屬性
hero_name = pal_hero_v4.get_name()
hero_species = pal_hero_v4.get_species()
hero_color = pal_hero_v4.get_color()

print(f"\n我的英雄夥伴叫做 {hero_name}。")
print(f"他是一隻 {hero_species}，有著帥氣的 {hero_color} 外表。")
print(pal_hero_v4.get_energy_status())

pal_hero_v4.perform_trick("空中翻轉")
print(pal_hero_v4.get_energy_status())

pal_hero_v4.perform_trick("高速俯衝")
pal_hero_v4.perform_trick("唱歌")
pal_hero_v4.perform_trick("隱形")
print(pal_hero_v4.get_energy_status())
pal_hero_v4.perform_trick("瞬間移動") # 應該會能量不足

# 雖然我們仍然可以這樣「直接」存取 (如果屬性名稱沒有用雙底線開頭做名稱修飾 name mangling)
# print(f"\n直接存取名字: {pal_hero_v4.name}")
# print(f"直接存取內部能量: {pal_hero_v4._energy}") # 可以存取，但好習慣是透過 getter
# 但是使用 getter 是一種好習慣，未來更有彈性，例如你想在取值前做一些檢查或格式化。
print("-" * 30 + "\n")


# --- 階段五：深入理解 `self` 的本質 ---
print("--- 階段五：`self` 的小實驗 ---")
# 再次強調：這只是為了證明 `self` 是慣例，平常寫程式千萬不要這樣做！
class ExperimentalPal:
    # 把 self 換成 this_object
    def __init__(this_object, name_param):
        print(f"[EXP LOG] 實驗開始，用 'this_object' 代替 'self'。")
        this_object.name = name_param # 這裡也要跟著改

    # 這裡也要改
    def say_my_name(this_object):
        print(f"我的名字是: {this_object.name}") # 這裡也要改

exp_pal = ExperimentalPal("小實驗家")
exp_pal.say_my_name()
print(f"直接存取實驗夥伴的名字: {exp_pal.name}")

print("\n思考：當我們呼叫 exp_pal.say_my_name() 時，Python 實際上做了什麼？")
print("它類似於執行了 ExperimentalPal.say_my_name(exp_pal)。")
print("所以 exp_pal 這個物件本身，被當作第一個參數傳給了 say_my_name 方法中名為 'this_object' 的參數。")
print("-" * 30 + "\n")

print("教學專案結束！希望你對 self 和取得屬性有更深的理解！")

