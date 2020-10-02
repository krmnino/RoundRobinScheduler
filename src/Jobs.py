class Jobs:
    tag = ''
    time_requested = 0
    finished = False

    def __init__(self, tag_, time_requested_):
        self.tag = tag_
        self.time_requested = time_requested_

