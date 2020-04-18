#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    if t in tickets:
        print(t.source,t.destination)
        hash_table_insert(hashtable,t.source,t.destination)

        print(route,hashtable)
        route[t] = 
    return 
    # return route
    # hash_table_insert(tickets)
    # print(tickets,length)
    # return tickets , length
    # pass


# one = Ticket(4)
ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")
tickets = [ticket_1, ticket_2, ticket_3]
re = reconstruct_trip( tickets,3)
print(re)