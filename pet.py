class Pet:
    def init(self, name, energy_level):
        self.name = name
        self.energy_level = energy_level

    def feed_pet(self):
        self.energy_level += 10
        print(f"{self.name} is fed! Energy level is now {self.energy_level}")