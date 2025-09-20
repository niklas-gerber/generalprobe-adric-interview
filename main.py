import pandas as pd

# CSV einlesen
df = pd.read_csv("data/invoices.csv")

# Erwarteten Wert berechnen
df["expected_total"] = df["quantity"] * df["price"]

# Prüfen, ob korrekt
df["is_correct"] = df["expected_total"] == df["total"]

# Ergebnis ausgeben
print(df)

# Neue Datei speichern
df.to_csv("data/invoices_checked.csv", index=False)
