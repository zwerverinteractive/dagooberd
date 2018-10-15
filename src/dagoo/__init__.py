import pygame, os
from datetime import datetime
from .readfile import csvdict
from .text import make_font

class Dagooberd():
    def __init__(self):
        self.font = make_font()
        self.table = csvdict("table.csv")
        self.pygame_running = False
        self.running = True
        self.last_hour = 0
        days = ["zondag","maandag","dinsdag","woensdag","donderdag","vrijdag","zaterdag"]
        while self.running:
            current = datetime.now().strftime('%Y %m %w %H %M %S')
            year,month,day,hour,minute,second = current.split(" ")
            if int(day) == 6 and int(hour) == 12 and int(minute) == 30:
                os.system('libreoffice table.csv')
            elif int(hour) > self.last_hour:
                self.last_hour = int(hour)
                try:
                    message = self.table["Timetable"][hour][days[int(day)]]
                    self.run_message(current, message)
                except:
                    pass

    def run_message(self, time, message):
        self.load_pygame()
        while True:
            self.screen.fill((0,0,0))
            current = datetime.now().strftime('%Y %m %d %H %M %S')
            year,month,day,hour,minute,second = current.split(" ")
            if int(minute) == 30:
                self.pygame_running = False
                pygame.quit()
                return
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.pygame_running = False
                    pygame.quit()
                    return
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        self.pygame_running = False
                        pygame.quit()
                        return
            current = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            i = 65 - (len(current)*4)/2
            for c,char in enumerate(current):
                self.screen.blit(self.font["white"][char], (i+(4*c),22))

            i = 65 - (len(message)*4)/2
            for c,char in enumerate(message):
                self.screen.blit(self.font["white"][char], (i+(4*c),28))
            pygame.transform.scale(self.screen, self.resolution, self.window)
            pygame.display.flip()
            self.clock.tick(self.fps)

    def load_pygame(self):
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        pygame.key.set_repeat(20,10)
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.fps = 30
        self.resolution = (1024,720)
        initial_flags = pygame.FULLSCREEN | pygame.DOUBLEBUF
        self.fullscreen = True
        self.resize_window(self.resolution, initial_flags)
        self.resize_screen((128, 128))
        try:
            pygame.mixer.pre_init(44100, -16, 2, 2048)
            pygame.mixer.init()
            pygame.mixer.music.load("alarm.wav")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play(-1)
        except pygame.error:
            print("NO SOUND!")
        self.pygame_running = True

    def resize_window(self, size, flags=0):
        self.wres = size
        self.window = pygame.display.set_mode(self.wres, flags)
        self.zwischen2 = pygame.Surface(self.wres)

    def resize_screen(self, size):
        self.sres = size
        self.screen = pygame.Surface(size)
        self.zwischen = pygame.Surface((size[0]*2, size[1]*2))
