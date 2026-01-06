import streamlit as st # Gọi thư viện streamlit

# 1. Danh sách cho các trường lựa chọn khác nhau
appetizer = ['Bánh mì nướng phomai', 'Súp hành tây Pháp', 'Salad Caesar', 'Gỏi cuốn', 'Bánh mì bơ tỏi']
main = ['Pizza', 'Pad Thai', 'Steak', 'Moussaka', 'Paella']
dessert = ['Cheesecake', 'Tiramisu', 'Crème brûlée', 'Panna cotta', 'Trifle']

# 2. Tạo các ô lựa chọn với danh sách đã tạo
with st.form('Thực đơn yêu thích'): # Tạo form
    options1 = st.multiselect('Món khai vị ưa thích của bạn?', appetizer)
    options2 = st.multiselect('Món chính ưa thích của bạn?', main)
    options3 = st.multiselect('Món tráng miệng ưa thích của bạn?', dessert)
    submitted = st.form_submit_button('Submit') # Tạo nút Submit

# 3. Xử lý sau khi nhấn nút Submit
if submitted: # Thỏa mãn điều kiện nút submit được bấm
    st.write('Các lựa chọn của bạn là:')
    
    # --- Xử lý Món khai vị ---
    st.write('**1. Món khai vị:**') # In đậm tên đề mục
    if len(options1) == 0: # Điều kiện: Người dùng chưa chọn món nào
        st.write('Bạn chưa chọn món khai vị')
    else: # In các món người dùng đã chọn
        for i in range(len(options1)):
            st.write(options1[i])

    # --- Xử lý Món chính ---
    st.write('**2. Món chính:**')
    if len(options2) == 0:
        st.write('Bạn chưa chọn món chính')
    else:
        for i in range(len(options2)):
            st.write(options2[i])

    # --- Xử lý Món tráng miệng ---
    st.write('**3. Món tráng miệng:**')
    if len(options3) == 0:
        st.write('Bạn chưa chọn món tráng miệng')
    else:
        for i in range(len(options3)):
            st.write(options3[i])