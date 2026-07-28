import os
import streamlit as st
import urllib.parse

# إعدادات صفحة الموقع
st.set_page_config(
    page_title="مكارون الملوك | Les Macarons Royaux",
    page_icon="🧁",
    layout="wide"
)

# نظام التحقق من نوع المستخدم في البداية (Session State)
if 'user_role' not in st.session_state:
    st.session_state.user_role = None

# إذا لم يتم تحديد الدور بعد، نظهر صفحة الاختيار الأولى
if st.session_state.user_role is None:
    st.title("🧁 مرحباً بك في مكارون الملوك | Les Macarons Royaux")
    st.markdown("---")
    st.subheader("المرجو اختيار نوع الحساب للمتابعة / Veuillez choisir votre profil :")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🛍️ أنا زبون (Client)", use_container_width=True):
            st.session_state.user_role = "customer"
            st.rerun()
            
    with col2:
        if st.button("👨‍🍳 أنا صانع الحلويات (Pâtissier / Admin)", use_container_width=True):
            st.session_state.user_role = "pending_admin"
            st.rerun()

elif st.session_state.user_role == "pending_admin":
    st.title("🔐 بوابة صانع الحلويات")
    st.markdown("---")
    entered_code = st.text_input("أدخل كود الدخول الخاص بصانع الحلويات:", type="password")
    
    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("دخول"):
            if entered_code == "2030@2030":
                st.session_state.user_role = "admin"
                st.success("تم تسجيل الدخول بنجاح!")
                st.rerun()
            else:
                st.error("الكود غير صحيح، حاول مرة أخرى.")
    with col_b:
        if st.button("⬅️ رجوع"):
            st.session_state.user_role = None
            st.rerun()

