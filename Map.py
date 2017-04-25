class Map:
    def __init__(self):
        self.start = [9, 1]
        self.end = [0, 8]
        self.map = [
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 1, 1, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
            [0, 1, 1, 1, 0, 1, 0, 1, 1, 1],
            [0, 1, 0, 0, 0, 1, 0, 1, 0, 0]]
        self.width = len(self.map[0])
        self.height = len(self.map)
        self.answers = [{"x": 2, "y": 2, "answer": "right"}, {"x": 2, "y": 4, "answer": "up"},
                        {"x": 5, "y": 4, "answer": "left"}, {"x": 7, "y": 8, "answer": "up"},
                        {"x": 4, "y": 2, "answer": "right"}]
        self.cross_roads = self.get_cross_roads()

    def get_cross_roads(self):
        cross_roads = []
        for y in range(1, self.height - 1, 1):  # вертикаль
            for x in range(1, self.width - 1, 1):  # горизонталь
                up = self.map[y - 1][x]
                down = self.map[y + 1][x]
                left = self.map[y][x - 1]
                right = self.map[y][x + 1]
                if up + down + left + right > 2 and self.map[y][x] == 1:
                    cross_roads.append({"up": up, "left": left, "right": right, "down": down, "x": x, "y": y})
        return cross_roads

    def get_data(self):
        X_data = []
        y_data = []
        direct_ratio = {"up" : [1,0,0,0],"right":[0,1,0,0],"down":[0,0,1,0],"left":[0,0,0,1]}
        for i in self.cross_roads: # О(n^2) !!!
            append_data = [i["up"], i["right"], i["down"], i["left"], i["x"] / self.width, i["y"] / self.height]
            X_data.append(append_data)
            for j in self.answers:
                if append_data[4] == j["x"] / self.width and append_data[5] == j["y"] / self.height:
                    y_data.append(direct_ratio[j['answer']])
        return {"X_data" : X_data, "y_data" : y_data}

def get_data(n):
    if n == 1:
        X_train = [[0, 1, 1, 1, 1, 0],[0, 1, 1, 1, 4, 0], [1, 0, 1, 1, 2, 2],[1, 1, 0, 1, 4, 4], [1, 1, 0, 1, 3, 4],[1, 1, 0, 1, 1, 4],[0, 1, 1, 1, 1, 5],[0, 1, 1, 1, 2, 5],[1, 0, 0, 1, 3, 6], [0, 1, 1, 1, 5, 5],[1, 1, 1, 1, 6, 5],[1, 0, 0, 1, 6, 6], [1, 0, 1, 1, 6, 3],[1, 1, 0, 1, 8, 6],[1, 1, 0, 1, 9, 6],[1, 1, 1, 0, 7, 1],[0, 1, 1, 1, 8, 0],[1, 0, 1, 1, 8, 1],[0, 1, 1, 1, 9, 0],[1, 1, 0, 1, 9, 3]]
        y_train = [[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 1, 0],[0, 0, 1, 0], [0, 0, 1, 0],[0, 0, 1, 0],[0, 1, 0, 0],[0, 1, 0, 0],[0, 1, 0, 0], [0, 1, 0, 0],[0, 1, 0, 0],[1, 0, 0 ,0], [0, 0, 1, 0],[1, 0, 0 ,0],[0, 0, 1, 0],[0, 1, 0, 0],[0, 1, 0, 0],[1, 0, 0 ,0],[0, 0, 1, 0],[0, 1, 0, 0]]
        nb_epoch = 4200
    elif n == 2:
        X_train = [[0,1,1,1,11,1],[1,1,1,0,11,4],[1,1,1,1,10,3],[0,1,1,1,5,1],[1,0,1,1,7,5],[0,1,1,1,6,5],[0,1,0,1,5,5],[0,1,1,1,5,3],[1,1,0,1,3,5],[1,1,1,0,2,5],[1,0,1,1,2,4],[1,1,1,0,1,4]]
        y_train = [[0,0,1,0],[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,0,0,1],[0,0,0,1],[0,0,0,1],[0,0,1,0],[0,0,0,1],[1,0,0,0],[0,0,0,1],[1,0,0,0]]
        nb_epoch = 400
    return [X_train,y_train,nb_epoch]

if __name__ == '__main__':
    map = Map();
    print(map.get_data()["X_data"])
    print(map.get_data()["y_data"])
