from dtc_database import lookup_dtc
from dtc_helper import format_dtc_output

print("=== Mahdi Auto-Diag System Initialized ===")

# تجربة فحص كود تجريبي
test_code = "P0102"
desc = lookup_dtc(test_code)
print(format_dtc_output(test_code, desc))