else:
    # اختيار اللغة (عربي / فرنسي)
    lang = st.sidebar.selectbox("🌐 اختر اللغة / Choisir la langue", ["العربية", "Français"])

    # زر العودة لتغيير الدور من القائمة الجانبية
    if st.sidebar.button("🔄 تغيير نوع الحساب"):
        st.session_state.user_role = None
        st.rerun()

    if lang == "العربية":
        title_text = "🧁 مكارون الملوك الفاخر"
        subtitle_text = "ألذ وأفخم أنواع المكارون الحلزوني والفرنسي الأصلي المصنوع بخبرة عالية."
        admin_title = "🛠️ لوحة التحكم لإضافة منتج جديد (صانع الحلويات فقط)"
        prod_name_label = "اسم الحلوى أو النكهة:"
        prod_desc_label = "وصف المنتج:"
        prod_price_label = "الثمن (درهم مغربي):"
        img_upload_label = "اضغط هنا لاختيار صورة المنتج من جهازك أو اسحبها:"
        add_btn = "✨ إضافة المنتج للموقع"
        catalog_title = "🛍️ قائمة منتجاتنا الحالية"
        order_box_title = "🛒 اطلب الآن (سيتم إرسال طلبك مباشرة عبر واتساب)"
        client_name_label = "اسمك الكريم:"
        client_city_label = "مدينتك (للتوصيل في المغرب):"
        client_phone_label = "رقم هاتفك:"
        client_notes_label = "ملاحظات خاصة (مثلاً: نكهة إضافية، وقت التوصيل...):"
        order_btn = "📤 إرسال الطلب عبر واتساب"
        delivery_info_title = "🚚 معلومات التوصيل في المغرب"
        delivery_desc = """
        * التوصيل متوفر لكافة المدن المغربية.
        * تبدأ رسوم التوصيل **من 10 درهم إلى 60 درهم** حسب المدينة.
        * للتواصل المباشر مع المسؤول: **212671234418+**
        """
        whatsapp_order_number = "212611759969"
        support_phone = "212671234418"
    else:
        title_text = "🧁 Les Macarons Royaux"
        subtitle_text = "Les meilleurs macarons artisanaux faits avec passion et expertise."
        admin_title = "🛠️ Tableau de bord (Pâtissier uniquement)"
        prod_name_label = "Nom du produit / de la pâtisserie :"
        prod_desc_label = "Description du produit :"
        prod_price_label = "Prix (MAD) :"
        img_upload_label = "Télécharger l'image depuis votre appareil :"
        add_btn = "✨ Ajouter le produit"
        catalog_title = "🛍️ Notre Catalogue"
        order_box_title = "🛒 Commander (Envoi direct sur WhatsApp)"
        client_name_label = "Votre Nom :"
        client_city_label = "Votre Ville (Livraison au Maroc) :"
        client_phone_label = "Votre Téléphone :"
        client_notes_label = "Notes spéciales :"
        order_btn = "📤 Envoyer la commande via WhatsApp"
        delivery_info_title = "🚚 Informations de Livraison au Maroc"
        delivery_desc = """
        * Livraison disponible dans toutes les villes du Maroc.
        * Les frais de livraison varient **de 10 MAD à 60 MAD** selon la ville.
        * Contact direct : **+212671234418**
        """
        whatsapp_order_number = "212611759969"
        support_phone = "212671234418"

    st.title(title_text)
    st.write(subtitle_text)
    st.markdown("---")

    # زر واتساب جانبي سريع للتواصل
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"📞 **رقم التنسيق والتواصل:**\n`+{support_phone}`")
    st.sidebar.markdown(f"[مراسلة الدعم عبر الواتساب](https://wa.me/{support_phone})")

    # تخزين المنتجات في الذاكرة المؤقتة
    if 'products' not in st.session_state:
        st.session_state.products = []

    # لوحة التحكم تظهر حصرياً لصانع الحلويات (Admin)
    if st.session_state.user_role == "admin":
        st.sidebar.success("✅ أنت مسجل كـ صانع الحلويات (مفعل)")
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
                    st.success("تم رفع الصورة وإضافة المنتج بنجاح للقائمة!")
    else:
        st.sidebar.info("👤 أنت تصفح الموقع كـ زبون")

    st.markdown("---")
    st.subheader(catalog_title)

    # عرض المنتجات للجميع بشكل شبكي
    if not st.session_state.products:
        st.info("لا توجد منتجات مضافة حالياً. سيتم عرضها هنا بمجرد إضافتها من طرف إدارة المحل.")
    else:
        cols = st.columns(3)
        for index, prod in enumerate(st.session_state.products):
            col = cols[index % 3]
            with col:
                st.image(prod["image"], use_container_width=True)
                st.markdown(f"### {prod['name']}")
                st.write(prod['desc'])
                st.markdown(f"**السعر / Prix:** {prod['price']} درهم / MAD")
                st.markdown("---")

    # قسم الطلب عبر واتساب للرقم المطلوب
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
                # تجهيز رسالة الواتساب بالكامل
                message = f"*طلب جديد عبر موقع مكارون الملوك* 🧁\n\n" \
                          f"👤 *الاسم:* {c_name}\n" \
                          f"🏙️ *المدينة:* {c_city}\n" \
                          f"📞 *رقم الهاتف:* {c_phone}\n" \
                          f"📝 *ملاحظات:* {c_notes if c_notes else 'لا توجد ملاحظات'}"
                
                encoded_message = urllib.parse.quote(message)
                whatsapp_url = f"https://wa.me/{whatsapp_order_number}?text={encoded_message}"
                
                st.success(f"شكراً لك يا {c_name}! اضغط على الزر أدناه لإرسال طلبك مباشرة عبر واتساب:")
                st.markdown(f"### [👉 اضغط هنا لإرسال الطلب عبر الواتساب مباشرة]({whatsapp_url})", unsafe_allow_html=True)

    # قسم معلومات التوصيل
    st.markdown("---")
    st.subheader(delivery_info_title)
    st.markdown(delivery_desc)
