quantity = int(input("จำนวนปืนที่รับมาขาย: "))
print("จำนวนปืนที่รับมาขาย: ", quantity)
cost_price = float(input("ราคาต้นทุนต่อกระบอก: "))
print("ราคาต้นทุนต่อกระบอก: ", cost_price)
sell_price = float(input("ราคาขายต่อกระบอก: "))
print("ราคาขายต่อกระบอก: ", sell_price)
team_member = int(input("จำนวนสมาชิกในทีม: "))
print("จำนวนสมาชิกในทีม: ", team_member)

print("รายงานผลกำไร ")
total_cost = quantity * cost_price
total_sell = quantity * sell_price
profit = total_sell - total_cost
print("ค่าใช้จ่ายรวม: ", total_cost)
print("รายได้รวม: ", total_sell)
print("กำไร: ", profit)

print("เงินที่บอสได้: ", profit - (profit * 0.8))
print("เงินที่สมาชิกต่อคนในทีมได้: ", (profit * 0.8) / team_member)

# หึหึหึหึ เก่งมากครับ น้องมีการตั้งชื่อตัวแปรได้เหมาะสมและอ่านได้เข้าใจสุด ๆ
# แต่อาจจะลองใช้การจัด format รูปแบบ f-string ดูอาจจะง่ายต่อการจัด format output มากกว่าและก็ถ้ามันแสดงทศนิยมยาวเกินไป อาจจะลองใข้ .2f ตามด้วยจำนวนทศนิยมที่ต้องการแสดงดูด้ายนะ เช่นที่พี่ยกตัวอย่างไปก็จะแสดงแค่ 2 ตำแหน่ง
# โดยรวมเก่งมากกกก
# จากพี่รีฟ :D
