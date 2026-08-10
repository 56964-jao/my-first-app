import streamlit as st

st.markdown("# :purple[คํานวณดัชนีมวลกาย BMI]")
st.write("🏋️กรอกข้อมูลนํ้าหนักเเละส่วนสูงของคุณ เพื่อเช็คสุขภาพเบื้องต้น🏋️")
weight = st.number_input("กรอกนํ้าหนักของคุณ(กิโลกรัม):", min_value=1.0)
height_cm = st.number_input("กรอกส่วนสูงของคุณ(เซนติเมตร):", min_value=1.0)
if st.button("คํานวณค่า BMI🔄"):
  # แปลงส่วนสู.จาก cm เป็น เมตร เเล้วคํานวณ BMI
  height_m = height_cm / 100
  bmi = weight / (height_m ** 2)
  st.write("--")
  st.header(f"ค่า BMI ของคุณคือ: **{bmi:.2f}**")
  if bmi < 18.5:
    st.warning("💡คุณมีนั้าหนักน้อยกว่าเกณฑ์ (ผอม)")
  elif 18.5 <= bmi < 23.0:
      st.success("🚨คุณมีนั้าหนักในเกณฑ์ปกติ (สุขภาพดี)")
  elif 23.0 <= bmi < 25.0:
        st.info("คุณเริ่มมีนํ้าหนักเกินเกณฑ์ (ท้วม)")
  else:
st.error("🎉คุณอยุ๋ในเกณฑ์อ้วนเเบบอ้วนชิบหาย ควรไปออกกําลังกายเด้อ")
st.divider()
st.write("นาย จ้าวพิภพ พานิชกุล")
