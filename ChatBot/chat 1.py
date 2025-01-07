import tkinter as tk
from tkinter import messagebox
from typing import List, Union
from difflib import get_close_matches
import json

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, questions: List[str]) -> Union[str, None]:
    matches: List = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> Union[str, None]:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
    return None

def teach_bot(new_question: str, new_answer: str, knowledge_base: dict):
    knowledge_base["questions"].append({"question": new_question, "answer": new_answer})
    save_knowledge_base('knowledge_base.json', knowledge_base)
    messagebox.showinfo("Success", "Thank you! The bot learned a new response.")

def chat():
    knowledge_base: dict = load_knowledge_base("knowledge_base.json")

    def send_message():
        user_input = entry.get()
        entry.delete(0, tk.END)

        if user_input.lower() == 'quit':
            root.destroy()
            return

        best_match = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            answer = get_answer_for_question(best_match, knowledge_base)
            if answer:
                chat_history.config(state=tk.NORMAL)
                chat_history.insert(tk.END, f"You: {user_input}\n", "user")
                chat_history.insert(tk.END, f"Bot: {answer}\n\n", "bot")
                chat_history.config(state=tk.DISABLED)
            else:
                messagebox.showinfo("Unknown Question", "Bot: I don't know the answer. Can you teach me?")
                teach_window(best_match)
        else:
            messagebox.showinfo("Unknown Question", "Bot: I don't know the answer. Can you teach me?")
            teach_window(user_input)

    def teach_window(question):
        teach_window = tk.Toplevel(root)
        teach_window.title("Teach Bot")
        teach_window.geometry('500x500+300+200')
        teach_window.resizable(0,0)

        tk.Label(teach_window, text="Question:").pack()
        new_question_entry = tk.Entry(teach_window)
        new_question_entry.insert(tk.END, question)
        new_question_entry.pack()

        tk.Label(teach_window, text="Answer:").pack()
        new_answer_entry = tk.Entry(teach_window)
        new_answer_entry.pack()

        def teach_bot_gui():
            new_question = new_question_entry.get()
            new_answer = new_answer_entry.get()
            if new_question and new_answer:
                teach_bot(new_question, new_answer, knowledge_base)
                teach_window.destroy()
            else:
                messagebox.showerror("Error", "Both question and answer are required.")

        tk.Button(teach_window, text="Teach Bot", command=teach_bot_gui).pack()

    root = tk.Tk()
    root.title("Chat Bot")

    chat_history = tk.Text(root, width=50, height=20, wrap=tk.WORD)
    chat_history.pack(padx=10, pady=10)
    chat_history.tag_configure("user", justify="right")
    chat_history.tag_configure("bot", foreground="blue")

    entry = tk.Entry(root, width=50)
    entry.pack(padx=10, pady=5)
    entry.bind("<Return>", lambda event: send_message())

    send_button = tk.Button(root, text="Send", command=send_message)
    send_button.pack(padx=10, pady=5)

    root.mainloop()

if __name__ == "__main__":
    chat()
