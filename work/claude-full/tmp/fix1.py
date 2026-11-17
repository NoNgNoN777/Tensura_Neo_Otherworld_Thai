import json,sys
p=r'D:\minecraft\Tensura_Neo_Otherworld_Thai\translation-src\lang\tensura\lang\th_th.json'
d=json.load(open(p,encoding='utf-8'))
fx={
'tensura.skill.mode.cannot_change':'คุณไม่ผ่านเงื่อนไขในการเปลี่ยนเป็นโหมดนั้นของ %s',
'tensura.skill.mode.need_toggle_off':'ต้องปิดความสามารถพาสซีฟของ %s ก่อนจึงจะใช้ความสามารถนี้ได้',
'tensura.skill.mode.need_toggle_on':'ต้องเปิดความสามารถพาสซีฟของ %s ก่อนจึงจะใช้ความสามารถนี้ได้',
'tensura.skill.mode.unyielding.backup_different_dimension':'ภาชนะสำรอง (Backup) อยู่คนละมิติ',
}
for k,v in fx.items():
    print(k,'|',d[k]); d[k]=v
json.dump(d,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
