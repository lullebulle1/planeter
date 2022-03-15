
class Planat:
    def __init__ (self, name, size):
        self.name = name
        self.size = size
        self.moons = []

    def get_size(self) -> None:
        return self.size
    
    def get_name(self):
        return self.name

    def get_moons(self):
        return self.moons
    
    def add_moon(self, moon):
        self.moons.append(moon)

    def print_moons(self):
        for moon in self.moons:
            print(moon.get_name())

    def certain_size(self, size):
        print(f"the following moons around {self.get_name()} larger then {size} sqkm")
        for moon in self.moons:
            print(moon.get_name())


class Moons:
    def __init__ (self, name, size):
        self.name = name
        self.size = size
        self.orbits = None

    def get_size(self) -> None:
        return self.size
    
    def get_name(self):
        return self.name

    def get_orbit(self):
        return self.orbits
    
    def add_orbit(self, orbit):
        self.orbits = orbit






def main():
    tellus = Planat("Tellus", 5.101e8)
    mars = Planat("Mars", 1.448e8)
    jupiter = Planat("jupiter", 6.142e10)


    luna = Moons("Luna", 3.8e7)
    phobos = Moons("Phobos", 1.5483e4)
    daimos = Moons("daimos", 494 )
    europa = Moons("Europa", 3.09e7)
    io = Moons("IO", 4.19e7)
    

    tellus.add_moon(luna)
    mars.add_moon(phobos)
    mars.add_moon(daimos)
    jupiter.add_moon(europa)
    jupiter.add_moon(io)
    

    luna.add_orbit(tellus)
    phobos.add_orbit(mars)
    daimos.add_orbit(mars)
    europa.add_orbit(jupiter)
    io.add_orbit(jupiter)

    tellus.print_moons()
    jupiter.print_moons()

    mars.certain_size(1000)

if __name__ == "__main__":
    main()

    

  
        

    
