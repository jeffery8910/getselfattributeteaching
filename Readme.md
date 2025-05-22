## **Python** self **用法教學 (一步一步來 \- 以「狗」為例)**

在 Python 程式設計中，self 是一個非常重要的概念，尤其當我們開始設計和使用自己定義的「東西類型」時。它代表「那個特定的東西本身」。讓我們一步一步來學習它。

**開始之前：先聊聊「藍圖」和「實際做出來的東西」**

在 Python 或很多程式設計方式中，我們常常會先定義一個「**藍圖**」。這個藍圖描述了某一類事物共同擁有的**資料（特徵）和可以執行的動作（功能）**。在程式術語中，這種「藍圖」被稱為「**類別**」(英文是 class)。

例如，我們可以設計一個「狗」的類別（藍圖）。這個藍圖可能會說：

1. 每隻狗都有一些資料，像是「名字」、「品種」（這些就是狗的「**屬性**」，英文是 attribute）。  
2. 每隻狗都能做一些動作，像是「叫」、「搖尾巴」（這些就是狗可以執行的「**方法**」，英文是 method）。

然後，依照這個「狗」的類別（藍圖），我們可以實際創造出「**一隻隻的狗**」。每一隻依藍圖實際創造出來的狗，就是這個類別的一個「**物件**」(英文是 object)，有時候也稱為「**實體**」(英文是 instance，可以想像成「實際的例子」)。

比如，我們可以有一隻叫做「小黃」的狗物件，和另一隻叫做「小白」的狗物件。牠們都是依照「狗」這個類別藍圖製造出來的實際成品。

self 這個詞，就是用在類別所定義的方法（動作）裡面，用來代表「**呼叫這個動作的那個特定的物件**」—— 也就是說，如果「小黃」這隻狗在叫，那麼在叫的方法執行時，self 就代表「小黃」；如果「小白」在叫，self 就代表「小白」。

### **1\. 什麼是** self**？以及它為何能「自動」代表那個物件？**

簡單來說，當你依照一個類別（藍圖）做出一個實際的物件（成品）後，self 在這個物件執行它自己的動作（方法）時，就是指「那個物件本身」。

self **為何能「自動」代表那個物件？**

這不是 self 本身有什麼特殊魔法，而是 Python **呼叫物件動作（方法）的方式** 所內建的機制。當你讓一個物件去執行它的動作時，例如 my\_dog.speak()（讓 my\_dog 這隻狗去叫），Python 在「幕後」會自動做一個處理：

1. Python 看到你希望 my\_dog 這個**物件**去執行 speak 這個動作。  
2. 它會找到 my\_dog 所屬的類別（藍圖）中定義的 speak 動作。  
3. 最關鍵的一步：Python 會**自動地、不著痕跡地**將 my\_dog 這個物件本身，作為**第一個資料**傳遞給該動作。  
4. 在動作（方法）的定義中，我們依照慣例將這個自動傳入的第一個資料命名為 self。

所以，並不是 self 自己跑去「指向」什麼，而是 Python 的運作機制**主動把「做事的這個物件」送給了動作的第一個接收位置 (也就是** self**)**。這就像一個內建的規則，每次你讓物件做動作時都會這樣發生。

這裡有一個圖示說明這個「幕後」過程：

