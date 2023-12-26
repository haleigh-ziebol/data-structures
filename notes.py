# Stack
    # last in first out (LIFO)
    # like a driveway
    # linear, take elements from top when remove
    # push = add on top, pop = remove top, peek = look at data on top
    # time efficient

# Queue
    # first in first out (FIFO)
    # like line of ppl waiting for bus
    # linear added on one side (end), removed from other (front)
    # handle tasks with asyncronous processing such as on web servers
    # dequeue - removes front item and hands it over, size reduced (altered state) and sets up new head
    # enqueue - adds new element to end of queue
    # front - read only access to front item (like peek in stack)
    # dequeue, enqueue, front = O(1)

# Trees
    # root node - 1st, initial node that all other nodes branch from (no parent)
    # edges - link between 2 nodes, establish parent, child relationship
    # node - holds data, connection point for other nodes
    # leaf node - no child node branching out (can signify reaching conclusion or solution for algorithm)
    # help DB execute queries quickly; data easier to sort, update, access
    # O log n, logarithmic time; divide problem space in half at each interval
    # Binary search tree- everything on right is bigger than on left
    # balanced tree - branches are not signficantly longer or more branched
        ## otherwise can degrade to linear performance
