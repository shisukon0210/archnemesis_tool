from tkinter import *
import clipboard as cb

class Filter:
    def __init__(self):
        self.T1 = ["毒素", "混沌編織", "冰霜編織", "永凍土", "急速", "銳眼", "投彈手", "烈焰編織", "縱火", "奧術緩衝", "回聲者", "風暴編織",
                   "發電機", "裂骨者", "放血者", "鑄鋼", "龐然大物", "暴徒", "哨兵", "勇士", "吸血魔", "超負荷", "魂靈牽引", "富饒", "憎惡", "奉獻使徒",
                   "喪心病狂"]
        self.T2 = ["先鋒召喚物", "刺客", "死靈師", "振興", "劊子手", "咒術師", "乾旱先鋒", "尾隨魔", "樹人部落", "霜行者", "冰牢",
                   "炎行者", "招魂師", "熔岩屏障", "鏡像幻影", "風行者", "魔靈吸取", "腐化者", "刀槍不入"]
        self.T3 = ["增幅召喚物", "詐欺師", "短暫幻想", "嗜魂者", "強化元素", "陰屍爆破", "晶瑩剔透", "雕像", "海洋之王之觸", "圖克哈瑪之觸", "艾貝拉斯之觸"]
        self.T4 = ["月神之觸", "日神之觸", "艾爾卡莉之觸", "夏卡莉之觸", "奇塔弗之觸"]
        self.T5 = ["善之觸"]

        self.root = Tk()
        self.root.title('宿敵聯盟配方工具')
        self.text1 = Label(self.root, text="T2:", bd=10)
        self.text1.grid(row=0, column=0)
        self.btnT2_0 = Button(self.root, text=self.T2[0], command=lambda: self.copy_recipe("T2", 0))
        self.btnT2_0.grid(row=1, column=0)
        self.btnT2_1 = Button(self.root, text=self.T2[1], bg="#007FFF", command=lambda: self.copy_recipe("T2", 1))
        self.btnT2_1.grid(row=2, column=0)
        self.btnT2_2 = Button(self.root, text=self.T2[2], command=lambda: self.copy_recipe("T2", 2))
        self.btnT2_2.grid(row=3, column=0)
        self.btnT2_3 = Button(self.root, text=self.T2[3], bg="#007FFF", command=lambda: self.copy_recipe("T2", 3))
        self.btnT2_3.grid(row=4, column=0)
        self.btnT2_4 = Button(self.root, text=self.T2[4], command=lambda: self.copy_recipe("T2", 4))
        self.btnT2_4.grid(row=5, column=0)
        self.btnT2_5 = Button(self.root, text=self.T2[5], command=lambda: self.copy_recipe("T2", 5))
        self.btnT2_5.grid(row=6, column=0)
        self.btnT2_6 = Button(self.root, text=self.T2[6], command=lambda: self.copy_recipe("T2", 6))
        self.btnT2_6.grid(row=7, column=0)
        self.btnT2_7 = Button(self.root, text=self.T2[7], command=lambda: self.copy_recipe("T2", 7))
        self.btnT2_7.grid(row=8, column=0)
        self.btnT2_8 = Button(self.root, text=self.T2[8], bg="#FF0000", command=lambda: self.copy_recipe("T2", 8))
        self.btnT2_8.grid(row=9, column=0)
        self.btnT2_9 = Button(self.root, text=self.T2[9], bg="#f28500", command=lambda: self.copy_recipe("T2", 9))
        self.btnT2_9.grid(row=10, column=0)
        self.btnT2_10 = Button(self.root, text=self.T2[10], command=lambda: self.copy_recipe("T2", 10))
        self.btnT2_10.grid(row=11, column=0)
        self.btnT2_11 = Button(self.root, text=self.T2[11], bg="#f28500", command=lambda: self.copy_recipe("T2", 11))
        self.btnT2_11.grid(row=12, column=0)
        self.btnT2_12 = Button(self.root, text=self.T2[12], bg="#f28500", command=lambda: self.copy_recipe("T2", 12))
        self.btnT2_12.grid(row=13, column=0)
        self.btnT2_13 = Button(self.root, text=self.T2[13], command=lambda: self.copy_recipe("T2", 13))
        self.btnT2_13.grid(row=14, column=0)
        self.btnT2_14 = Button(self.root, text=self.T2[14], bg="#007FFF", command=lambda: self.copy_recipe("T2", 14))
        self.btnT2_14.grid(row=15, column=0)
        self.btnT2_15 = Button(self.root, text=self.T2[15], bg="#f28500", command=lambda: self.copy_recipe("T2", 15))
        self.btnT2_15.grid(row=16, column=0)
        self.btnT2_16 = Button(self.root, text=self.T2[16], command=lambda: self.copy_recipe("T2", 16))
        self.btnT2_16.grid(row=17, column=0)
        self.btnT2_17 = Button(self.root, text=self.T2[17], command=lambda: self.copy_recipe("T2", 17))
        self.btnT2_17.grid(row=18, column=0)
        self.btnT2_18 = Button(self.root, text=self.T2[18], command=lambda: self.copy_recipe("T2", 18))
        self.btnT2_18.grid(row=19, column=0)

        self.text2 = Label(self.root, text="T3:", bd=10)
        self.text2.grid(row=0, column=1)
        self.btnT3_0 = Button(self.root, text=self.T3[0], command=lambda: self.copy_recipe("T3", 0))
        self.btnT3_0.grid(row=1, column=1)
        self.btnT3_1 = Button(self.root, text=self.T3[1], command=lambda: self.copy_recipe("T3", 1))
        self.btnT3_1.grid(row=2, column=1)
        self.btnT3_2 = Button(self.root, text=self.T3[2], command=lambda: self.copy_recipe("T3", 2))
        self.btnT3_2.grid(row=3, column=1)
        self.btnT3_3 = Button(self.root, text=self.T3[3], command=lambda: self.copy_recipe("T3", 3))
        self.btnT3_3.grid(row=4, column=1)
        self.btnT3_4 = Button(self.root, text=self.T3[4], command=lambda: self.copy_recipe("T3", 4))
        self.btnT3_4.grid(row=5, column=1)
        self.btnT3_5 = Button(self.root, text=self.T3[5], command=lambda: self.copy_recipe("T3", 5))
        self.btnT3_5.grid(row=6, column=1)
        self.btnT3_6 = Button(self.root, text=self.T3[6], command=lambda: self.copy_recipe("T3", 6))
        self.btnT3_6.grid(row=7, column=1)
        self.btnT3_7 = Button(self.root, text=self.T3[7], command=lambda: self.copy_recipe("T3", 7))
        self.btnT3_7.grid(row=8, column=1)
        self.btnT3_8 = Button(self.root, text=self.T3[8], bg="#FF0000", command=lambda: self.copy_recipe("T3", 8))
        self.btnT3_8.grid(row=9, column=1)
        self.btnT3_9 = Button(self.root, text=self.T3[9], command=lambda: self.copy_recipe("T3", 9))
        self.btnT3_9.grid(row=10, column=1)
        self.btnT3_10 = Button(self.root, text=self.T3[10], command=lambda: self.copy_recipe("T3", 10))
        self.btnT3_10.grid(row=11, column=1)

        self.text3 = Label(self.root, text="T4:", bd=10)
        self.text3.grid(row=0, column=2)
        self.btnT4_0 = Button(self.root, text=self.T4[0], command=lambda: self.copy_recipe("T4", 0))
        self.btnT4_0.grid(row=1, column=2)
        self.btnT4_1 = Button(self.root, text=self.T4[1], command=lambda: self.copy_recipe("T4", 1))
        self.btnT4_1.grid(row=2, column=2)
        self.btnT4_2 = Button(self.root, text=self.T4[2], command=lambda: self.copy_recipe("T4", 2))
        self.btnT4_2.grid(row=3, column=2)
        self.btnT4_3 = Button(self.root, text=self.T4[3], bg="#f28500", command=lambda: self.copy_recipe("T4", 3))
        self.btnT4_3.grid(row=4, column=2)
        self.btnT4_4 = Button(self.root, text=self.T4[4], bg="#ffd700", command=lambda: self.copy_recipe("T4", 4))
        self.btnT4_4.grid(row=5, column=2)

        self.text4 = Label(self.root, text="T5:", bd=10)
        self.text4.grid(row=0, column=3)
        self.btnT5_0 = Button(self.root, text=self.T5[0], bg="#ffd700", command=lambda: self.copy_recipe("T5", 0))
        self.btnT5_0.grid(row=1, column=3)

        self.text5 = Label(self.root, text="combo", bd=10)
        self.text5.grid(row=0, column=4)
        self.btnCombo_0 = Button(self.root, text="通貨", bg="#ffd700", command=lambda: self.combo_recipe(0))
        self.btnCombo_0.grid(row=1, column=4)
        self.btnCombo_1 = Button(self.root, text="傳奇", bg="#f28500", command=lambda: self.combo_recipe(1))
        self.btnCombo_1.grid(row=2, column=4)
        self.btnCombo_2 = Button(self.root, text="甲蟲", bg="#007FFF", command=lambda: self.combo_recipe(2))
        self.btnCombo_2.grid(row=3, column=4)

        self.text4 = Label(self.root, text='Copyright © 2022 shisukon0210.')
        self.text4.grid(row=21)

    def show_all(self):
        print("T1:\n")
        for i in range(27):
            print(str(i) + ":" + self.T1[i] + "\n")
        print("T2:\n")
        for i in range(19):
            print(str(i) + ":" + self.T2[i] + "\n")
        print("T3:\n")
        for i in range(11):
            print(str(i) + ":" + self.T3[i] + "\n")
        print("T4:\n")
        for i in range(5):
            print(str(i) + ":" + self.T4[i] + "\n")
        print("T5\n")
        print("0:" + self.T5[0] + "\n")

    def copy_recipe(self, tier, index):
        if tier == "T2":
            if index == 0:
                result = self.T1[9] + "|" + self.T1[12]
                cb.copy(result)
            if index == 1:
                result = self.T1[5] + "|" + self.T1[20]
                cb.copy(result)
            if index == 2:
                result = self.T1[6] + "|" + self.T1[21]
                cb.copy(result)
            if index == 3:
                result = self.T1[16] + "|" + self.T1[20]
                cb.copy(result)
            if index == 4:
                result = self.T1[17] + "|" + self.T1[26]
                cb.copy(result)
            if index == 5:
                result = self.T1[1] + "|" + self.T1[10]
                cb.copy(result)
            if index == 6:
                result = self.T1[5] + "|" + self.T1[24]
                cb.copy(result)
            if index == 7:
                result = self.T1[0] + "|" + self.T1[14]
                cb.copy(result)
            if index == 8:
                result = self.T1[0] + "|" + self.T1[15] + "|" + self.T1[18]
                cb.copy(result)
            if index == 9:
                result = self.T1[2] + "|" + self.T1[4]
                cb.copy(result)
            if index == 10:
                result = self.T1[3] + "|" + self.T1[18]
                cb.copy(result)
            if index == 11:
                result = self.T1[4] + "|" + self.T1[7]
                cb.copy(result)
            if index == 12:
                result = self.T1[2] + "|" + self.T1[7] + "|" + self.T1[11]
                cb.copy(result)
            if index == 13:
                result = self.T1[8] + "|" + self.T1[13]
                cb.copy(result)
            if index == 14:
                result = self.T1[10] + "|" + self.T1[22]
                cb.copy(result)
            if index == 15:
                result = self.T1[4] + "|" + self.T1[11]
                cb.copy(result)
            if index == 16:
                result = self.T1[12] + "|" + self.T1[25]
                cb.copy(result)
            if index == 17:
                result = self.T1[1] + "|" + self.T1[14]
                cb.copy(result)
            if index == 18:
                result = self.T1[18] + "|" + self.T1[19] + "|" + self.T1[25]
                cb.copy(result)
        if tier == "T3":
            if index == 0:
                result = self.T2[2] + "|" + self.T2[4] + "|" + self.T1[16]
                cb.copy(result)
            if index == 1:
                result = self.T2[1] + "|" + self.T1[10] + "|" + self.T1[21]
                cb.copy(result)
            if index == 2:
                result = self.T2[5] + "|" + self.T1[9] + "|" + self.T1[19]
                cb.copy(result)
            if index == 3:
                result = self.T2[2] + "|" + self.T1[16] + "|" + self.T1[22]
                cb.copy(result)
            if index == 4:
                result = self.T2[12] + "|" + self.T1[1] + "|" + self.T1[15]
                cb.copy(result)
            if index == 5:
                result = self.T2[2] + "|" + self.T1[8]
                cb.copy(result)
            if index == 6:
                result = self.T2[3] + "|" + self.T1[3] + "|" + self.T1[17]
                cb.copy(result)
            if index == 7:
                result = self.T2[5] + "|" + self.T2[17] + "|" + self.T1[24]
                cb.copy(result)
            if index == 8:
                result = self.T2[0] + "|" + self.T2[10] + "|" + self.T2[15]
                cb.copy(result)
            if index == 9:
                result = self.T2[4] + "|" + self.T2[13] + "|" + self.T1[13]
                cb.copy(result)
            if index == 10:
                result = self.T2[3] + "|" + self.T2[11] + "|" + self.T1[26]
                cb.copy(result)
        if tier == "T4":
            if index == 0:
                result = self.T3[0] + "|" + self.T2[9] + "|" + self.T2[18]
                cb.copy(result)
            if index == 1:
                result = self.T3[0] + "|" + self.T2[13] + "|" + self.T2[18]
                cb.copy(result)
            if index == 2:
                result = self.T3[5] + "|" + self.T2[1] + "|" + self.T2[7]
                cb.copy(result)
            if index == 3:
                result = self.T3[3] + "|" + self.T2[6] + "|" + self.T2[7]
                cb.copy(result)
            if index == 4:
                result = self.T3[5] + "|" + self.T3[9] + "|" + self.T3[10] + "|" + self.T2[17]
                cb.copy(result)
        if tier == "T5":
            if index == 0:
                result = self.T4[0] + "|" + self.T4[1] + "|" + self.T2[14] + "|" + self.T2[16]
                cb.copy(result)

    def combo_recipe(self, index):
        if index==0:
            cb.copy("善之觸|海洋王之觸|樹人部落|奇塔弗之觸")
        if index==1:
            cb.copy("夏卡莉之觸|海洋王之觸|招魂師|炎行者|霜行者|風行者")
        if index==2:
            cb.copy("鏡像幻影|樹人部落|刺客|振興")

