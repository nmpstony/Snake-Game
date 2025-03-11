from config import *
from config import size
class Object():
    """
    Đây là lớp cơ bản cho các đối tượng trong trò chơi.
    """
    def __init__(self, pos_x = 0, pos_y = 0,type = '', timeremain = 0):
        """
        Khởi tạo đối tượng với vị trí và kích thước cụ thể.
        """
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.type = type
        self.time = timeremain
        self.part = [[(self.pos_x, self.pos_y),self.time]]


class Snake(Object):
    """
    Lớp Snake kế thừa từ lớp Object, đại diện cho con rắn trong trò chơi.
    """
    def __init__(self, pos_x = 0, pos_y = 0, size = size, body = []):
        """
        Khởi tạo con rắn với vị trí, kích thước và cơ thể cụ thể.
        """
        super().__init__(pos_x, pos_y, size)
        self.body = body
        self.body.append([pos_x,pos_y])
    def move(self, dx, dy):
        """
        Di chuyển con rắn theo hướng dx, dy.
        """
        head_x = self.body[0][0] + dx
        head_y = self.body[0][1] + dy
        self.body.insert(0, [head_x, head_y])
        self.body.pop()

