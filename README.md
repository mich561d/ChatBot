# 4th semester exam project - ChatBot
Create by Jesper C. & Michael Due P.

## Explanation of Project
This project was developed as a exam project for 4. semester in Python.

The program uses multi threading concept. There are two scripts, one running on the server side and the other on the client side as it is with every chat server. The server relays the messages. The server side script accepts connections and creates 2 threads for every client that connects 
- One to process and respond to the `who`, `wholast`, `send`, `broadcast` commands to the client
- One to keep sending the messages that are destined to the client.

Similarly the client uses two threads, one for prompting commands from user and getting inputs. The other thread receives chat messages from the server and displays them. **Note :** The responses for the commands are received in thread 1 

Each pair of thread is connected by a separate socket. (2 sockets are used per client-server) 
One socket between server and client is exclusively used for the server to get the messages from the clients message queue and send it to the client thread that receives the chat messages.

Shared queues are used. When a connection occurs, a queue is added to the set of queues with the index being the file descriptor of the connection. Hence every client has a separate index and therefore a separate queue in the server. All queues belong to the set send queue. 

A message intended for the client is put into the respective queue and the other thread is responsible for taking these messages out of the queue and send it to the appropriate client.

Every queue access is wrapped up in a mutex lock to prevent clashes or race condition.

Common lists are used to store the information of online users, blocked users, offline users and mapping between username and the file descriptor to access the sendqueue.

Offline messaging implementation : The offline messaging system works in such a way that it stores the offline messages on a file that is allocated to the client (Every client has a text file which has their respective chat history). The inbox command makes the server retrieve command from the file and send it across the client.

**Note :** File system is used instead of queue because queue cannot show history. Also offline messages is not available for broadcasted messages. Broadcast is generally done only to those who are online.

**Note :** The chat messages gets displayed without any proper alignment on the terminal screen. Sometimes they might clash with the command prompt. 

### Core Features
- Client/Server architecture
- Client-based GUI
- Server-based GUI
- Intern-based GUI
- TensorFlow integration
- Multi-language supported

## Installation of Project
open command prompt and do : `git clone https://github.com/mich561d/ChatBot.git`

There are only two scripts. Place them on the different systems. If same systems use 127.0.0.1 as the address. 

Server is invoked from the terminal as : `Python chatBot-server.py <port number>`

Client is invoked from the terminal as : `Python chatBot-client.py <TCP ip address of the server> <port number>`

Commands to use from Client:
1. `whoelse` : displays other users who are online
2. `wholast` : lastnumber displays the users who were online until lastnumber minutes ago
3. `send <user> <message>` : sends \<message\> to \<user\>
4. `Broadcast <message>` : displays \<message\> to the users who are online
5. `Broadcast <user> <list of users> <message>` :  broadcasts the \<message\> to \<list of users\>
6. `Inbox` : Shows the messages that were sent when the client was offline. It also shows chat history.

## Development environment :
- Windows 10 Pro
- Bash shell
- Python 3.7.3
- Visual Studio Code v1.38.1
- 8th of October, 2019
