import tkinter as tk

def play_game(root):
    ANS = "2002/08/01"
    MAX_TRIES = 3

    mylabel = tk.Label(root, text='您好，進入猜生日遊戲')
    mylabel.pack()

    return 0


def main():
    root = tk.Tk()
    root.title("Guessing game")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = 600
    window_height = 400

    left = int((screen_width - window_width) / 2)
    top = int((screen_height - window_height) / 2)

    root.geometry(f'{window_width}x{window_height}+{left}+{top}')

    btn = tk.Button(
        root,
        text='我是按鈕',
        font=('Arial', 30, 'bold'),
        padx=10,
        pady=10,
        activeforeground='#f00',
        command=lambda: play_game(root)
    )
    btn.pack()

    root.mainloop()


main()