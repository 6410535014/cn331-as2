# Classroom Reservation

ระบบจองห้องเรียน ใช้ **Django Framework** <br>
โดย นายอุกฤษฏ์ ดอกกุหลาบ 6410535014 <br>
Link video: [แสดงและบรรยายการใช้งานทุกฟังก์ชันของระบบ](https://drive.google.com/file/d/1rIJprRaxM0py4lU0G6lsw01sggeFjFyS/view?usp=sharing)

---
## Features

- **Authentication**
  - แยกผู้ใช้เป็น **Admin** (จัดการห้อง) และ **Users** (จองห้อง)

- **Room Management (Admin)**
  - Admin จัดการห้องเรียนผ่าน Django Admin Interface
  - ข้อมูลห้องประกอบด้วย:
    - รหัสห้อง
    - ชื่อห้อง
    - ความจุ
    - ชั่วโมงว่างที่สามารถจองได้
    - สถานะการจอง

- **Room Booking (User)**
  - Users ดูรายการห้องที่เปิดให้จอง
  - Users จองได้ 1 ชั่วโมงต่อห้อง (ห้ามจองห้องซ้ำ)

- **Booking Management**
  - Users ดูรายการห้องที่จองสำเร็จ
  - Users สามารถยกเลิกการจอง โดยชั่วโมงว่างของห้องจะเพิ่มขึ้น

---
