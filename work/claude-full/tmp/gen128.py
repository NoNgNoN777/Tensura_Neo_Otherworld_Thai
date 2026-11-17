import sys
sys.path.insert(0,r'D:\minecraft\Tensura_Neo_Otherworld_Thai\work\claude-full\tmp')
from gt import run
Y='text.yigd.message.'
D={
'ymktn.gpu.integrated.message':"คุณกำลังใช้ %s แต่มี GPU แยก (%s) ให้ใช้ เปลี่ยนไปใช้ GPU แยกเพื่อประสิทธิภาพที่ดีขึ้น ตรวจสอบการตั้งค่ากราฟิกใน Windows หรือแผงควบคุม GPU ของคุณ",
Y+'rob.too_early':"คุณปล้นหลุมศพนี้ไม่ได้จนกว่าจะถึง %s",
Y+'missing_key':"คุณไม่มีกุญแจที่ถูกต้องเพื่อปลดล็อกหลุมศพนี้",
Y+'no_shovel':"คุณต้องใช้พลั่วเพื่อปล้นหลุมศพนี้",
Y+'sellout_player':"%s ออกจากเกม และมีหลุมศพที่ X: %d / Y: %d / Z: %d / %s",
Y+'inform_robbery':"หลุมศพของคุณหลุมหนึ่งถูกปล้น",
Y+'inform_robbery.with_details':"%s ปล้นหลุมศพของคุณหลุมหนึ่ง",
Y+'grave_location':"หลุมศพของคุณอยู่ที่ X: %d / Y: %d / Z: %d / %s",
Y+'on_day':" ในวันที่ %d",
Y+'irl_time':" (%d %s, %d, %d:%d%s)",
Y+'grave_destroyed':"หลุมศพของคุณถูกทำลายโดยไม่คาดคิด หากมีสิทธิ์ที่เหมาะสม กู้คืนหลุมศพได้ด้วยคำสั่ง /yigd",
Y+'grave_relocated':"หลุมศพของคุณถูกย้ายไปที่ X: %d / Y: %d / Z: %d / %s",
Y+'grave_generation_error':"สร้างหลุมศพล้มเหลว ทิ้งไอเทม",
}
run(128,D)
