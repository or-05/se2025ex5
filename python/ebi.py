import tkinter as tk

def add_task():
    text = entry.get()      # 入力欄の文字を取得
    listbox.insert(tk.END, text)  # リストに追加
    entry.delete(0, tk.END)       # 入力欄を空にする

# ウィンドウ
root = tk.Tk()
root.title("タスク管理")

# 入力欄
entry = tk.Entry(root, width=30)
entry.pack()

# ボタン
button = tk.Button(root, text="追加", command=add_task)
button.pack()

# リスト
listbox = tk.Listbox(root, width=40, height=10)
listbox.pack()

root.mainloop()