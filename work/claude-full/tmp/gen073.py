import json,sys
sys.stdout.reconfigure(encoding='utf-8')
W=r'D:\minecraft\Tensura_Neo_Otherworld_Thai\work\claude-full'
N=73
D={
'greatsage.filter.sort.recent':"เห็นล่าสุด",'greatsage.filter.sort.samples':"ค่าที่อ่านได้",'greatsage.filter.sort.tier':"ระดับ",
'greatsage.filter.source':"ม็อด",'greatsage.filter.state':"สถานะ",'greatsage.filter.state.all':"ทั้งหมด",
'greatsage.filter.state.analysable':"วิเคราะห์ได้",'greatsage.filter.state.learning':"กำลังดำเนินการ",
'greatsage.filter.state.mastered':"ชำนาญแล้ว",'greatsage.filter.state.missing':"ยังไม่มี",'greatsage.filter.state.owned':"ได้รับแล้ว",
'greatsage.filter.tier':"ระดับ",'greatsage.filter.tier.common':"ทั่วไป",'greatsage.filter.tier.extra':"Extra",
'greatsage.filter.tier.intrinsic':"โดยกำเนิด",'greatsage.filter.tier.ultimate':"Ultimate",'greatsage.filter.tier.unique':"Unique",
'greatsage.filter.tier.unknown':"ไม่จัดระดับ",
}
keys=[l.split(' = ',1)[0] for l in open(W+rf'\tmp\d0{N}.txt',encoding='utf-8').read().split('\n') if ' = ' in l]
out={}
for l in open(W+rf'\tmp\d0{N}.txt',encoding='utf-8'):
    if ' = ' not in l: continue
    k,v=l.rstrip('\n').split(' = ',1)
    a=k.replace('foxablazeaqzl_wiki.wiki.','')
    if a in D: out[k]=D[a]
    elif a.startswith('greatsage.grant.'): out[k]=json.loads(v)
print('keys',len(keys),'out',len(out),[k for k in keys if k not in out])
json.dump(out,open(W+rf'\tmp\t0{N}.json','w',encoding='utf-8'),ensure_ascii=False)