"""
        self.T1 = ["毒素", "Chaosweaver", "Frostweaver", "Permafrost", "急速", "獵者之眼", "Bombardier", "Flameweaver", "縱火", "奧術緩衝", "回聲者", "Stormweaver",
                   "蓄電", "Bonebreaker", "血書", "Steel-infused", "巨人", "狂戰士", "哨兵", "勇士", "吸血鬼", "充能完畢", "造靈之體", "富饒", "惡語術", "Consecrator",
                   "Frenzied"]
        self.T2 = ["Heralding Minions", "刺客", "死靈法師", "振興之", "劊子手", "Hexer", "Drought Bringer", "Entangler","Treant Horde", "Frost Strider", "冰牢",
                   "烈焰行者", "Evocationist", "Magma Barrier", "鏡像幻影", "Storm Strider", "吸取靈環", "汙染者", "傷害免疫"]
        self.T3 = ["Empowering Minions", "詐欺師", "短暫幻想", "噬魂者", "Empowered Elements", "屍暴者", "Crystal-skinned", "Effigy", "海洋之王之觸", "圖克哈瑪之觸", "艾貝拉斯之觸"]
        self.T4 = ["月神之觸", "日神之觸", "艾爾卡莉之觸", "夏卡莉之觸", "奇塔弗之觸"]
        self.T5 = ["純潔之觸"]
"""

if __name__ == "__main__":
    obj = Filter()
    # obj.show_all()
    mainloop()
