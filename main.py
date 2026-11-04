from obd_reader import connect_obd, read_real_dtc
from dtc_database import lookup_dtc
from dtc_helper import format_dtc_output

print("=== Mahdi Auto-Diag System Initialized ===")

# محاولة الاتصال بالسيارة عبر منفذ الـ OBD2
connection = connect_obd()

if connection:
    print("جاري فحص أكواد الأعطال المخزنة في السيارة...")
    codes = read_real_dtc(connection)
    
    if codes:
        for code in codes:
            desc = lookup_dtc(code)
            print(format_dtc_output(code, desc))
    else:
        print("[معلومة] لا توجد أكواد أعطال مسجلة (السيارة سليمة بحمد الله).")
else:
    # وضع تجريبي في حال لم يتم توصيل الجهاز حالياً للتأكد من عمل النظام
    test_code = "P0102"
    desc = lookup_dtc(test_code)
    print("\n[وضع محاكاة تجريبي]:")
    print(format_dtc_output(test_code, desc))
