from node_recursive import *

# node3 = Node(10, None)
# node2 = Node(45, node3)

node1 = Node(23, None)

# newHead = Node(120, None)
# node1.get_next().get_next()

node1.add_to_end(45)
node1.add_to_end(10)
node1.add_to_end(120)

node1.print_list()

node1.delete_from_end()

node1.print_list()

node1.replace_at_index(1, 225)

node1.print_list()

node1.add_at_index(1, 293)

node1.print_list()