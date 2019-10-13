# 4th semester exam project - ChatBot
Create by Jesper C. & Michael Due P.

## Explanation of Project
This project was developed as a exam project for 4. semester in Python.

The program uses multi threading concept. There are two scripts, one running on the server side and the other on the client side as it is with every chat server. The server relays the messages. The server side script accepts connections and creates 2 threads for every client that connects 
- One to process and respond to the commands from and to the client
- One to keep sending the messages that are destined to the client.

Similarly the client uses two threads
- One for prompting commands from user and getting inputs. 
- One for receives chat messages from the server and displays them. 

**Note :** The responses for the commands are received in thread 1 

Each pair of thread is connected by a separate socket. (2 sockets are used per client-server) 
One socket between server and client is exclusively used for the server to get the messages from the clients message queue and send it to the client thread that receives the chat messages.

Shared queues are used. When a connection occurs, a queue is added to the set of queues with the index being the file descriptor of the connection. Hence every client has a separate index and therefore a separate queue in the server. All queues belong to the set send queue. 

A message intended for the client is put into the respective queue and the other thread is responsible for taking these messages out of the queue and send it to the appropriate client.

Every queue access is wrapped up in a mutex lock to prevent clashes or race condition.

**Note :** The chat messages gets displayed without any proper alignment on the terminal screen. Sometimes they might clash with the command prompt. 

### Core Features
- [x] Client/Server architecture
- [ ] Client-based GUI
- [ ] Server-based GUI
- [ ] Intern-based GUI
- [ ] TensorFlow integration
- [ ] Multi-language supported

## Installation of Project
open command prompt and do : `git clone https://github.com/mich561d/ChatBot.git`

There are only two scripts. Place them on the different systems. If same systems use 127.0.0.1 as the address. 

Server is invoked from the terminal as : `Python chatBot-server.py <port number>`

Client is invoked from the terminal as : `Python chatBot-client.py <TCP ip address of the server> <port number>`

Commands to use from Client: `TODO`

## Development environment :
- Windows 10 Pro
- Bash shell
- Python 3.7.3
- Visual Studio Code v1.38.1
- 10th of October, 2019
