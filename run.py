import os
import streamlit as st
import urllib.parse

# إعدادات صفحة الموقع لتكون متجاوبة
st.set_page_config(
    page_title="مكارون الملوك | Les Macarons Royaux",
    page_icon="🧁",
    layout="wide"
)

# تخصيص التصميم ليكون متناسقاً ورائعاً على الهواتف والشاشات
st.markdown("""
    <style>
    .stButton button {
        width: 100%;
        border-radius: 10px;
        font-weight: bold;
    }
    .main {
        padding: 1rem;
    }
    @media (max-width: 768px) {
        h1 {
            font-size: 1.5rem !important;
        }
        h3 {
            font-size: 1.2rem !important;
        }
    }
    </style>
""", unsafe_allow_html=True)

# نظام التحقق من نوع المستخدم في البداية (Session State)
if 'user_role' not in st.session_state:
    st.session_state.user_role = None

# إذا لم يتم تحديد الدور بعد، نظهر واجهة الاختيار الأولى
if st.session_state.user_role is None:
    st.markdown("<h1 style='text-align: center;'>🧁 مكارون الملوك</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: gray;'>Les Macarons Royaux</h3>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("<h4 style='text-align: center;'>المرجو اختيار نوع الحساب للمتابعة:</h4>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🛍️ أنا زبون\n(Client)", use_container_width=True):
            st.session_state.user_role = "customer"
            st.rerun()
            
    with col2:
        if st.button("👨‍🍳 صانع الحلويات\n(Pâtissier)", use_container_width=True):
            st.session_state.user_role = "pending_admin"
            st.rerun()

elif st.session_state.user_role == "pending_admin":
    st.title("🔐 بوابة صانع الحلويات")
    st.markdown("---")
    entered_code = st.text_input("أدخل كود الدخول الخاصص بك:", type="password")
    
    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("دخول"):
            if entered_code == "2030@2030":
                st.session_state.user_role = "admin"
                st.success("تم تسجيل الدخول بنجاح!")
                st.rerun()
            else:
                st.error("الكود غير صحيح.")
    with col_b:
        if st.button("⬅️ رجوع"):
            st.session_state.user_role = None
            st.rerun()

else:
    # اختيار اللغة (عربي / فرنسي)
    lang = st.sidebar.selectbox("🌐 اختر اللغة / Langue", ["العربية", "Français"])

    # زر العودة لتغيير الدور
    if st.sidebar.button("🔄 تغيير نوع الحساب"):
        st.session_state.user_role = None
        st.rerun()

    if lang == "العربية":
        title_text = "🧁 مكارون الملوك الفاخر"
        subtitle_text = "ألذ وأفخم أنواع المكارون الحلزوني والفرنسي الأصلي المصنوع بخبرة عالية."
        admin_title = "🛠️ لوحة التحكم لإضافة منتج جديد (خاص بصانع الحلويات)"
        prod_name_label = "اسم الحلوى أو النكهة:"
        prod_desc_label = "وصف المنتج:"
        prod_price_label = "الثمن (درهم مغربي):"
        img_upload_label = "اختر صورة المنتج من جهازك:"
        add_btn = "✨ إضافة المنتج للموقع"
        catalog_title = "🛍️ قائمة منتجاتنا الحالية"
        order_box_title = "🛒 اطلب الآن (سيتم إرسال طلبك فوراً عبر واتساب)"
        client_name_label = "اسمك الكريم:"
        client_city_label = "مدينتك (للتوصيل في المغرب):"
        client_phone_label = "رقم هاتفك:"
        client_notes_label = "ملاحظات خاصة (مثلاً: نكهة مفضلة، وقت التوصيل...):"
        order_btn = "📤 إرسال الطلب عبر واتساب"
        delivery_info_title = "🚚 معلومات التوصيل في المغرب"
        delivery_desc = """
        * التوصيل متوفر لكافة المدن المغربية.
        * تبدأ رسوم التوصيل **من 10 درهم إلى 60 درهم** حسب المدينة.
        * للتواصل الهاتفي المباشر: **212671234418+**
        """
        whatsapp_order_number = "212611759969"
        support_phone = "212671234418"
    else:
        title_text = "🧁 Les Macarons Royaux"
        subtitle_text = "Les meilleurs macarons artisanaux faits avec passion et expertise."
        admin_title = "🛠️ Tableau de bord (Pâtissier)"
        prod_name_label = "Nom du produit :"
        prod_desc_label = "Description du produit :"
        prod_price_label = "Prix (MAD) :"
        img_upload_label = "Télécharger l'image :"
        add_btn = "✨ Ajouter le produit"
        catalog_title = "🛍️ Notre Catalogue"
        order_box_title = "🛒 Commander (Envoi direct sur WhatsApp)"
        client_name_label = "Votre Nom :"
        client_city_label = "Votre Ville (Livraison au Maroc) :"
        client_phone_label = "Votre Téléphone :"
        client_notes_label = "Notes spéciales :"
        order_btn = "📤 Envoyer via WhatsApp"
        delivery_info_title = "🚚 Informations de Livraison au Maroc"
        delivery_desc = """
        * Livraison disponible dans toutes les villes du Maroc.
        * Frais de livraison **de 10 MAD à 60 MAD** selon la ville.
        * Contact direct : **+212671234418**
        """
        whatsapp_order_number = "212611759969"
        support_phone = "212671234418"

    st.title(title_text)
    st.write(subtitle_text)
    st.markdown("---")

    # زر واتساب جانبي سريع للتواصل
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"📞 **رقم التواصل المباشر:**\n`+{support_phone}`")
    st.sidebar.markdown(f"[مراسلة عبر الواتساب](https://wa.me/{support_phone})")

    # تخزين المنتجات في الذاكرة المؤقتة
    if 'products' not in st.session_state:
        st.session_state.products = []

    # لوحة التحكم تظهر لصانع الحلويات فقط
    if st.session_state.user_role == "admin":
        st.sidebar.success("✅ وضع صانع الحلويات (نشط)")
        with st.expander(admin_title, expanded=True):
            with st.form("add_product_form_file"):
                p_name = st.text_input(prod_name_label)
                p_desc = st.text_area(prod_desc_label)
                p_price = st.text_input(prod_price_label)
                
                uploaded_file = st.file_uploader(img_upload_label, type=["jpg", "png", "jpeg"])
                
                submitted = st.form_submit_button(add_btn)
                if submitted and p_name and p_price:
                    image_path = None
                    if uploaded_file is not None:
                        os.makedirs("uploads", exist_ok=True)
                        image_path = os.path.join("uploads", uploaded_file.name)
                        with open(image_path, "wb") as f:
                            f.write(uploaded_file.getbuffer())
                    
                    st.session_state.products.append({
                        "name": p_name,
                        "desc": p_desc,
                        "price": p_price,
                        "image": image_path if image_path else "https://images.unsplash.com/photo-1569864358842-78a20d43f9a7?w=500"
                    })
                    st.success("تم إضافة المنتج بنجاح!")
    else:
        st.sidebar.info("👤 وضع الزبون")

    st.markdown("---")
    st.subheader(catalog_title)

    # عرض المنتجات بشكل متجاوب (عمودين أو ثلاثة حسب شاشة الهاتف أو الكمبيوتر)
    if not st.session_state.products:
        st.info("لا توجد منتجات مضافة حالياً. سيتم عرضها هنا فور إضافتها من طرف المحل.")
    else:
        cols = st.columns(2 if st.get_option("client.showSidebarNavigation") else 3)
        for index, prod in enumerate(st.session_state.products):
            # جعل العرض يتكيف مع الشاشات الصغيرة تلقائياً
            col = st.container() if st.sidebar else cols[index % len(cols)]
            with col:
                st.image(prod["image"], use_container_width=True)
                st.markdown(f"### {prod['name']}")
                st.write(prod['desc'])
                st.markdown(f"**السعر / Prix:** {prod['price']} درهم / MAD")
                st.markdown("---")

    # قسم الطلب عبر واتساب
    st.markdown("---")
    st.subheader(order_box_title)

    with st.form("order_form"):
        c_name = st.text_input(client_name_label)
        c_city = st.text_input(client_city_label)
        c_phone = st.text_input(client_phone_label)
        c_notes = st.text_area(client_notes_label)
        
        order_submitted = st.form_submit_button(order_btn)
        
        if order_submitted:
            if not c_name or not c_city or not c_phone:
                st.error("المرجو ملء البيانات الأساسية (الاسم، المدينة، ورقم الهاتف) قبل الإرسال.")
            else:
                message = f"*طلب جديد عبر موقع مكارون الملوك* 🧁\n\n" \
                          f"👤 *الاسم:* {c_name}\n" \
                          f"🏙️ *المدينة:* {c_city}\n" \
                          f"📞 *رقم الهاتف:* {c_phone}\n" \
                          f"📝 *ملاحظات:* {c_notes if c_notes else 'لا توجد ملاحظات'}"
                
                encoded_message = urllib.parse.quote(message)
                whatsapp_url = f"https://wa.me/{whatsapp_order_number}?text={encoded_message}"
                
                st.success(f"شكراً لك يا {c_name}! اضغط على الزر أدناه لإرسال طلبك مباشرة عبر واتساب:")
                st.markdown(f"### [👉 اضغط هنا لإرسال الطلب عبر الواتساب]({whatsapp_url})", unsafe_allow_html=True)

    # قسم معلومات التوصيل
    st.markdown("---")
    st.subheader(delivery_info_title)
    st.markdown(delivery_desc)
