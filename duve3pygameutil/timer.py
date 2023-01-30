import pygame


class Timer:
    def __init__(self, clock: pygame.time.Clock, timeLimit: int, timerStarts=0, oneTime=False):
        assert isinstance(timeLimit, int), "The timeLimit value must be an integer! (Its in milliseconds not seconds)."
        assert isinstance(oneTime, bool), "The oneTime value should be a boolean (true/false)!"

        self.once = oneTime
        self.limit = timeLimit
        self.timer = 0
        self.timerStarts = timerStarts
        self.clock = clock
        self.run = True

    # must be called each frame to ensure a working timer
    def tick(self):
        if self.run:
            self.timer += self.clock.get_time()
            if self.timer > self.limit:
                self.timer = self.timerStarts
                if self.once:
                    self.run = False
                return True  # meaning that the timer has reached the time limit
            else:
                return False  # meaning that the timer hasn't reached the time limit

    def reset(self):
        self.timer = 0
        self.run = True
        self.clock.tick()
