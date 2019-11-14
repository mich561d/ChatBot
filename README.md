# 4th semester exam project - ChatBot
Create by Jesper C. & Michael Due P.

Last updated: 14th of November, 2019

## Explanation of Project
This project was developed as a exam project for 4. semester in Python.

The program uses multi-threading concept. There are two scripts, one running on the server side and the other on the client side as it is with every chat server. The server relays the messages. The server side script accepts connections and creates 2 threads for every client that connects 
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
- [x] TensorFlow integration
- [x] Logging
    - [x] Logging of conversations
    - [x] Logging of exceptions
    - [x] Logging of Connections
    - [x] Logging of TensorFlow Learning time
- [ ] Data
    - [x] Common data
    - [ ] Convert logging of conversations to JSON
    - [ ] Camping data
    - [ ] Bunch of data
- [ ] Self-learning of log files
- [ ] Matlib-plots
    - [x] Time intervals of chats
    - [x] When is there chat activity and what is the activity level 
    - [x] How long does TensorFlow use to train it self
    - [x] How often can TensorFlow not respond
    - [ ] What tags is most used
    - [ ] Where does the customers come from
    - [ ] How many times does a customer chat
    - [x] Ratings from customers
- [ ] Create facade class
- [ ] Client-based GUI
- [ ] Intern-based GUI
- [ ] Multi-language

## Installation of Project
Open command prompt and do : `git clone https://github.com/mich561d/ChatBot.git`

Setup correct version of Python:
- `conda create -n "name" python=3.6`
- `conda activate "name"`
- `conda deactivate "name"`

Install dependencies:
- `pip install numpy`
- `pip install nltk`
- `pip install tensorflow==1.14`
- `pip install tflearn`

If this is your first time running the project you have to run the method `downloadNLTK()` in the `brain.py` script 

Edit settings files and then:
1. Invoke server from the terminal as : `Python chatBot-server.py`
2. Invoke client from the terminal as : `Python chatBot-client.py`

## Development environment :
- Windows 10 Pro
- Windown CMD (Server / Brain)
- Python 3.6.9 (Server / Brain)
- Git Bash (Client)
- Python 3.7.3 (Client)
- Visual Studio Code v1.39.2

## Proof of concept (Danish)
### Hvad vil vi?

Vi vil designe og udvikle et kommunikationsværktøj skrevet i Python. Opbygningen af systemet består af en client-server arkitektur. Ved hjælp at TensorFlow vil vi kunne manipulere data som vores chat-bot kan bruge til at interagere med brugerne. Vi vil ved hjælp af logging danne ny data som vores chat-bot kan lære ud fra og blive bedre.

På klient-siden af kommunikationsværktøjet vil vi udarbejde en GUI som brugeren kan interagere med. Den skal holde et minimalistisk design som kun kan sende input til serveren og tage imod output til brugeren, lukke for chatten og give mulighed for en rating.

Server-siden skal det meste af chat-bottens funktionalitet ligge udover selvfølgelig at kunne kommunikere med brugeren. Her vil vi give mulighed for virksomheden at kunne holde et overblik over hvilke chats der er, se tidligere samtaler ved hjælp af logning og give statistik over de enkelte samtaler samt chat-bottens brugere.

Vi vil bruge TensorFlow frameworket til at give vores chat-bot en simpel form for kunstig intelligens.

Når ovenstående er klaret, skal der endvidere implementeres multi-language funktionalitet, så chat-botten kan bruges af flere brugere, da den kan tage imod input fra flere sprog, og give output i samme sprog.

### Hvad har vi?

Vi har udviklet størstedelen af vores arkitektur, som består af en server som kan snakke sammen med en eller flere klienter. Alt brugerinteraktion foregår gennem kommandoprompt, og bruger kan kun på nuværende tidspunkt skrive til serveren, hvorefter at, serveren laver et echo, som skriver inputtet tilbage til brugeren, men er meget tæt på at kunne integrere TensorFlow på chat-botten. Brugeren har også mulighed for at afslutte chatten ved at skrive ‘exit’. Både serveren og klienten har begge to tråde til rådighed, den ene er en læse-tråd og den anden en skrive-tråd. Klientens skrive-tråd skriver til serverens læse-tråd, som siger til serverens skrive-tråd at klienten skal have en svar på klientens læse-tråd.

Vi har også udviklet fundamentet for vores machine learning del. Den kan på nuværende tidspunkt læse data fra en JSON fil og ud fra den fil træne en model ved hjælp af frameworket TFLearn og dets algoritmer. Vi har også opsat en basal chat funktion for at kunne teste trænings modellen. Hvis spørgsmålets probability er mindre end 70% vil der smides en fejl for at mindske at give forkerte svar.

### Hvad er næste step?

Det første vi skal gøre er at integrere de to systemer så client-serveren kan bruge trænings modellen og give mere end bare et echo svar tilbage.

Det næste der skal implementeres, for at optimere chat-botten, er at indhente en masse data og sætte det ind i JSON filen som TensorFlow læser og træner fra så der er større sandsynlighed for at botten kan give et rigtigt svar.

Vi skal også implementere logging fra samtalerne som bliver gemt i det rigtige format så det nemt og hurtigt kan blive implementeret i JSON filen så chat-botten kan blive bedre. De logget samtaler skal vi også bruge til at kunne danne statistiker så virksomheden som bruger systemet, kan holde øje med chat-bottens performance og kundernes tilfredshed. Disse statistikker vil være: 
- Chattens tidsvarihed
- Hvornår der er aktivitet og aktivitetsniveauet 
- Hvor lang tid TensorFlow bruger på at træne sig selv
- Hvor lang tid TensorFlow bruger på at danne svar
- Hvor tit TensorFlow ikke kan komme frem til et godt nok svar
- Hvilke tags der bliver brugt mest
- Hvor kunderne kommer fra
- Hvor mange gange samme kunde kommer ind
- Ratings fra brugerne

For at kunne forbedre kundernes oplevelse ved brug af chat-botten skal vi have udviklet en simpel GUI som gør det nemt og enkelt for kunderne at holde en samtale med botten. Det vil bestå udelukkende af et interface for at se beskederne. På nuværende tidspunkt har vi tænkt os at bruge TkInter som vores GUI framework, men skulle vi finde et mere elegant framework, vil det blive brugt.

Samme framework vil vi bruge til at udvikle en GUI som virksomhederne bruger internt. Her skal de have mulighed for at holde styr på samtalerne med kunderne og se de tidligere nævnte statistikker på chat-botten.

Skulle vi have tid til overs vil vi også implementere multi language support.
