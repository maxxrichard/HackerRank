'''
Given a log of website requests, where each line contains an entry with the following fields
(time, customerId, pageVisited), write an algorithm to find the top 3-page sequence of page
visits for all customers. Each line represents a request (A-Z) made by customer (C#) at
time T to one of the website's pages.

For example, given the following log file containing:

T0,C1,A
T0,C2,E
T1,C1,B
T1,C2,B
T2,C1,C
T2,C2,C
T3,C1,D
T3,C2,D
T4,C1,E
T5,C2,A

Sequence of visits for each customer:

C1 = A -> B -> C -> D -> E

C2 = E -> B -> C -> D -> A

Answer: We see that the most common 3-page sequence visited by a customer is:  B->C->D

'''





def read_log(path:str):
    log = dict()
    with open(path,'r') as file:
      for line in file:
        entry = list(map(str, line.split(',')))
        if entry[1] not in log.keys(): log.update({entry[1]:list(entry[2])})
        else: log[entry[1]].append(entry[2])
    return log


def find_freq(log:dict):
    seq = dict()
    for customer in list(log.keys()):
        sequence = log[customer]
        for i in range(len(sequence)-2):
            window = str(sequence[i]+sequence[i+1]+sequence[i+2])
            if window not in list(seq.keys()):seq.update({window: 1})
            else: seq[window]+=1

    frequent = max(seq, key=seq.get)
    print(f'Most common 3-page sequence is: {frequent}')


#path = '/content/drive/MyDrive/Teaching/data.txt'
#log = read_log(path)
#print(log)

log = {
    'C1': ['A', 'B', 'C', 'D', 'E'],
    'C2': ['E', 'B', 'C', 'D', 'A']
}

find_freq(log)