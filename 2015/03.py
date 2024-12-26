from util import *

print(graph2d().moves(D).visited_num())
print(graph2d().moves(D[::2]).reset_pos().moves(D[1::2]).visited_num())
