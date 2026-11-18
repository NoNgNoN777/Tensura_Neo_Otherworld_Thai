import json,sys,os
sys.stdout.reconfigure(encoding="utf-8")
n=int(sys.argv[1]);B=120
t=json.load(open("todo.json",encoding="utf-8"))
a=json.load(open(f"ans/{n:03d}.json",encoding="utf-8"))
for i in range((n-1)*B,min(n*B,len(t))):
    if str(i) not in a: print(i,"	",t[i]["keys"][0].split("|")[1].split(".",2)[-1][-48:],"	",json.dumps(t[i]["en"],ensure_ascii=False))
