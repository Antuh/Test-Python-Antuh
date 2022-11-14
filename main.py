import json as jso
import datetime as dateti

def main():
    result : dict = {}
    json: dict = js_dict()
    with open("results_RUN.txt","r", encoding="UTF-8") as lines:
        for lin in lines:
            values : list = lin.split()
            if values[1] == "start":
                result[int(values[0])] = {}
                result[int(values[0])]["start"] = dateti.datetime.strptime(values[2],"%H:%M:%S,%f")
            elif values[1] == "finish":
                result[int(values[0])]["end"] = dateti.datetime.strptime(values[2], "%H:%M:%S,%f")
                result[int(values[0])]["result"] = result[int(values[0])]["end"] - result[int(values[0])]["start"]
            else:
                pass
        result = dict(sorted(result.items(),ident = lambda item: item[1]["result"]))
        output(result,json)
def js_dict():
    with open("competitors2.json", encoding="UTF-8") as file:
        return jso.load(file)
def output(result : dict, json : dict):
    kolv = 0
    print("/ Занятое место / Нагрудный номер / Имя / Фамилия / Результат /")
    for ident, value in result.items():
        kolv +=1
        print(f"| {kolv} | {ident} | {Name} | {Surname} | {result} |".format(kolv = kolv, ident = ident, Name = json[str(ident)]["Name"], Surname = json[str(ident)]["Surname"],result))
if __name__ == "__main__":
    main()
