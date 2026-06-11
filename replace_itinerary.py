import re

new_data = r"""    const itineraryData = [
        {
            date: "2026-06-13",
            title: "抵達日本 & 自駕前往下田",
            tag: "啟程",
            weather: "🌙 16°C",
            events: [
                {
                    time: "14:00", type: "flight", icon: "fas fa-plane",
                    title: "抵達機場（成田/羽田）",
                    desc: "預計耗時 1.5 小時，過海關提領行李，預抓 1 小時。",
                    badges: [{cls:"booking", icon:"fa-plane", text:"入境辦理"}],
                    notice: { icon: "fa-clock", text: "導遊時間提醒", warning: "成田搭Skyliner到上野約45分，14:00落地若抓1小時出關，16:00上野取車會非常趕！建議聯繫車行改16:30取車較保險。" }
                },
                {
                    time: "16:00", type: "booking", icon: "fas fa-key",
                    title: "【租車組】上野租車取車",
                    desc: "請出示日文駕照譯本與台灣護照，確認 ETC 卡與保險範圍。",
                    badges: [{cls:"booking", icon:"fa-key", text:"取車"}],
                    tip: { title: "導遊取車秘訣 🚙", content: "1. <b>日文駕照譯本</b>絕對不能忘（沒帶100%無法取車）。<br>2. 務必確認車內 ETC 卡已設定好。<br>3. 保險強烈建議直上最高級（自負額 ¥0 方案/NOC補償）。<br>4. 在市區先習慣右駕再上高速公路！" }
                },
                {
                    time: "17:30", type: "transport", icon: "fas fa-car",
                    title: "自駕前往下田飯店",
                    desc: "走東名高速 → 伊豆縱貫道，車程約 3.5 小時。",
                    notice: { icon: "fa-car", text: "長途夜車注意", warning: "週末傍晚出東京市區(東名高速)容易塞車。若太晚抵達下田，餐廳大多20:00關門，建議在途中的高速公路休息站(如海老名SA)先吃點東西！" }
                }
            ]
        },
        {
            date: "2026-06-14",
            title: "下田自駕：海風與金目鯛",
            tag: "自駕",
            weather: "☀️ 22°C",
            events: [
                {
                    time: "10:45", type: "sight", icon: "fas fa-water",
                    title: "第一站：龍宮窟",
                    desc: "神祕的愛心形海蝕洞與天然天窗，享受早晨平靜的海風。",
                    badges: [{cls:"sight", icon:"fa-heart", text:"天窗洞"}],
                    tip: { title: "導遊私房拍攝點 📸", content: "龍宮窟入口較隱密，旁邊有收費停車場(約500日圓)。建議出發前確認潮汐，退潮時可以走到沙灘上；從上方步道往下拍，可以拍到完美的愛心形海蝕洞！" }
                },
                {
                    time: "11:45", type: "food", icon: "fas fa-utensils",
                    title: "午餐：下田港美食二選一",
                    desc: "選項 A：金目亭（招牌金目鯛海鮮丼）/ 選項 B：Ra-maru（黑船漢堡）",
                    badges: [{cls:"food", icon:"fa-fish", text:"招牌金目鯛"}],
                    notice: { icon: "fa-fish", text: "下田特產金目鯛", warning: "「金目亭」只營業到15:00（且食材賣完提早打烊）！建議不要太晚過去。他們家的金目鯛燉煮定食是極品！" }
                },
                {
                    time: "13:30", type: "sight", icon: "fas fa-camera",
                    title: "第二站：白濱海灘 & 白浜神社",
                    desc: "參拜古老神社，走到沙灘拍矗立在海中礁石上的「紅色海上鳥居」。",
                    badges: [{cls:"sight", icon:"fa-camera", text:"Tiffany藍海水"}],
                    tip: { title: "導遊參拜提醒", content: "鳥居位在礁石上，海浪來時容易打濕鞋子，建議穿著好穿脫的涼鞋。另外白浜神社是伊豆最古老的神社，境內有2000年神木，別忘了入內參拜結緣。" }
                },
                {
                    time: "16:00", type: "sight", icon: "fas fa-walking",
                    title: "傍晚：看體力二選一",
                    desc: "想走走 → 培里之路咖啡廳；想躺平 → 搭下田纜車登頂看全景。",
                    badges: [{cls:"story", icon:"fa-leaf", text:"慢活行程"}],
                    notice: { icon: "fa-leaf", text: "行程選擇建議", warning: "若天氣晴朗推薦下田纜車(來回約1250日圓)看夕陽海景；若想喝下午茶，培里之路(Perry Road)石板街道非常有幕末復古風情。" }
                },
                {
                    time: "19:00", type: "food", icon: "fas fa-utensils",
                    title: "晚餐：在地小吃 or 飯店開趴",
                    desc: "上の山亭有神級金目鯛炒飯；7-11 買炸雞泡麵回飯店洗澡開趴！",
                    badges: [{cls:"tip", icon:"fa-star", text:"極致放鬆"}],
                    tip: { title: "導遊在地美食名單", content: "「上の山亭」是當地人愛去的町中華料理，不用訂位。必點：金目鯛炒飯、金目鯛拉麵！份量很大，CP值極高。" }
                }
            ]
        },
        {
            date: "2026-06-15",
            title: "城崎海岸、大室山與水豚君",
            tag: "絕景",
            weather: "☀️ 20°C",
            events: [
                {
                    time: "10:00", type: "transport", icon: "fas fa-car",
                    title: "下田飯店出發 → 城崎海岸",
                    desc: "沿國道 135 號北上，車程約 40 分鐘。",
                    notice: { icon: "fa-map-marked-alt", text: "海岸線駕駛", warning: "國道135號沿線海景絕美，但只有單線道，遇到假日容易走走停停，行車時間請多抓15分鐘緩衝。" }
                },
                {
                    time: "10:40", type: "sight", icon: "fas fa-mountain",
                    title: "第一站：城崎海岸 & 門脇吊橋",
                    desc: "黑色熔岩斷崖奇景，吊橋下是洶湧的波浪，氣勢磅礴。",
                    badges: [{cls:"sight", icon:"fa-water", text:"熔岩斷崖"}],
                    tip: { title: "導遊步道指南 🥾", content: "停車場收費約500日圓。走到吊橋約需10分鐘，沿途是海岸松林步道，吊橋晃度適中，從門脇燈塔可以免費登高眺望整個海岸線！" }
                },
                {
                    time: "11:40", type: "food", icon: "fas fa-utensils",
                    title: "午餐：Ohmuro Luncheonette（大室軽食堂）",
                    desc: "位於大室山纜車站旁，非常熱門，建議提早 11:40 抵達避開人潮。",
                    badges: [{cls:"food", icon:"fa-utensils", text:"大室軽食堂"}],
                    tip: { title: "免排隊攻略", content: "大室山纜車旁吃東西最方便！這家店的炸物定食跟麥飯非常搭。吃飽後直接去買纜車票上山，動線最順。" }
                },
                {
                    time: "13:00", type: "sight", icon: "fas fa-mountain",
                    title: "第二站：大室山 ⛰️（搭纜車登頂）",
                    desc: "搭纜車上山，環繞火山口散步一圈，是陽光最足、海景最亮的時候。",
                    badges: [{cls:"sight", icon:"fa-mountain", text:"抹茶布丁山"}],
                    tip: { title: "導遊山頂注意事項", content: "纜車來回票約1000日圓。山上<b>完全沒有遮蔽物</b>且風大！請做好防曬，帽子記得抓緊。火山口底部有個射箭場(約1000日圓)，非常有武士修行感，強烈推薦體驗！" }
                },
                {
                    time: "14:15", type: "sight", icon: "fas fa-paw",
                    title: "第三站：伊豆仙人掌公園 🦫",
                    desc: "就在大室山對面，走路就到。重點看水豚泡湯與半開放小動物。",
                    badges: [{cls:"sight", icon:"fa-paw", text:"療癒水豚"}],
                    notice: { icon: "fa-paw", text: "水豚君出沒", warning: "6月沒有冬季限定的溫泉水豚，但可以買草親自餵食水豚君與袋鼠。門票較貴(約2700日圓)，可在網路上先買好電子票折價。" }
                },
                {
                    time: "16:15", type: "transport", icon: "fas fa-car",
                    title: "一路向北，直奔熱海",
                    desc: "從大室山沿國道 135 號北上，車程約 45 分鐘。",
                    notice: { icon: "fa-car", text: "黃昏塞車警報", warning: "黃昏時段進入熱海市區容易遇到下班與遊客車潮，請耐心駕駛。" }
                },
                {
                    time: "18:30", type: "food", icon: "fas fa-fire",
                    title: "晚餐：健康燒肉 Honori 熱海店",
                    desc: "在飯店放完行李稍作休息後，出門享用美味的燒肉大餐，慰勞一天的疲勞！",
                    badges: [{cls:"food", icon:"fa-fire", text:"健康焼肉ほのり"}],
                    tip: { title: "導遊私房推薦", content: "熱海不只有海鮮，這家黑毛和牛燒肉品質極高。必點：厚切牛舌、特上霜降！座位不多，強烈建議請飯店櫃檯先幫忙打電話訂位。" }
                }
            ]
        },
        {
            date: "2026-06-16",
            title: "神木、藝術與熱海老街",
            tag: "文化",
            weather: "⛅ 19°C",
            events: [
                {
                    time: "09:30", type: "sight", icon: "fas fa-tree",
                    title: "第一站：來宮神社（2100年神木）",
                    desc: "趁早吸收神木芬多精，在附設的茶寮喝拿鐵、吃點心，拍美美的照片。",
                    badges: [{cls:"sight", icon:"fa-tree", text:"2100年神木"}],
                    notice: { icon: "fa-parking", text: "停車場極度容易客滿", warning: "來宮神社附設停車場位子很少！若9點後抵達客滿，請依指引停到附近的收費停車場，不要在門口排隊影響交通。" },
                    tip: { title: "導遊祈福教學", content: "傳說繞著2100年大楠樹走一圈可以延長一年壽命。神社境內設計非常現代，每個角落都有手機放置架方便自拍，『茶寮 緣』的麥焦饅頭(焦がし饅頭)是必吃名產！" }
                },
                {
                    time: "11:00", type: "sight", icon: "fas fa-palette",
                    title: "第二站：MOA 美術館（看展＋午餐）",
                    desc: "開車攻頂，停進大停車場，館內有無敵海景與三星甜點主廚監修的咖啡廳。",
                    badges: [{cls:"sight", icon:"fa-palette", text:"國寶藝術"}, {cls:"tip", icon:"fa-star", text:"三星甜點"}],
                    tip: { title: "導遊動線建議", content: "美術館位於半山腰，視野極佳（門票約1700日圓，線上預購有折扣）。最出名的是館內的『萬花筒手扶梯』。看完展直接在館內的 鎧塚俊彥(Toshi Yoroizuka) 甜點店吃熱海限定烤布蕾。" }
                },
                {
                    time: "14:00", type: "hotel", icon: "fas fa-car",
                    title: "開車前往樂天 STAY 熱海",
                    desc: "車程 15 分鐘，把車子穩穩停在專屬車位，開啟無壓力逛街模式！",
                    notice: { icon: "fa-car", text: "停好車再出門", warning: "熱海車站周邊停車費超貴且容易客滿，最好的策略是把車停在飯店，改搭公車或計程車去逛商店街！" }
                },
                {
                    time: "14:30", type: "buy", icon: "fas fa-shopping-bag",
                    title: "第三站：熱海站前商店街爆買！",
                    desc: "搭計程車或公車不到 5 分鐘，雙手空空盡情買，不用搶停車位！",
                    badges: [{cls:"food", icon:"fa-store", text:"吃貨模式"}, {cls:"buy", icon:"fa-shopping-bag", text:"買伴手禮"}],
                    tip: { title: "導遊必吃名單清盤 🎯", content: "商店街17:00左右就會陸續關門，請把握時間！<br>1. <b>熱海布丁(熱海プリン)</b>：招牌焦糖口味與復古牛奶瓶包裝，必排。<br>2. <b>磯揚げ まる天</b>：現炸海鮮黑輪，起司竹輪是極品。<br>3. <b>又一庵謹製 熱海ばたーあん</b>：紅豆奶油麵包，非常搶手。<br>買完可以直接帶回飯店慢慢享用。" }
                }
            ]
        },
        {
            date: "2026-06-17",
            title: "沼津深海與三島絕景",
            tag: "深海",
            weather: "☀️ 21°C",
            events: [
                {
                    time: "09:00", type: "transport", icon: "fas fa-car",
                    title: "熱海退房 → 驅車直奔沼津港",
                    desc: "沿國道 135 號北上後接東名，車程約 45 分鐘。",
                    notice: { icon: "fa-parking", text: "沼津港停車資訊", warning: "9:45 抵達沼津港，這時候大型免費/計次停車場都還有位子。導遊建議直接停在『沼津港免費停車場』或『水族館旁立體停車場』。" }
                },
                {
                    time: "09:45", type: "buy", icon: "fas fa-shopping-bag",
                    title: "市場搶先逛（伴手禮速掃）🛍️",
                    desc: "水族館開門前先把最想要的「真空包裝一夜干」與田丸屋「山葵鹽/美乃滋」買齊，放回車上的冷氣房。",
                    badges: [{cls:"buy", icon:"fa-shopping-bag", text:"無負擔逛街"}],
                    tip: { title: "在地伴手禮推薦", content: "靜岡的『田丸屋山葵美乃滋』是日本當地人也愛買的調味料，不管是沾炸物還是配飯都無敵！買完記得放車上，不要提著逛水族館。" }
                },
                {
                    time: "10:00", type: "sight", icon: "fas fa-fish",
                    title: "🐠 沼津深海水族館",
                    desc: "準時開門第一波進場！看各種奇特的駿河灣深海生物。",
                    badges: [{cls:"sight", icon:"fa-fish", text:"腔棘魚標本"}],
                    tip: { title: "導遊看點解說", content: "門票約1800日圓。這是日本唯一深海主題水族館！二樓有世界唯一的『腔棘魚冷凍標本』，宛如恐龍時代的活化石，非常震撼，必看！" }
                },
                {
                    time: "11:30", type: "food", icon: "fas fa-utensils",
                    title: "🍱 午餐黃金時間（翻牌三選一）",
                    desc: "壽司之助（滿溢壽司）/ 五鐵（海鮮三吃）/ かねはち（定食）",
                    badges: [{cls:"food", icon:"fa-utensils", text:"免排隊入座"}],
                    notice: { icon: "fa-store", text: "完美避開人潮", warning: "11:30是各大排隊名店剛開門的時間，完全不用曬太陽排隊！如果猶豫，導遊首推『五鐵』的海鮮丼三吃，最後用鮮魚高湯泡飯收尾，絕讚！" }
                },
                {
                    time: "13:00", type: "sight", icon: "fas fa-water",
                    title: "港邊消遣：巨型水門「View-O」散步 🌊",
                    desc: "搭電梯到 30 公尺高的空中展望迴廊，吹著海風眺望駿河灣與富士山（門票 ¥100！）",
                    badges: [{cls:"sight", icon:"fa-water", text:"富士山眺望"}],
                    tip: { title: "全日本最大水門", content: "只要100日圓銅板價！在30公尺高空享受360度環景，運氣好可以清楚拍到富士山，也是消化午餐的好去處。" }
                },
                {
                    time: "14:30", type: "transport", icon: "fas fa-car",
                    title: "開車前往三島大吊橋",
                    desc: "結束沼津港全攻略，吹著冷氣往山線移動，車程約 30 分鐘。",
                    notice: { icon: "fa-car", text: "山路駕駛提醒", warning: "前往三島大吊橋的國道1號會開始爬坡，路幅較寬但重機多，請注意後視鏡。" }
                },
                {
                    time: "15:00", type: "sight", icon: "fas fa-mountain",
                    title: "👑 三島大吊橋（Mishima Skywalk）",
                    desc: "日本最長吊橋！下午 3 點整抵達，夕陽光影灑在山谷上最美，也是拍富士山最立體的時段。",
                    badges: [{cls:"sight", icon:"fa-mountain", text:"日本最長吊橋"}],
                    tip: { title: "導遊拍照秘訣", content: "門票1100日圓。下午3點太陽在吊橋側後方，順光拍吊橋與富士山最清晰。若想挑戰極限，現場加購Zipline(約2000日圓)飛越山谷，會是此行最難忘回憶！" }
                },
                {
                    time: "16:30", type: "transport", icon: "fas fa-car",
                    title: "順流直上，直奔箱根溫泉飯店",
                    desc: "從三島大吊橋走箱根新道，輕鬆翻過山頭，正式進入箱根，車程約 30 分鐘。",
                    notice: { icon: "fa-car", text: "天黑前抵達箱根", warning: "箱根山路沒有路燈且常起大霧！請務必在17:00天黑前抵達飯店，安全第一。" }
                },
                {
                    time: "17:00", type: "hotel", icon: "fas fa-hot-tub",
                    title: "抵達箱根 Check-in ♨️",
                    desc: "時間非常優雅。放好行李喝杯熱茶，享用澎湃精緻的溫泉會席料理，再去泡個暖呼呼的箱根溫泉！",
                    badges: [{cls:"booking", icon:"fa-hot-tub", text:"溫泉會席"}],
                    tip: { title: "溫泉飯店禮儀", content: "入住後先換上浴衣(Yukata)！會席料理通常需吃1.5-2小時，請放慢步調。泡湯時毛巾不可入水，有刺青者請預先向飯店確認或預約『貸切風呂』(個人湯屋)。" }
                }
            ]
        },
        {
            date: "2026-06-18",
            title: "箱根特攻大迴圈",
            tag: "早鳥",
            weather: "⛅ 18°C",
            events: [
                {
                    time: "06:30", type: "transport", icon: "fas fa-car",
                    title: "退房出發 🚗",
                    desc: "清晨的山路完全沒車，開起來非常舒服。",
                    notice: { icon: "fa-car", text: "清晨山路小心", warning: "箱根清晨氣溫較低(約15度)，外套必備！開車注意可能會有野生動物(鹿/猴子)出沒。" }
                },
                {
                    time: "07:00", type: "sight", icon: "fas fa-camera",
                    title: "第一站：箱根神社・平和鳥居（完美包場）",
                    desc: "07:00 準時卡位，光線最柔和，拍出天地間只有你們的鳥居神級大片。",
                    badges: [{cls:"sight", icon:"fa-camera", text:"黃金包場"}],
                    tip: { title: "導遊排隊預測", content: "平和鳥居如果9點以後來，拍照要排隊1-2小時！7點抵達是『神之操作』，完全沒人。車子可以直接停在箱根神社免費停車場，走下去只要3分鐘。" }
                },
                {
                    time: "09:00", type: "food", icon: "fas fa-coffee",
                    title: "第二站：Bakery & Table 箱根（足湯頭等艙）",
                    desc: "09:00 準時進店，搶下一樓戶外「溫泉足湯座位區」，邊泡足湯邊吃熱麵包看湖景。",
                    badges: [{cls:"booking", icon:"fa-coffee", text:"足湯頭等艙"}],
                    notice: { icon: "fa-clock", text: "黃金座位爭奪戰", warning: "一樓戶外足湯位只有幾個，09:00開店前5分鐘抵達等候最保險。自備小毛巾擦腳用！" },
                    tip: { title: "必點麵包", content: "招牌『米粉咖哩麵包』內包一整顆半熟蛋，以及『箱根山羊奶吐司』，搭配卡布奇諾，看著蘆之湖的海賊船，是最奢華的箱根早晨。" }
                },
                {
                    time: "10:05", type: "sight", icon: "fas fa-running",
                    title: "第三站：箱根驛傳博物館 & 元箱根港",
                    desc: "順向開車 5 分鐘到箱根町港，看日本最熱血的大學接力賽歷史，在港口拍巨大的海賊船進港。",
                    badges: [{cls:"sight", icon:"fa-running", text:"熱血歷史"}],
                    tip: { title: "海賊船最佳拍攝點", content: "如果不搭船，在元箱根港或箱根町港的岸邊，以蘆之湖和富士山為背景，拍即將靠岸的海賊船最壯觀！" }
                },
                {
                    time: "11:30", type: "food", icon: "fas fa-utensils",
                    title: "第四站：箱根湯本商店街（蕎麥麵午餐＋買伴手禮）",
                    desc: "開車走「箱根新道」一路下坡，抵達時剛好各大老字號餐廳剛開門，免排隊！",
                    badges: [{cls:"food", icon:"fa-utensils", text:"蕎麥麵午餐"}, {cls:"buy", icon:"fa-shopping-bag", text:"買伴手禮"}],
                    notice: { icon: "fa-parking", text: "湯本停車困難", warning: "箱根湯本車站周邊很難停車，建議停在『湯本觀光停車場』，走路3分鐘可達商店街。" },
                    tip: { title: "導遊美食名單", content: "午餐首推『はつ花(Hatsuhana)』的自然薯蕎麥麵，口感獨特！伴手禮必買『湯もっち(溫泉麻糬)』及現烤仙貝。逛完把東西丟回車上，下午輕裝出發。" }
                },
                {
                    time: "13:30", type: "sight", icon: "fas fa-palette",
                    title: "第五站：雕刻之森美術館",
                    desc: "在森林與藝術品之間漫步，必拍彩繪玻璃塔，節奏非常悠閒。",
                    badges: [{cls:"sight", icon:"fa-palette", text:"午後藝術散步"}],
                    tip: { title: "網美打卡點", content: "門票約1600日圓。<b>彩繪玻璃塔 (The Hall of Happiness)</b> 必去！爬到塔頂光影絕美。園區內也有免費足湯，記得帶剛剛擦腳的小毛巾過來。" }
                },
                {
                    time: "15:30", type: "sight", icon: "fas fa-mountain",
                    title: "第六站：大湧谷 🌋（極限趕場）",
                    desc: "從雕刻之森開車約20分鐘，趕在商店關門前抵達，吃延壽黑雞蛋、看火山煙。",
                    badges: [{cls:"food", icon:"fa-egg", text:"黑雞蛋"}, {cls:"sight", icon:"fa-mountain", text:"火山奇景"}],
                    notice: { icon: "fa-exclamation-triangle", text: "【導遊極度警告】", warning: "大湧谷停車場與商店16:00-16:30就會關閉！務必在15:30前抵達，否則買不到黑雞蛋也進不了停車場！" },
                    tip: { title: "黑雞蛋傳說", content: "傳說吃一顆大湧谷黑雞蛋(5顆約600日圓)能延壽7年！導遊提醒：一個人吃1-2顆就好，多吃無益(而且會很飽)。火山口硫磺味重，呼吸道敏感者請戴口罩。" }
                }
            ]
        },
        {
            date: "2026-06-19",
            title: "御殿場血拼與必吃美食",
            tag: "購物",
            weather: "🌤️ 17°C",
            events: [
                {
                    time: "09:30", type: "buy", icon: "fas fa-shopping-bag",
                    title: "抵達 御殿場 Premium Outlets 採買",
                    desc: "全日本最大Outlet！腹地廣大，建議先在官網看好必逛品牌地圖。",
                    badges: [{cls:"buy", icon:"fa-shopping-bag", text:"富士山絕景"}, {cls:"sight", icon:"fa-mountain", text:"富士山背景"}],
                    tip: { title: "導遊攻略(重要) 🗺️", content: "園區分為West/East/Hill三區。停好車第一件事：<b>直奔想吃的餐廳抽整理券！</b> 拿到券再去血拼。退稅需帶護照正本。天氣好時，夢之大橋是拍富士山的絕佳位置。" }
                },
                {
                    time: "10:00", type: "food", icon: "fas fa-ticket-alt",
                    title: "【極密任務】抽取 Sawayaka 整理券",
                    desc: "Sawayaka漢堡排在御殿場的排隊時間極長(常破3-4小時)！10點開門立刻去抽券！",
                    badges: [{cls:"tip", icon:"fa-running", text:"衝刺抽券"}],
                    notice: { icon: "fa-exclamation-circle", text: "導遊血淚提醒", warning: "Sawayaka(さわやか)漢堡排是靜岡縣限定，全日本最難排！10:00抽券，通常要等到13:00-14:00才能吃。抽完用手機看叫號進度，安心去逛街。" }
                },
                {
                    time: "13:30", type: "food", icon: "fas fa-utensils",
                    title: "午餐：神級漢堡排 Sawayaka 或 田むら銀かつ亭",
                    desc: "依據整理券時間享用午餐！",
                    badges: [{cls:"food", icon:"fa-utensils", text:"神級漢堡排"}, {cls:"food", icon:"fa-leaf", text:"豆腐豬排"}],
                    tip: { title: "點餐指南", content: "<b>Sawayaka</b>：必點『拳頭漢堡排(げんこつハンバーグ)』，店員會在桌邊切開鐵板壓熟，五分熟的紅肉口感最棒！<br><b>田むら銀かつ亭</b>：若吃不到漢堡排的備案。箱根名店的『豆腐豬排煮定食』，絞肉包在豆腐裡炸，非常下飯。" }
                },
                {
                    time: "16:30", type: "transport", icon: "fas fa-car",
                    title: "提早撤退，自駕返回東京上野",
                    desc: "避開週末傍晚回城塞車潮，預計車程 1.5 - 2 小時。",
                    notice: { icon: "fa-car", text: "東名高速塞車警報", warning: "週五傍晚東名高速公路往東京方向極易塞車！強烈建議16:30前離開Outlet，否則車程可能拉長至3小時。" }
                },
                {
                    time: "18:30", type: "hotel", icon: "fas fa-hotel",
                    title: "上野飯店 Check-in 🏨",
                    desc: "行李與戰利品直接上房間，晚餐在上野附近輕鬆解決！",
                    badges: [{cls:"booking", icon:"fa-hotel", text:"上野首晚"}],
                    tip: { title: "還車準備", content: "今晚先在飯店下行李。確認明天早上還車的車行位置與附近的加油站。晚上可以去阿美橫町吃個居酒屋，慶祝順利回到東京！" }
                }
            ]
        },
        {
            date: "2026-06-20",
            title: "池袋特攻：一番賞與扭蛋爆抽！",
            tag: "抽爆",
            weather: "☀️ 25°C",
            events: [
                {
                    time: "09:30", type: "booking", icon: "fas fa-key",
                    title: "上野市區還車 🔑",
                    desc: "還車前記得把油加滿，還完車後開啟「雙手空空無痛狂逛」模式！",
                    badges: [{cls:"booking", icon:"fa-key", text:"自駕大功告成"}],
                    notice: { icon: "fa-gas-pump", text: "滿油還車規定", warning: "日本租車必須滿油還車。請用導航尋找最近的加油站，加『レギュラー (Regular 紅色油槍)』，並記得保留加油收據，車行會檢查！" }
                },
                                {
                    time: "10:00", type: "buy", icon: "fas fa-shopping-bag",
                    title: "抵達池袋站 & 百貨購物 🛍️",
                    desc: "抵達池袋！西口直通東武百貨 (Tobu) 與 LUMINE 百貨。東武 5F 除了 Mont-bell 戶外專區（為市區少數可辦理退稅專櫃），還有鬼塚虎 (Onitsuka Tiger) 及 United Arrows 專櫃，開門第一波前去選購裝備與潮流服飾！",
                    badges: [{cls:"buy", icon:"fa-shopping-bag", text:"Mont-bell選購"}, {cls:"buy", icon:"fa-tags", text:"鬼塚虎/UA"}, {cls:"sight", icon:"fa-check", text:"西口直通"}],
                    tip: { title: "百貨購物與置物攻略 💡", content: "1. <b>東武百貨 (Tobu)：</b>5F 設有 Mont-bell 與 <b>Onitsuka Tiger (鬼塚虎)</b> 專櫃，且可辦理退稅。<br>2. <b>LUMINE 池袋：</b>與西口直通，內部有 <b>United Arrows</b> 專櫃，推薦順路去逛！<br>3. <b>置物小貼士：</b>建議購買完後，先將大件戰利品寄放在池袋車站的投幣置物櫃 (Lockers)，這樣後續就可以輕裝逛街，不會提得太累。" }
                },
                {
                    time: "10:05", type: "sight", icon: "fas fa-map-marked-alt",
                    title: "🗺️ 池袋行程地圖導覽 🗺️",
                    desc: "為您特別標記的池袋東口逛街路線地圖，可點擊放大查看。<br><br><a href='./ikebukuro_map.png' target='_blank'><img src='./ikebukuro_map.png' alt='池袋逛街地圖' class='mt-2 rounded-xl border border-pink-100 max-w-full h-auto shadow-md hover:scale-[1.01] transition-transform' /></a>",
                    badges: [{cls:"sight", icon:"fa-map", text:"路線地圖"}, {cls:"tip", icon:"fa-search-plus", text:"點擊放大"}]
                },
                {
                    time: "11:30", type: "transport", icon: "fas fa-walking",
                    title: "穿越站區前往池袋東口 🚶",
                    desc: "穿越車站中央通路，往熱鬧的東口（陽光 60 通）前進。出站即是 PARCO 本館，內有 <b>Onitsuka Tiger (鬼塚虎)</b> 與 <b>Beauty & Youth (United Arrows)</b> 專櫃，推薦在此進行第一波採購！",
                    badges: [{cls:"buy", icon:"fa-tags", text:"PARCO本館潮流"}],
                    tip: { title: "散步與東口採購備註 🚶", content: "如果還有多餘體力，東口一出來就是 PARCO 本館（鬼塚虎、UA/BY 都在此），旁邊還有 Bic Camera 與唐吉訶德，也可以先在此做第一波採點。" }
                },
                {
                    time: "12:00", type: "food", icon: "fas fa-utensils",
                    title: "午餐：麵處 花田 或 太陽城美食 🍜",
                    desc: "午餐首推陽光 60 通巷內的「麵處 花田」（主打極度濃郁的味噌拉麵）。",
                    badges: [{cls:"food", icon:"fa-utensils", text:"濃郁味噌拉麵"}],
                    notice: { icon: "fa-store", text: "用餐策略", warning: "花田拉麵為池袋超人氣味噌拉麵，排隊人數多。若不想排隊，也可以直接在太陽城內隨意挑選餐廳用餐，自由度更高。" }
                },
                {
                    time: "13:00", type: "buy", icon: "fas fa-gamepad",
                    title: "第一站：太陽城 Sunshine City（扭蛋總本店 & 遊戲中心） 🎮",
                    desc: "集結吉尼斯世界紀錄 3000 台扭蛋的「扭蛋百貨總本店」與萬代南夢宮遊戲中心都在太陽城 World Import Mart 3F，是同一個地方！下午在冷氣房裡悠閒狂歡。",
                    badges: [{cls:"buy", icon:"fa-gamepad", text:"3000台扭蛋"}, {cls:"booking", icon:"fa-trophy", text:"南夢宮遊戲"}],
                    tip: { title: "太陽城其他看點 🏢", content: "太陽城內還有陽光水族館、寶可夢中心 (Pokémon Center Mega Tokyo), 卡普空商店 (Capcom Store) 及陽光 60 展望台。想逛哪裡就逛哪裡，時間非常充裕且自由！" }
                },
                {
                    time: "16:30", type: "buy", icon: "fas fa-shopping-bag",
                    title: "第二站：UNIQLO 採購 & 西友超市掃貨 👕",
                    desc: "逛陽光 60 通的大型 UNIQLO 旗艦店，採買日本限定款服飾，隨後至隔壁 24H 西友超市掃貨零食與伴手禮。",
                    badges: [{cls:"buy", icon:"fa-shopping-bag", text:"UNIQLO"}, {cls:"buy", icon:"fa-store", text:"24H西友超市"}]
                },
                {
                    time: "18:00", type: "sight", icon: "fas fa-walking",
                    title: "傍晚：自由探索與備案時間 ☕",
                    desc: "完全不設限的遊玩與探索時光！可以隨心找間特色咖啡廳歇腳、喝杯飲料。有多餘時間可自行探索，或前往備案點（Animate 本店、Bic Camera、唐吉訶德）。",
                    badges: [{cls:"story", icon:"fa-leaf", text:"無壓力逛街"}, {cls:"buy", icon:"fa-store", text:"動漫/電器備案"}],
                    tip: { title: "自由探索說明 💡", content: "池袋東口街區繁華，您也可以隨便找家藥妝店比價、或者到站前的商場逛逛，輕鬆無負擔。" }
                },
                {
                    time: "21:30", type: "food", icon: "fas fa-utensils",
                    title: "宵夜：麵創房 無敵家 🍜",
                    desc: "深夜前去無敵家吃招牌熱騰騰豚骨拉麵，避開晚餐時間的恐怖排隊人潮。",
                    badges: [{cls:"food", icon:"fa-star", text:"宵夜首選"}, {cls:"booking", icon:"fa-money-bill-wave", text:"僅收現金"}],
                    tip: { title: "用餐提示", content: "無敵家排隊時店員會先給菜單並點餐。無敵家【只收現金】，請在排隊前備足日幣現鈔喔！" }
                }
            ]
        },
        {
            date: "2026-06-21",
            title: "上野主場：阿美橫町爆買",
            tag: "血拼",
            weather: "☀️ 25°C",
            events: [
                {
                    time: "10:00", type: "sight", icon: "fas fa-tree",
                    title: "上午：上野恩賜公園散步",
                    desc: "飯店就在附近，睡飽再出發。去上野動物園看熊貓，或在星巴克喝杯咖啡。",
                    badges: [{cls:"sight", icon:"fa-tree", text:"休閒芬多精"}],
                    tip: { title: "導遊在地指南", content: "上野公園非常大，公園內的星巴克設計很美，適合悠閒吃早餐。如果喜歡藝術，旁邊的國立西洋美術館(柯比意建築)也很值得一看。" }
                },
                {
                    time: "12:00", type: "food", icon: "fas fa-utensils",
                    title: "午餐：阿美橫町平民美食",
                    desc: "體驗最接地氣的東京市場文化！",
                    badges: [{cls:"food", icon:"fa-utensils", text:"鐵火丼/肉餅"}],
                    tip: { title: "必吃街頭小吃", content: "1. <b>鐵火丼</b>：阿美橫町有很多便宜的海鮮丼，如『みなとや』，500-800日圓就能吃一碗。<br>2. <b>肉的大山</b>：炸肉餅(メンチカツ)超級多汁，站著吃配杯啤酒就是道地吃法！" }
                },
                {
                    time: "13:30", type: "buy", icon: "fas fa-shopping-bag",
                    title: "下午：阿美橫町 & 多慶屋狂掃",
                    desc: "買到雙手提不動，隨時走回飯店放戰利品，這就是住上野的最大特權！",
                    badges: [{cls:"buy", icon:"fa-shopping-bag", text:"藥妝零食"}],
                    notice: { icon: "fa-bullhorn", text: "藥妝店避坑指南", warning: "阿美橫町的『OS Drug』藥妝通常最便宜，但【只收現金且無退稅】。如果要大量購買並刷卡退稅，建議去松本清、大國藥妝或『多慶屋(紫色的建築)』！" }
                },
                {
                    time: "15:30", type: "sight", icon: "fas fa-coffee",
                    title: "下午茶與歷史街區：日本橋（搭銀座線直達 8 分鐘） ☕",
                    desc: "搭乘地鐵直達日本橋，探訪東京商業起點與百年老街！可造訪日本首家百貨「日本橋三越」、復古奢華的「日本橋高島屋」或現代商場「COREDO 室町」。",
                    badges: [{cls:"sight", icon:"fa-history", text:"百年歷史街區"}, {cls:"buy", icon:"fa-store", text:"老字號百貨"}],
                    tip: { title: "日本橋必逛與必吃 🍡", content: "1. <b>福德神社：</b>隱身在 COREDO 室町大樓之間的綠意神社，以祈求中籤（一番賞、演唱會門票）與旅途平安聞名，一定要去參拜！<br>2. <b>傳統和菓子：</b>可以去「日本橋 榮太樓」或「木屋」等百年老店品嚐日式甜點，歇腳喝杯抹茶。<br>3. <b>交通：</b>上野站搭乘「東京地鐵銀座線」直達日本橋站僅需 8 分鐘，刷交通卡進出即可。" }
                },
                {
                    time: "18:00", type: "sight", icon: "fas fa-gamepad",
                    title: "傍晚：秋葉原最終補貨（搭日比谷線 4 分鐘） 🎮",
                    desc: "從日本橋地區搭乘日比谷線直達秋葉原，補齊動漫周邊、電器或扭蛋遺珠！",
                    badges: [{cls:"sight", icon:"fa-gamepad", text:"電器扭蛋天堂"}],
                    tip: { title: "秋葉原採買重點", content: "電器首選：<b>Yodobashi Camera Multimedia Akiba</b>（最大，退稅+刷卡+積點全有）。<br>動漫扭蛋：Radio會館、中央通各棟大樓都有。<br>二手收藏：Sofmap、Lashinbang秋葉原店，超多二手周邊。<br><b>交通：</b>從人形町站或三越前站搭乘日比谷線/銀座線，約 3-5 分鐘即達秋葉原。" }
                },
                {
                    time: "19:30", type: "food", icon: "fas fa-beer",
                    title: "晚餐：上野居酒屋街，為旅程乾杯！",
                    desc: "高架橋下的下町居酒屋，串燒＋生啤，完美收尾。",
                    badges: [{cls:"food", icon:"fa-beer", text:"下町居酒屋"}],
                    tip: { title: "在地居酒屋體驗", content: "「大統領」或「肉の大山」傍晚氣氛超棒！坐在高架橋下的露天攤位，點幾串もつ焼き（內臟串燒）和一杯生ビール（生啤酒），體驗最真實的東京下町夜晚。這是旅行最後能量儲備，明天認真打包！" }
                }
            ]
        },
        {
            date: "2026-06-22",
            title: "最後衝刺與滿載歸國",
            tag: "歸途",
            weather: "🌤️ 22°C",
            events: [
                {
                    time: "09:30", type: "hotel", icon: "fas fa-suitcase",
                    title: "飯店退房與行李寄放",
                    desc: "將行李先寄放在櫃台，準備最後的補齊作戰！",
                    badges: [{cls:"booking", icon:"fa-suitcase", text:"打包戰利品"}],
                    notice: { icon: "fa-balance-scale", text: "行李超重檢查", warning: "請向飯店借用行李秤(Luggage Scale)，確保沒有超過航空公司的托運限制！" }
                },
                {
                    time: "10:00", type: "buy", icon: "fas fa-gift",
                    title: "二木の菓子（伴手禮最終補貨）",
                    desc: "各種日本零食、伴手禮這邊最齊全，把握最後機會裝滿行李箱！",
                    badges: [{cls:"buy", icon:"fa-gift", text:"買免稅"}],
                    notice: { icon: "fa-clock", text: "結帳人潮預警", warning: "二木の菓子免稅櫃台經常大排長龍，結帳可能需要20-30分鐘，請務必抓緊時間，以免錯過前往機場的電車！" },
                    tip: { title: "必買伴手禮清單", content: "各式口味的KitKat、Pocky、帆船巧克力、梅片、干貝糖。這邊價格比機場免稅店便宜很多，可以一次買齊送同事親友的份！" }
                },
                {
                    time: "12:30", type: "transport", icon: "fas fa-train",
                    title: "搭乘 Skyliner 前往成田機場",
                    desc: "從京成上野直達成田機場約 41 分鐘，全車對號座超舒適！",
                    badges: [{cls:"booking", icon:"fa-train", text:"京成電鐵"}],
                    tip: { title: "導遊購票建議", content: "強烈建議在出發前就在 Klook / KKday 買好 Skyliner 電子票。抵達京成上野站時，直接掃 QR Code 劃位換實體票，省去售票機排隊的時間！" }
                },
                {
                    time: "14:00", type: "flight", icon: "fas fa-plane-departure",
                    title: "抵達成田機場辦理登機",
                    desc: "入關後還可以買 Tokyo Banana、白色戀人等機場限定伴手禮！",
                    badges: [{cls:"booking", icon:"fa-plane-departure", text:"準備起飛"}],
                    tip: { title: "機場免稅店終極攻略", content: "成田機場必買：Tokyo Banana、白色戀人、薯條三兄弟、Royce生巧克力(記得買保冷袋)。<br>【最後提醒】退稅購買的食品不能在境內拆封！請原封不動放入托運或手提上機。" }
                }
            ]
        }
    ];"""

import re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'    const itineraryData = \[.*?\n    \];', re.DOTALL)
new_content = pattern.sub(new_data, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Update successfully")
