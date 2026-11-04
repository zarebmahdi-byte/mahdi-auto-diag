import obd

def connect_obd():
    """محاولة الاتصال بجهاز OBD2 الموصول بالسيارة"""
    print("جاري البحث عن جهاز التشخيص (OBD2)...")
    connection = obd.OBD() # يقوم بالبحث تلقائياً عن منفذ البلوتوث أو الـ USB الموصول

    if connection.is_connected():
        print("[نجاح] تم الاتصال بسيارة Golf 5 بنجاح!")
        return connection
    else:
        print("[تنبيه] لم يتم العثور على الجهاز. تأكد من وضع الكونتاكت وتشغيل البلوتوث/الربط.")
        return None

def read_real_dtc(connection):
    """قراءة أكواد الأعطال الحقيقية المخزنة في كمبيوتر السيارة"""
    if not connection:
        return []

    query_cmd = obd.commands.GET_DTC
    response = connection.query(query_cmd)

    if response.is_null():
        return []

    return response.value
