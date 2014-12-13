from PIL import Image
import PIL, os

tupleAverage = lambda v: sum(v)/3

shade_Map = {
    0: chr(0),
    1: chr(176),
    2: chr(177),
    3: chr(178),
    4: chr(219)
}

def shaderValue(value):
    if 0 <= value <= 51:
        return 0
    elif 52 <= value <= 102:
        return 1
    elif 103 <= value <= 153:
        return 2
    elif 154 <= value <= 204:
        return 3
    elif 205 <= value <= 255:
        return 4
    else:
        raise ValueError, "Not in any range"

file       = "cat.jpg"
initial_im = Image.open(file)
termLength = 80
parity     = (termLength/float(initial_im.size[0]))
endsize    = int((float(initial_im.size[1])*float(parity)))
initial_im = initial_im.resize((termLength,endsize), PIL.Image.ANTIALIAS)
IIData     = list(initial_im.getdata())
averages   = [tupleAverage(pix) for pix in IIData]
values     = [shaderValue(v) for v in averages]
printable  = ''.join([shade_Map[n] for n in values])

print printable



os.system("pause")