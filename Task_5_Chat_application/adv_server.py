import tkinter as tk
import socket
import threading

class ChatApp:
    def __init__(self, master):
        self.master = master
        master.title("Chat Application")

        self.messages = tk.Text(master)
        self.messages.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()
        self.entry.bind("<Return>", self.send_message)

        self.server_thread = threading.Thread(target=self.start_server)
        self.server_thread.start()

    def start_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('localhost', 12345))
        server_socket.listen(1)
        client_socket, address = server_socket.accept()

        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if message.lower() == 'exit':
                break
            self.messages.insert(tk.END, f"Client: {message}\n")

        client_socket.close()
        server_socket.close()

    def send_message(self, event):
        message = self.entry.get()
        self.messages.insert(tk.END, f"You: {message}\n")
        self.entry.delete(0, tk.END)

        # Add socket code to send message to server here

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()
