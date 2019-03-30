class TV():
    def __init__(self, inch, hz, fhd ):
        self.inch = inch
        self.hz = hz
        self.fhd = fhd

    def __str__(self):
        if self.fhd == True:
            return f"Your Tv has {self.inch}', {self.hz}Hz and is FullHd"
        else:
            return f"Your Tv has {self.inch}', {self.hz}Hz and isn't FullHd"

    def turn_on(self):
        return "Your TV is turn on"

    def turn_off(self):
        return "Your TV is turn off"
