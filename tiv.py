from PIL import Image
import PIL, sys

tupleAverage = lambda v: sum(v)/3

def svalue(value):
    shade_Map = {
        0   <= value <= 51:  chr(0),
        52  <= value <= 102: chr(176),
        103 <= value <= 153: chr(177),
        154 <= value <= 204: chr(178),
        205 <= value <= 255: chr(219)
    }
    return shade_Map[True] #genius

file       = sys.argv[1]
initial_im = Image.open(file)
termLength = 80 #adjust accordingly
parity     = (termLength/float(initial_im.size[0]))
endsize    = int((float(initial_im.size[1])*float(parity)))
initial_im = initial_im.resize((termLength,endsize), PIL.Image.ANTIALIAS)
IIData     = list(initial_im.getdata())
averages   = [tupleAverage(pix) for pix in IIData]
values     = ''.join([svalue(v) for v in averages])

chop = lambda o, l: [o[i:i+l] for i in range(0, len(o), l)]  #For copypasta
newline_splitted = '\n'.join(chop(values, termLength))

print values
