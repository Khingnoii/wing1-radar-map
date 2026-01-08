import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

# ตั้งค่าหน้าเว็บให้กว้างเต็มจอ
st.set_page_config(layout="wide", page_title="Wing 1 Local Data Map")

# --- 1. ส่วนแถบด้านข้าง (Sidebar) ---
with st.sidebar:
    st.header("📍 แผนที่ข้อมูลท้องถิ่น กองบิน 1")
    st.info("Wing 1 Air Base Local Data Map")
    
    # ส่วนแสดงสถิติ (ตัวเลขด้านบน)
    col1, col2 = st.columns(2)
    col1.metric("ไข่แดง", "48", "0-3 กม.")
    col2.metric("ไข่ขาว", "274", "3-5 กม.")
    
    st.divider()
    
    # ส่วนเลือกประเภทสถานที่ (Checkbox)
    st.write("### หมวดหมู่สถานที่")
    show_atm = st.checkbox("ตู้ ATM", value=True)
    show_hotel = st.checkbox("โรงแรม/ที่พัก", value=True)
    show_gas = st.checkbox("ปั๊มน้ำมัน", value=True)
    show_store = st.checkbox("เซเว่น/ร้านค้า", value=True)

# --- 2. ส่วนการสร้างแผนที่ ---
# พิกัดกองบิน 1
lat_wing1, lon_wing1 = 14.9333, 102.0833

m = folium.Map(location=[lat_wing1, lon_wing1], zoom_start=13, control_scale=True)

# วาดวงรัศมี ไข่แดง-ไข่ขาว
folium.Circle([lat_wing1, lon_wing1], radius=3000, color='red', fill=True, fill_opacity=0.1, popup="ไข่แดง 3 กม.").add_to(m)
folium.Circle([lat_wing1, lon_wing1], radius=5000, color='orange', fill=False, popup="ไข่ขาว 5 กม.").add_to(m)

# (ตัวอย่าง) มาร์คจุดจำลอง
if show_store:
    folium.Marker([14.9400, 102.0900], popup="7-Eleven Branch A", icon=folium.Icon(color='green', icon='shopping-cart')).add_to(m)

# --- 3. แสดงผลแผนที่บนหน้าเว็บ ---
st_folium(m, width="100%", height=700)
