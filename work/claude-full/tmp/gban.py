import json,sys,re
W=r'D:\minecraft\Tensura_Neo_Otherworld_Thai\work\claude-full'
C={'black':('Black','ดำ'),'blue':('Blue','น้ำเงิน'),'brown':('Brown','น้ำตาล'),'cyan':('Cyan','ฟ้าอมเขียว'),'gray':('Gray','เทา'),'green':('Green','เขียว'),'light_blue':('Light Blue','ฟ้า'),'light_gray':('Light Gray','เทาอ่อน'),'lime':('Lime','เขียวมะนาว'),'magenta':('Magenta','ม่วงแดง'),'orange':('Orange','ส้ม'),'pink':('Pink','ชมพู'),'purple':('Purple','ม่วง'),'red':('Red','แดง'),'white':('White','ขาว'),'yellow':('Yellow','เหลือง')}
def run(n):
    out={}
    for l in open(W+rf'\tmp\d{n}.txt',encoding='utf-8'):
        if ' = ' not in l: continue
        k,v=l.rstrip('\n').split(' = ',1); v=json.loads(v)
        m=re.search(r'\.desc\.(\w+)$',k)
        if m and m.group(1) in C and v.startswith(C[m.group(1)][0]+' '):
            out[k]=v[len(C[m.group(1)][0])+1:]+' สี'+C[m.group(1)][1]
        else: out[k]=v
    json.dump(out,open(W+rf'\tmp\t{n}.json','w',encoding='utf-8'),ensure_ascii=False); print(len(out))
run(sys.argv[1])
