import tkinter as tk
from tkinter import messagebox
import storage
from models import Task

class TaskApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("タスク管理")
        self.tasks = storage.load()
        self._build_ui()
        self._refresh()

    def _build_ui(self):
        # 入力エリア
        frame = tk.Frame(self.root)
        frame.pack(pady=8)
        self.entry = tk.Entry(frame, width=30)
        self.entry.pack(side=tk.LEFT)
        tk.Button(frame, text="追加", command=self._add).pack(side=tk.LEFT)

        # タスク一覧
        self.listbox = tk.Listbox(self.root, width=50, height=15)
        self.listbox.pack(pady=4)

        # 操作ボタン
        btn_frame = tk.Frame(self.root)
        btn_frame.pack()
        tk.Button(btn_frame, text="完了にする", command=self._done).pack(side=tk.LEFT, padx=4)
        tk.Button(btn_frame, text="削除",       command=self._delete).pack(side=tk.LEFT, padx=4)

    def _refresh(self):
        """リストボックスを tasks の内容で描き直す"""
        self.listbox.delete(0, tk.END)
        for t in self.tasks:
            prefix = "✅" if t.done else "⬜"
            self.listbox.insert(tk.END, f"{prefix} {t.title}")

    def _add(self):
        title = self.entry.get().strip()
        if not title:
            return
        self.tasks.append(Task(title=title))
        storage.save(self.tasks)
        self.entry.delete(0, tk.END)
        self._refresh()

    def _done(self):
        idx = self.listbox.curselection()
        if not idx:
            messagebox.showinfo("選択してください", "タスクを選んでから押してください")
            return
        self.tasks[idx[0]].done = True
        storage.save(self.tasks)
        self._refresh()

    def _delete(self):
        idx = self.listbox.curselection()
        if not idx:
            return
        self.tasks.pop(idx[0])
        storage.save(self.tasks)
        self._refresh()