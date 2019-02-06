class Memory:
    def __int__(self, RAM, ROM):
        self.RAM = RAM
        self.ROM = ROM
    def prints(self):
         print("hai hello")
class Computer:
    def __int__(self, model, version):
        self.model = self.model
        self.version = self.version

    def show_details(self):
        print("model of the computer :", self.model)
        print("version of the computer:", self.version)
        print(self.version.prints())


composition2 = Memory(16, 32)
composition = Computer("HP", 3.4, composition2)
composition2.show_details()
