class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
        self.oldest = None

    def append(self, item):
        # check buffer
        # if buffer is empty
        if len(self.buffer) == 0:
            # add item to the list
            self.buffer.append(item)
            # make the new ithem the "oldest"
            self.oldest = item
            # return oldest item
            return self.oldest
        # the buffer is not empty
        # the buffer is not at capacity
        if len(self.buffer) < self.capacity:
            # add item to the end of the buffer
            self.buffer.append(item)
            # return the added item
            return item
        # the buffer is at capacity
        if len(self.buffer) == self.capacity:
            # get the index of the oldest item
            index_oldest = self.buffer.index(self.oldest)
            # replace the oldest with the new item
            self.buffer[index_oldest] = item
            if (index_oldest + 1) >= len(self.buffer):
                self.oldest = self.buffer[0]
            else:
                self.oldest = self.buffer[index_oldest + 1]

    def get(self):
        # return the buffer
        return self.buffer