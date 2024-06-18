import tkinter as tk
from tkinter import messagebox

# ウィンドウの作成
root = tk.Tk()
root.title("天才判定くん")

# ウィンドウサイズ設定
root.geometry("400x200")

# メインフレーム
main_frame = tk.Frame(root)
main_frame.pack(pady=20)

# タイトルラベル
title_label = tk.Label(main_frame, text="天才判定くん", font=("Arial", 20))
title_label.pack(pady=10)

# 質問ラベル
question_label = tk.Label(main_frame, text="あなたは天才ですか？", font=("Arial", 14))
question_label.pack(pady=10)

# ボタンフレーム
button_frame = tk.Frame(main_frame)
button_frame.pack(pady=10)

# 関数：yesボタンが押されたとき
def yes_clicked():
    messagebox.showinfo("結果", "おめでとうございます！あなたは天才です！")

# 関数：noボタンが押されたとき
def no_clicked():
    messagebox.showinfo("結果", "あなたは天才ではありません。どんまい！")

# yesボタン
yes_button = tk.Button(button_frame, text="Yes", command=yes_clicked, width=10)
yes_button.pack(side=tk.LEFT, padx=10)

# noボタン
no_button = tk.Button(button_frame, text="No", command=no_clicked, width=10)
no_button.pack(side=tk.LEFT, padx=10)

# メインループ
root.mainloop()

