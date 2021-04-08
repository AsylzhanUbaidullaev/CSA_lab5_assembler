from pip._vendor.distlib.compat import raw_input

print("Enter your Assembly code")
us_input = ""
bool1 = 0
result = {}


def CheckName(Str):
    Che = Str[0:Str.find(" ")].lower()
    if (Che != "add" and Che != "sub" and Che != "mul" and Che != "div" and Che != "inc" and Che != "dec" and
            Che != "mov" and Che != "xchg"):
        Var = Str[0:Str.find(" ")]
        return Var


def CheckOper(Str):
    global result
    global Dict


def WhatIs(Str):
    Check = Str[0:Str.find(" ")].lower()
    global bool1
    if (Check != "add" and Check != "sub" and Check != "mul" and Check != "div" and Check != "inc" and Check != "dec" and
            Check != "mov" and Check != "xchg"):
        bool1 = 1
    else:
        bool1 = 2


def defineVal(Str):
    if (Str.find("DB ".lower())):
        Val = 0
        global esep
        if (Str[len(Str) - 1:len(Str)] == "h"):
            esep = 16
            Val = int(str(Str[Str.find("DB ".lower()) + 3:len(Str) - 1]), 16)
        elif (Str[len(Str) - 1:len(Str)] == "q"):
            esep = 8
            Val = int(str(Str[Str.find("DB ".lower()) + 3:len(Str) - 1]), 8)
        elif (Str[len(Str) - 1:len(Str)] == "b"):
            esep = 2
            Val = int(str(Str[Str.find("DB ".lower()) + 3:len(Str) - 1]), 2)
        elif (Str[len(Str) - 1:len(Str)] == "d"):
            esep = 10
            Val = int(str(Str[Str.find("DB ".lower()) + 3:len(Str) - 1]))
        else:
            esep = 10
            Val = int(str(Str[Str.find("DB ".lower()) + 3:len(Str)]), 10)
        return Val
    if (Str.find("DW ".lower())):
        Val = str(Str[Str.find("DW ".lower()) + 3:len(Str)])
        return Val
    if (Str.find("DD ".lower())):
        Val = float(Str[Str.find("DD ".lower()) + 3:len(Str)])
        return Val


Rows = []
Dict = {}
Vars = {}
result = {}
esep = 0

while (us_input != "exec"):
    us_input = raw_input(" ")

    if (us_input != "exec"):
        Rows.append(us_input)
        WhatIs(us_input)
        if (bool1 == 1):
            Dict[CheckName(us_input)] = defineVal(us_input)
            Vars[CheckName(us_input)] = defineVal(us_input)
        if (bool1 == 2):
            Str = us_input
            Che = Str[0:Str.find(" ")].lower()
            Var1 = Str.split()[1]
            if (len(Str) != 2):
                Var2 = Str.split()[-1]
            else:
                Var2 = 0
            if (Che == "add"):
                if (esep == 16):
                    result[Var1] = hex(Dict[Var1] + Dict[Var2])
                if (esep == 8):
                    result[Var1] = oct(Dict[Var1] + Dict[Var2])
                if (esep == 2):
                    result[Var1] = bin(Dict[Var1] + Dict[Var2])
                elif (esep == 10):
                    result[Var1] = Dict[Var1] + Dict[Var2]
                    Dict[Var1] = int(Dict[Var1] + Dict[Var2])
            if (Che == "sub"):
                if (esep == 16):
                    result[Var1] = hex(Dict[Var1] - Dict[Var2])
                if (esep == 8):
                    result[Var1] = oct(Dict[Var1] - Dict[Var2])
                if (esep == 2):
                    result[Var1] = bin(Dict[Var1] - Dict[Var2])
                elif (esep == 10):
                    result[Var1] = Dict[Var1] - Dict[Var2]
                    Dict[Var1] = int(Dict[Var1] - Dict[Var2])
            if (Che == "mul"):
                if (esep == 16):
                    result[Var1] = hex(Dict[Var1] * Dict[Var2])
                if (esep == 8):
                    result[Var1] = oct(Dict[Var1] * Dict[Var2])
                if (esep == 2):
                    result[Var1] = bin(Dict[Var1] * Dict[Var2])
                else:
                    result[Var1] = Dict[Var1] * Dict[Var2]
                    Dict[Var1] = int(Dict[Var1] * Dict[Var2])
            if (Che == "div"):
                if (esep == 16):
                    result[Var1] = hex(Dict[Var1] / Dict[Var2])
                if (esep == 8):
                    result[Var1] = oct(Dict[Var1] / Dict[Var2])
                if (esep == 2):
                    result[Var1] = bin(Dict[Var1] / Dict[Var2])
                else:
                    result[Var1] = Dict[Var1] / Dict[Var2]
                    Dict[Var1] = int(Dict[Var1] / Dict[Var2])
            if (Che == "inc"):
                if (esep == 16):
                    result[Var1] = hex(Dict[Var1] + 1)
                if (esep == 8):
                    result[Var1] = oct(Dict[Var1] + 1)
                if (esep == 2):
                    result[Var1] = bin(Dict[Var1] + 1)
                elif (esep == 10):
                    result[Var1] = (Dict[Var1] + 1)
                    Dict[Var1] = int(Dict[Var1] + 1)
            if (Che == "dec"):
                if (esep == 16):
                    result[Var1] = hex(Dict[Var1] - 1)
                if (esep == 8):
                    result[Var1] = oct(Dict[Var1] - 1)
                if (esep == 2):
                    result[Var1] = bin(Dict[Var1] - 1)
                else:
                    result[Var1] = Dict[Var1] - 1
                    Dict[Var1] = int(Dict[Var1] - 1)
            if (Che == "mov"):
                if (esep == 16):
                    result[Var1] = hex(Dict[Var2])
                if (esep == 8):
                    result[Var1] = oct(Dict[Var2])
                if (esep == 2):
                    result[Var1] = bin(Dict[Var2])
                else:
                    result[Var1] = Dict[Var2]
            Dict[Var1] = int(Dict[Var1] + 1)

    print(Vars)
    print(result)