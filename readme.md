<h1>Project Required :dart:</h1>
<ul>
  <li> Python Version: 3.6 [Recommend]</li>
  <li> Docker Desktop</li>
 </ul>
 
 <h1>Settings [แก้ไขให้ตรงกับของตัวเอง] ⚙</h1>
<h3> >>> ไปที่ mysite/setting</h3>
 <ul> 
  <li><h3>DATABASES</h3></li>
  <li><h3>CHANNEL_LAYERS</h3></li>
</ul> 



<h1>Run command follow by this list 🎮</h1>

  <ul>
  <li><h3>Run in Docker</h3></li>
  </ul>
   <ol>
   <li>docker run -p 6379:6379 -d redis:5 </li>
  </ol>
  <ul>
    <li><h3>Run in Virtual Environment</h3></li>
  </ul>
  <ol>
   <li>pip install -r requirements.txt <br>*** สำหรับ [macOS] ใน requirements.txt ให้แก้ psycopg2 เป็น psycopg2-binary ***</li>
   <li>python manage.py migrate</li>
  <li>python manage.py createsuperuser <br>(optional) for create admin user if u want to be admin for django for view in django db, etc(not associate with my project)
and goto localhost:8000/admin
</li>
  <li>python manage.py runserver</li>
 </ol>
 
<h1>ตัวอย่างเว็บไซต์ 💻</h1>
<h3>หน้าเข้าสู่ระบบ</h3>
<img src="./images_for_readme/1.png"/>
<h3>หน้าสมัครสมาชิก</h3>
<img src="./images_for_readme/2.png"/>
<h3>หน้าแรก</h3>
<img src="./images_for_readme/3.png"/>
<h3>หน้าเทรนด์</h3>
<img src="./images_for_readme/4.png"/>
<h3>หน้าแอดมิน</h3>
<img src="./images_for_readme/5.png"/>
<h3>หน้ารายชื่อผู้ใช้งานที่ถูกแบน</h3>
<img src="./images_for_readme/6.png"/>
<h3>หน้าเพิ่มประกาศ</h3>
<img src="./images_for_readme/7.png"/>
<h3>หน้าดูโพสต์ทั้งหมด</h3>
<img src="./images_for_readme/9.png"/>
<h3>หน้าแชท</h3>
<img src="./images_for_readme/10.png"/>
<h3>หน้ากดดูคอมเม้นในโพสต์</h3>
<img src="./images_for_readme/11.png"/>
<h3>หน้าดูโพสต์สำหรับผู้ใช้งานปกติ</h3>
<img src="./images_for_readme/12.png"/>

<h3>หน้าดูรายชื่อผู้ใช้ทั้งหมดของแอดมิน</h3>

<img src="./images_for_readme/13.png"/>

<h3>หน้าแก้ไขประกาศ</h3>

<img src="./images_for_readme/14.png"/>

<h3>หน้าดูประกาศทั้งหมดของแอดมิน</h3>

<img src="./images_for_readme/16.png"/>

