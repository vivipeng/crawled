import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import time

class DiceRollerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("自定义骰子")

        # 设置窗口大小为 10cm x 10cm (约 378px x 378px)
        window_width = 378
        window_height = 378
        self.root.geometry(f"{window_width}x{window_height}")

        # 默认骰子的六个面
        self.faces = ["面1", "面2", "面3", "面4", "面5", "面6"]

        # 创建标签用于显示骰子结果
        self.result_label = tk.Label(root, text="", font=("Helvetica", 48))
        self.result_label.pack(pady=50)

        # 创建按钮用于掷骰子
        self.roll_button = tk.Button(root, text="掷骰子", command=self.roll_dice, font=("Helvetica", 24))
        self.roll_button.pack(pady=10)

        # 创建按钮用于自定义骰子面
        self.customize_button = tk.Button(root, text="自定义骰子面", command=self.customize_faces, font=("Helvetica", 16))
        self.customize_button.pack(pady=10)

    def roll_dice(self):
        # 禁用按钮以防止多次点击
        self.roll_button.config(state=tk.DISABLED)

        # 模拟骰子滚动效果
        for _ in range(10):
            random_face = random.choice(self.faces)
            self.result_label.config(text=random_face)
            self.root.update()
            time.sleep(0.1)

        # 最终结果
        final_face = random.choice(self.faces)
        self.result_label.config(text=final_face)

        # 启用按钮
        self.roll_button.config(state=tk.NORMAL)

    def customize_faces(self):
        # 弹出对话框让用户输入新的骰子面
        new_faces = []
        for i in range(6):
            face = simpledialog.askstring("自定义骰子面", f"请输入第{i + 1}个面的内容:")
            if face:  # 如果用户输入了内容
                new_faces.append(face)
            else:  # 如果用户没有输入内容，保留默认值
                new_faces.append(f"面{i + 1}")

        # 更新骰子面
        self.faces = new_faces
        messagebox.showinfo("成功", "骰子面已更新！")

if __name__ == "__main__":
    root = tk.Tk()
    app = DiceRollerApp(root)
    root.mainloop()