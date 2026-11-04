# Mahdi Auto-Diag - DTC Database
DTC_DATABASE = {
    "P0102": "Mass Air Flow (MAF) Circuit Low Input",
    "P0301": "Cylinder 1 Misfire Detected",
    "P0299": "Turbocharger Underboost Condition",
    "P0420": "Catalyst System Efficiency Below Threshold"
}

def lookup_dtc(code):
    return DTC_DATABASE.get(code.upper(), "Unknown Diagnostic Trouble Code")