\[Image of ASCII art explaining Python's "behind-the-scenes" mechanism for method calls\]

當你寫 (You write):  
my\_dog.speak()  
   │  
   │ (這是你對 'my\_dog' 這個物件發出的指令，叫它做出 'speak' 動作)  
   ▼  
┌──────────────────────┐  
│ 物件: my\_dog         │  
│ (一隻特定的狗)       │  
└──────────────────────┘  
   │  
   │ Python 看到這個，並在內部做了類似這樣的轉換：  
   ▼  
Dog.speak(my\_dog)  \<── 關鍵步驟！ (Dog 是類別/藍圖的名稱)  
   │      ▲  
   │      │  
   │      └─ 物件 'my\_dog' 被「自動地」  
   │         作為第一個資料傳遞進去。  
   ▼  
┌───────────────────────────────────┐  
│ 在 Dog 類別（藍圖）的 speak 動作內部：│  
│                                   │  
│ def speak(self):                  │  
│            ▲                      │  
│            │                      │  
│            └─ 這個 'self' 現在就代表│  
│               'my\_dog' 這個物件   │  
│   print("汪汪！")                  │  
└───────────────────────────────────┘


現在，讓我們來看程式碼範例：
```python
\# 這是一個「狗」的類別 (藍圖)  
class Dog:  
    \# 定義一個「叫」的動作 (方法)  
    \# 當一隻狗「叫」的時候，self 就會代表那隻正在叫的狗  
    def speak(self):  
        \# 在這個動作內部，self 就指向了呼叫這個動作的「那隻狗」物件  
        print("汪汪！我是這隻狗。")

\# 首先，我們依照 Dog 藍圖，建立一個實際的狗物件，取名為 my\_dog  
my\_dog \= Dog()

\# 讓 my\_dog 這隻狗執行「叫」的動作  
\# Python 內部處理：Dog.speak(my\_dog)，所以 speak 方法中的 self 就是 my\_dog  
my\_dog.speak()
```
在這個例子中，當 my\_dog.speak() 被呼叫時，speak 方法中的 self 就代表 my\_dog 這個特定的狗物件。

* **建立物件**：my\_dog \= Dog() 這一行程式碼會依照 Dog 類別（藍圖）創造出一個實際的狗物件，並讓 my\_dog 這個名字指向它。  
* **呼叫動作**：當你執行 my\_dog.speak() 時，你是在告訴 Python：「嘿，請 my\_dog 這個物件去執行它的 speak 動作。」  
* self **的自動設定**：如前面所解釋，Python 自動將 my\_dog 這個物件本身，作為 speak 動作的第一個接收資料（參數）傳遞進去。在 Dog 類別中 speak 動作的定義 def speak(self):，那個 self 就是用來接收這個自動傳入的物件。  
* self **的角色**：因此，在 speak 動作的內部，self 就代表了 my\_dog 這個特定的物件。

這就是為什麼即使我們呼叫 my\_dog.speak() 時沒有明確寫出要傳遞什麼資料給 self，speak 動作的定義中仍然需要 self 這個接收位置。

### **2\.** self **如何運作？為什麼需要它來操作物件的資料？**

當你讓一個物件執行它的某個動作（方法）時，例如 my\_object.do\_something(arg1, arg2)，Python 會自動將這個物件本身 (my\_object) 作為第一個資料傳遞給該動作。按照慣例，這個第一個資料被命名為 self。這讓動作（方法）能夠知道它正在為哪一個物件服務，並能存取或修改那個特定物件的資料（屬性）。
```python
class Dog: \# 狗的藍圖 (類別)  
    \# 這是狗物件剛被建立時的「初始化」動作  
    \# 它負責設定新狗物件一開始的資料  
    def \_\_init\_\_(self, name, breed):  
        \# self 代表正在被建立的那隻新狗物件  
        \# self.dog\_name \= name 的意思是：  
        \# 「給這隻狗 (self) 一個叫做 dog\_name 的資料標籤 (屬性)，  
        \#   並把傳進來的 name (例如 "小黃") 存到這個標籤裡。」  
        self.dog\_name \= name  
        self.dog\_breed \= breed \# 設定這隻狗的品種

    \# 介紹自己的動作 (方法)  
    def introduce(self):  
        \# self 代表呼叫 introduce 動作的那隻狗  
        \# 所以 self.dog\_name 就是那隻狗的 dog\_name 資料 (名字)  
        print(f"汪！我是 {self.dog\_name}，一隻{self.dog\_breed}。")

\# 依照 Dog 藍圖建立兩隻不同的狗物件  
dog1 \= Dog("小黃", "柴犬") \# Python 內部呼叫 Dog.\_\_init\_\_(dog1物件, "小黃", "柴犬")  
dog2 \= Dog("旺財", "黃金獵犬") \# Python 內部呼叫 Dog.\_\_init\_\_(dog2物件, "旺財", "黃金獵犬")

dog1.introduce() \# introduce 方法中的 self 代表 dog1  
dog2.introduce() \# introduce 方法中的 self 代表 dog2

如果沒有 self，introduce 這個動作就無法知道要介紹的是「小黃」還是「旺財」，因為它不知道是哪一隻狗在執行這個動作。self 提供了這種區分。

### **3\. 使用** self **設定和取得物件的「屬性」(資料)**

self 最常見的用途之一，就是在物件中儲存和讀取它自己的資料。這些儲存在特定物件裡的資料，我們稱為物件的「**屬性**」(attribute)。我們通常在物件剛被建立時的「初始化」動作 (\_\_init\_\_) 中使用 self 來設定這些屬性。
```python
class Dog: \# 狗的藍圖  
    \# 初始化動作：當一隻新狗物件被建立時執行  
    def \_\_init\_\_(self, name, age):  
        \# self 代表這隻正在被建立的新狗物件  
        self.dog\_name \= name    \# 設定這隻狗的名字屬性  
        self.dog\_age \= age      \# 設定這隻狗的年齡屬性  
        self.is\_hungry \= True   \# 設定牠是否飢餓的屬性 (預設是餓的)

    \# 餵食的動作  
    def feed(self):  
        \# self 代表呼叫 feed 動作的那隻狗  
        if self.is\_hungry:  
            print(f"正在餵食 {self.dog\_name}...")  
            self.is\_hungry \= False \# 修改這隻狗的 is\_hungry 屬性  
            print(f"{self.dog\_name} 吃飽了！")  
        else:  
            print(f"{self.dog\_name} 現在不餓。")

my\_pet\_dog \= Dog("Lucky", 3\) \# 建立一隻叫做 Lucky，3歲的狗物件  
print(f"我的狗叫做 {my\_pet\_dog.dog\_name}，牠 {my\_pet\_dog.dog\_age} 歲了。")  
print(f"Lucky 現在餓嗎？ {'餓' if my\_pet\_dog.is\_hungry else '不餓'}")

my\_pet\_dog.feed() \# 讓 my\_pet\_dog 物件執行餵食的動作  
print(f"Lucky 現在餓嗎？ {'餓' if my\_pet\_dog.is\_hungry else '不餓'}")  
my\_pet\_dog.feed() \# 再試著餵一次
```
這裡，self.dog\_name、self.dog\_age 和 self.is\_hungry 都是 my\_pet\_dog 這個特定狗物件擁有的資料。

### **4\. 使用** self **呼叫同一個物件的其他動作**

在一個類別（藍圖）中定義的一個動作（方法）裡面，你可以使用 self 來呼叫同一個物件的「其他」動作。
```
class Dog: \# 狗的藍圖  
    def \_\_init\_\_(self, name):  
        self.dog\_name \= name  
        self.energy\_level \= 100 \# 初始能量值

    \# 一個檢查能量的 "內部" 動作  
    def \_check\_energy(self):  
        \# self 代表呼叫 \_check\_energy 動作的那個狗  
        print(f"{self.dog\_name}：檢查能量... 目前能量 {self.energy\_level}。")  
        if self.energy\_level \> 20:  
            return True  
        else:  
            print(f"{self.dog\_name}：能量不足，需要休息！")  
            return False

    \# 玩耍的動作  
    def play\_fetch(self, times):  
        \# self 代表呼叫 play\_fetch 動作的那個狗  
        print(f"{self.dog\_name} 準備開始玩撿球遊戲！")  
        for i in range(times):  
            if self.\_check\_energy(): \# 呼叫同一個狗 (self) 的 \_check\_energy 動作  
                print(f"第 {i+1} 次撿球：{self.dog\_name} 衝啊！撿到球了！")  
                self.energy\_level \-= 15 \# 玩耍會消耗能量  
            else:  
                print(f"{self.dog\_name} 太累了，不能再玩了。")  
                break  
        print(f"{self.dog\_name} 玩完了，目前能量 {self.energy\_level}。")

active\_dog \= Dog("皮蛋") \# 建立一隻名為皮蛋的狗物件  
active\_dog.play\_fetch(5) \# 讓皮蛋玩5次撿球遊戲
```
在 play\_fetch 動作中，self.\_check\_energy() 確保了是 active\_dog 這個狗物件自己去檢查自己的能量。

### **5\.** self **是一個慣例名稱，不是「特殊保留字」**

雖然幾乎所有的 Python 開發者都使用 self 作為物件動作（方法）的第一個接收位置（參數）的名稱，但它並不是 Python 的一個「特殊保留字」(英文是 keyword，是指 Python 語言中已經有預先定義好的特殊意義的字，例如 if、for、class 等)。

理論上你可以用任何其他有效的變數名稱代替 self，例如 this\_dog 或 current\_pet，但**強烈建議你遵循使用** self **這個慣例**，這樣你的程式碼才能讓其他 Python 開發者 (以及未來的你) 容易閱讀和理解。

**透過** self **設定物件資料 (屬性) 的詳細步驟：**

當我們在 \_\_init\_\_ (初始化) 動作中使用像 self.資料名稱 \= 值 這樣的語句時，到底發生了什麼事？

1. self **代表新建立的物件**：  
   * 當你寫 my\_object \= MyClass(some\_value) 來依照 MyClass 藍圖建立一個新物件時，Python 首先會在記憶體中做出一個 MyClass 的新成品 (一個空白的物件)。  
   * 然後，Python 自動呼叫 MyClass 的 \_\_init\_\_ 動作。  
   * 最重要的，Python 將剛剛做出來的那個新物件，作為 \_\_init\_\_ 動作的第一個接收資料傳進去。這個接收位置，我們習慣上命名為 self。所以，在 \_\_init\_\_ 動作內部，self 就代表這個「剛出爐、正在被初始設定的物件」。  
2. **點號** . **的意義：存取或建立物件的資料標籤 (屬性)**：  
   * 在 self.資料名稱 中，這個點號 . 是一個運算子，它告訴 Python：「我要處理 self 這個物件裡面，一個叫做 資料名稱 的資料標籤 (屬性)。」  
   * 如果 self 物件中還沒有一個叫做 資料名稱 的資料標籤，Python 就會準備在這個物件上新增一個這樣的標籤。  
3. **賦值** \= **的動作：將值存到資料標籤裡**：  
   * self.資料名稱 \= 值 這整行程式碼的意思是：將等號右邊的「值」，儲存到 self 這個物件的 資料名稱 這個資料標籤中。  
   * 如果 資料名稱 這個標籤是第一次出現並被賦值，那麼這個標籤就會被建立起來，並且存放你給它的值。  
   * 如果 self 物件之前已經有了 資料名稱 這個標籤，那麼它裡面舊的值就會被新的「值」所取代。

**總結來說，**self.資料名稱 \= 值 **的步驟是：**

* **a. 找到物件**：self 代表當前正在操作的這個特定物件。  
* **b. 指定資料標籤名稱**：.資料名稱 告訴 Python 我們要處理的是這個物件中，名為 資料名稱 的那個資料標籤。  
* **c. 存入值**：\= 值 將右邊的「值」儲存到該物件的這個資料標籤中。

這樣，這個特定的 self 物件就擁有了一個名為 資料名稱 的資料標籤，其內容為你指定的「值」。
```
class PetBlueprint: \# 一個寵物的藍圖  
    def \_\_init\_\_(this\_pet, initial\_name): \# 故意不用 self，但 this\_pet 扮演相同角色  
        \# this\_pet 代表新建立的寵物物件  
        this\_pet.pet\_name \= initial\_name \# 設定這個寵物的名字資料

    def show\_name(this\_pet): \# this\_pet 代表呼叫此動作的寵物物件  
        print(f"我的名字是 {this\_pet.pet\_name}")

my\_dog\_from\_blueprint \= PetBlueprint("豆豆") \# 建立物件，this\_pet 在 \_\_init\_\_ 中就是 my\_dog\_from\_blueprint  
my\_dog\_from\_blueprint.show\_name()        \# 呼叫動作，this\_pet 在 show\_name 中就是 my\_dog\_from\_blueprint
```  
\# 輸出: 我的名字是 豆豆

上面的程式碼可以運作，但它違反了 Python 的慣例。重點是理解無論這個第一個接收位置叫什麼名字，它都代表「物件本身」。

### **6\. 為什麼** self **如此重要？**

self 是實現許多程式設計好處的基石，尤其是在稱為「物件導向程式設計」(Object-Oriented Programming, OOP) 的風格中。它允許：

* **區分不同的物件**：讓每個依照相同藍圖做出來的物件，都能擁有自己獨立的資料值。例如，兩隻狗物件「小黃」和「旺財」可以有不同的名字和品種。  
* **管理物件的「狀態」**：讓物件能夠「記住」它自己的情況或目前擁有的資料（透過它自己的屬性）。例如，一隻狗物件可以記住自己是「飢餓」還是「吃飽了」的狀態。  
* **將資料和操作資料的動作綁在一起**：物件的動作（方法）可以很方便地處理它自己的資料（屬性）。這有助於程式碼的組織和重用。

沒有 self（或類似的機制，用來指代物件本身），藍圖（類別）就很難有效地建立和管理多個擁有不同資料和狀態的物件。

希望這個逐步教學能讓你更清楚地理解 self 的概念和用法！
