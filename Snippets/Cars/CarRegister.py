import Car as c
import BMW as bmw
import AUDI as audi
import JLR as jlr
import MINI as mini
import Person as p

ironman = p.Person("IRON",jlr.JLR("IRON MAN", 2000))
cap = p.Person("COP", audi.AUDI("CAP US", 8000))
hulk = p.Person("HULK", bmw.BMW("HULK ER", 4000))
batm = p.Person("BAT", mini.MINI("BRUS CR", 10000))

people = [ironman, cap, hulk, batm]
people.sort(key=lambda p:p.car.Worth(), reverse=True)

print("In order of worth: richest to poorest")
for p in people:
    print(p.name +' owns '+ p.car.brand+' worth '+str(p.car.Worth()))

