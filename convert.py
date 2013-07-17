def convert(msg):
    if msg[1] == "help":
        return "SYNTAX: .convert <conversion type> <number>, eg .convert in-cm 5::CONVERSIONS: in-cm, cm-in (cm/inches) | f-c, c-f (Fahrenheit/Celsius) | km-mi, mi-km (miles/kilometres) | kg-lb, lb-kg (kilograms/pounds)"
    else: 
        try:
            num = msg[2]
            if msg[1] == "in-cm": #inches to cm conversion
                return str(in2cm(num))
            elif msg[1] == "cm-in": #cm to inches conversion
                return str(cm2in(num))
            elif msg[1] == "f-c": #fahrenheit to celsius
                return str(f2c(num))
            elif msg[1] == "c-f": #celsius to fahrenheit
                return str(c2f(num))
            elif msg[1] == "km-mi": #kilometres to miles
                return str(km2mi(num))
            elif msg[1] == "mi-km": #miles to kilometres
                return str(mi2km(num))
            elif msg[1] == "lb-kg": #pounds to kilograms
                return str(lb2kg(num))
            elif msg[1] == "kg-lb": #kilograms to pounds
                return str(kg2lb(num))
            elif msg[1] == "help":
                return "SYNTAX: .convert <conversion type> <number>::CONVERSION TYPES: in-cm, cm-in (cm/inches); f-c, c-f (fahrenheit/celsius); km-mi, mi-km (miles/kilometres); kg-lb, lb-kg (kilograms/pounds)"				
            else:
                return "Not a valid unit conversion"
        except:
            return "Your argument is invalid. See .convert help for usage"


def in2cm(i	):
    i = round(float(i) * 2.54, 2)
    return i
	
def cm2in(i):
    i = round(float(i) / 2.54, 2)
    return i
	
def f2c(i):
    i = round((float(i) - 32) * (5/9.0), 2)
    return i
	
def c2f(i):
    i = round(float(i) * (9/5.0) + 32, 2)
    return i	

def c2k(i):
    i = round(float(i) + 273.15, 2) 
    return i
	
def k2c(i):
    i = round(273.15 - float(i), 2)
    return i
	
def f2k(i):
    i = round(c2k(f2c(i)), 2)
    return i
	
def k2f(i):
    i = round(c2f(k2c(i)), 2)
    return i
	
def km2mi(km):
    mi = round(float(km) * 0.62137, 2)
    return mi
	
def mi2km(mi):
    km = round(float(mi) / 0.62137, 2)
    return km
	
def lb2kg(lb):
    kg = round(float(lb) / 2.2, 2)
    return kg
	
def kg2lb(kg):
    lb = round(float(kg) * 2.2, 2)
    return lb
