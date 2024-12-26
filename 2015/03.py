from util import *

print(graph2d().moves(raw()).visited_num())
print(graph2d().moves(raw()[::2]).reset_pos().moves(raw()[1::2]).visited_num())
