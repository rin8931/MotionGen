class BvhLoader:
    def __init__(self):
        self.__node_names = []
        self.__channels = []
        self.offsets = []
        self.frame_positions = []
        self.frame_rotations = []
        self.frame_time = 0
        self.frame_num = 0

    def load(self, file_path):
        f = open(file_path)
        lines = f.readlines()

        self.__read_hierarchy(lines)
        self.__read_motion(lines)

        f.close()

    def __read_hierarchy(self, lines):
        stack = []
        for i in range(len(lines)):
            line = lines[i].strip()
            tokens = line.split(' ')

            if tokens[0] == "HIERARCHY":
                continue
            if tokens[0] == "{":
                stack.append(0)
                continue
            if tokens[0] == "}":
                stack.pop()
                continue
            if tokens[0] == "ROOT" or tokens[0] == "JOINT":
                self.__node_names.append(tokens[1])
                continue
            if tokens[0] == "OFFSET":
                offset = [float(tokens[1]), float(tokens[2]), float(tokens[3])]
                self.offsets.append(offset)
                continue
            if tokens[0] == "CHANNELS":
                self.__channels.append(int(tokens[1]))
                continue
            if tokens[0] == "End":
                continue
            if tokens[0] == "MOTION":
                return

    def __read_motion(self, lines):
        index = 0
        for i in range(len(lines)):
            if lines[i] == "MOTION\n":
                index = i
                break
        self.frame_num = int(lines[index + 1].strip().split('\t')[1])
        self.frame_time = float(lines[index + 2].strip().split('\t')[1])
        for i in range(int(self.frame_num)):
            line = lines[index + i + 3].strip()
            tokens = line.split(' ')
            count_channel = 0
            positions = []
            rotations = []
            for channel in self.__channels:
                position = [0, 0, 0]
                rotation = [0, 0, 0]
                if channel == 3:
                    rotation[0] = float(tokens[count_channel])
                    rotation[1] = float(tokens[count_channel + 1])
                    rotation[2] = float(tokens[count_channel + 2])
                    count_channel = count_channel + 3
                elif channel == 6:
                    position[0] = float(tokens[count_channel])
                    position[1] = float(tokens[count_channel + 1])
                    position[2] = float(tokens[count_channel + 2])
                    rotation[0] = float(tokens[count_channel + 3])
                    rotation[1] = float(tokens[count_channel + 4])
                    rotation[2] = float(tokens[count_channel + 5])
                    count_channel = count_channel + 6
                positions.extend(position)
                rotations.extend(rotation)
            self.frame_positions.append(positions)
            self.frame_rotations.append(rotations)



