import tkinter as tk
import socket
import threading


class ChatApp:
    def __init__(self, master):
        self.master = master
        master.title("Chat Application")

        self.messages = tk.Text(master, state='disabled')
        self.messages.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()
        self.entry.bind("<Return>", self.send_message)

        self.server_thread = threading.Thread(target=self.start_server, daemon=True)
        self.server_thread.start()

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('localhost', 12345))

    def start_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('localhost', 12345))
        server_socket.listen(1)
        print("Server is listening for connections...")
        client_socket, address = server_socket.accept()
        print(f"Connection from {address} has been established!")

        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if message.lower() == 'exit':
                break
            self.show_message(f"Client: {message}")

        client_socket.close()
        server_socket.close()

    def show_message(self, message):
        self.messages.config(state='normal')
        self.messages.insert(tk.END, message + "\n")
        self.messages.config(state='disabled')
        self.messages.yview(tk.END)

    def send_message(self, event):
        message = self.entry.get()
        self.show_message(f"You: {message}")
        self.entry.delete(0, tk.END)

        # Send the message to the server
        self.client_socket.send(message.encode('utf-8'))
        if message.lower() == 'exit':
            self.client_socket.close()
            self.master.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()
