# Python self 用法教學 (一步一步來 - 以「狗」為例)
# 這是從教學文件中提取並組織的 Python 程式碼範例

print("--- 1. 什麼是 self？ ---")
# 這是一個「狗」的類別 (藍圖)
class Dog_Example1:
    # 定義一個「叫」的動作 (方法)
    # 當一隻狗「叫」的時候，self 就會代表那隻正在叫的狗
    def speak(self):
        # 在這個動作內部，self 就指向了呼叫這個動作的「那隻狗」物件
        print("汪汪！我是這隻狗。 (來自 Dog_Example1)")

# 首先，我們依照 Dog_Example1 藍圖，建立一個實際的狗物件，取名為 my_dog1
my_dog1 = Dog_Example1()

# 讓 my_dog1 這隻狗執行「叫」的動作
# Python 內部處理：Dog_Example1.speak(my_dog1)，所以 speak 方法中的 self 就是 my_dog1
my_dog1.speak()
print("-" * 20)

print("\n--- 2. self 如何運作？為什麼需要它來操作物件的資料？ ---")
class Dog_Example2: # 狗的藍圖 (類別)
    # 這是狗物件剛被建立時的「初始化」動作
    # 它負責設定新狗物件一開始的資料
    def __init__(self, name, breed):
        # self 代表正在被建立的那隻新狗物件
        # self.dog_name = name 的意思是：
        # 「給這隻狗 (self) 一個叫做 dog_name 的資料標籤 (屬性)，
        #   並把傳進來的 name (例如 "小黃") 存到這個標籤裡。」
        self.dog_name = name
        self.dog_breed = breed # 設定這隻狗的品種
        print(f"通知：一隻叫做 {self.dog_name} 的{self.dog_breed}誕生了！(來自 Dog_Example2 __init__)")

    # 介紹自己的動作 (方法)
    def introduce(self):
        # self 代表呼叫 introduce 動作的那隻狗
        # 所以 self.dog_name 就是那隻狗的 dog_name 資料 (名字)
        print(f"汪！我是 {self.dog_name}，一隻{self.dog_breed}。(來自 Dog_Example2 introduce)")

# 依照 Dog_Example2 藍圖建立兩隻不同的狗物件
dog1_ex2 = Dog_Example2("小黃", "柴犬") # Python 內部呼叫 Dog_Example2.__init__(dog1_ex2物件, "小黃", "柴犬")
dog2_ex2 = Dog_Example2("旺財", "黃金獵犬") # Python 內部呼叫 Dog_Example2.__init__(dog2_ex2物件, "旺財", "黃金獵犬")

dog1_ex2.introduce() # introduce 方法中的 self 代表 dog1_ex2
dog2_ex2.introduce() # introduce 方法中的 self 代表 dog2_ex2
print("-" * 20)

print("\n--- 3. 使用 self 設定和取得物件的「屬性」(資料) ---")
class Dog_Example3: # 狗的藍圖
    # 初始化動作：當一隻新狗物件被建立時執行
    def __init__(self, name, age):
        # self 代表這隻正在被建立的新狗物件
        self.dog_name = name    # 設定這隻狗的名字屬性
        self.dog_age = age      # 設定這隻狗的年齡屬性
        self.is_hungry = True   # 設定牠是否飢餓的屬性 (預設是餓的)
        print(f"通知：{self.dog_name} ({self.dog_age}歲) 加入了我們，牠現在很餓！(來自 Dog_Example3 __init__)")

    # 餵食的動作
    def feed(self):
        # self 代表呼叫 feed 動作的那隻狗
        if self.is_hungry:
            print(f"正在餵食 {self.dog_name}...")
            self.is_hungry = False # 修改這隻狗的 is_hungry 屬性
            print(f"{self.dog_name} 吃飽了！(來自 Dog_Example3 feed)")
        else:
            print(f"{self.dog_name} 現在不餓。(來自 Dog_Example3 feed)")

my_pet_dog_ex3 = Dog_Example3("Lucky", 3) # 建立一隻叫做 Lucky，3歲的狗物件
print(f"我的狗叫做 {my_pet_dog_ex3.dog_name}，牠 {my_pet_dog_ex3.dog_age} 歲了。")
print(f"Lucky 現在餓嗎？ {'餓' if my_pet_dog_ex3.is_hungry else '不餓'}")

my_pet_dog_ex3.feed() # 讓 my_pet_dog_ex3 物件執行餵食的動作
print(f"Lucky 現在餓嗎？ {'餓' if my_pet_dog_ex3.is_hungry else '不餓'}")
my_pet_dog_ex3.feed() # 再試著餵一次
print("-" * 20)

print("\n--- 4. 使用 self 呼叫同一個物件的其他動作 ---")
class Dog_Example4: # 狗的藍圖
    def __init__(self, name):
        self.dog_name = name
        self.energy_level = 100 # 初始能量值
        print(f"通知：活力充沛的 {self.dog_name} 登場！能量 {self.energy_level}。(來自 Dog_Example4 __init__)")

    # 一個檢查能量的 "內部" 動作
    def _check_energy(self):
        # self 代表呼叫 _check_energy 動作的那個狗
        print(f"{self.dog_name}：檢查能量... 目前能量 {self.energy_level}。(來自 Dog_Example4 _check_energy)")
        if self.energy_level > 20:
            return True
        else:
            print(f"{self.dog_name}：能量不足，需要休息！(來自 Dog_Example4 _check_energy)")
            return False

    # 玩耍的動作
    def play_fetch(self, times):
        # self 代表呼叫 play_fetch 動作的那個狗
        print(f"{self.dog_name} 準備開始玩撿球遊戲！(來自 Dog_Example4 play_fetch)")
        for i in range(times):
            if self._check_energy(): # 呼叫同一個狗 (self) 的 _check_energy 動作
                print(f"第 {i+1} 次撿球：{self.dog_name} 衝啊！撿到球了！(來自 Dog_Example4 play_fetch)")
                self.energy_level -= 15 # 玩耍會消耗能量
            else:
                print(f"{self.dog_name} 太累了，不能再玩了。(來自 Dog_Example4 play_fetch)")
                break
        print(f"{self.dog_name} 玩完了，目前能量 {self.energy_level}。(來自 Dog_Example4 play_fetch)")

active_dog_ex4 = Dog_Example4("皮蛋") # 建立一隻名為皮蛋的狗物件
active_dog_ex4.play_fetch(5) # 讓皮蛋玩5次撿球遊戲
print("-" * 20)

print("\n--- 5. self 是一個慣例名稱，不是「特殊保留字」 ---")
# 這裡的 PetBlueprint 例子來自教學文件第5點，用來說明 self 只是慣例
class PetBlueprint: # 一個寵物的藍圖
    def __init__(this_pet, initial_name): # 故意不用 self，但 this_pet 扮演相同角色
        # this_pet 代表新建立的寵物物件
        this_pet.pet_name = initial_name # 設定這個寵物的名字資料
        print(f"通知：新寵物 {this_pet.pet_name} 已使用 PetBlueprint 建立。(來自 PetBlueprint __init__)")

    def show_name(this_pet): # this_pet 代表呼叫此動作的寵物物件
        print(f"我的名字是 {this_pet.pet_name}。(來自 PetBlueprint show_name)")

my_dog_from_blueprint_ex5 = PetBlueprint("豆豆") # 建立物件，this_pet 在 __init__ 中就是 my_dog_from_blueprint_ex5
my_dog_from_blueprint_ex5.show_name()        # 呼叫動作，this_pet 在 show_name 中就是 my_dog_from_blueprint_ex5
print("-" * 20)

print("\n教學範例結束。")
