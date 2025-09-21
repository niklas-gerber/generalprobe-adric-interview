# Rechnungsprüfung (Beispiel-Aufgabe)

Ziel: Entwickeln Sie ein kleines Python-Programm zur Überprüfung von Rechnungsdaten.

## Daten
Die Datei `data/invoices.csv` enthält Rechnungspositionen mit den Spalten:

- invoice_id: Rechnungsnummer
- item: Artikelname
- quantity: Anzahl
- price: Einzelpreis
- total: Summe (laut Rechnung)

## Aufgabe
1. Laden Sie die CSV-Datei ein (mit `pandas`).
2. Berechnen Sie für jede Zeile `quantity * price` und vergleichen Sie das Ergebnis mit der angegebenen `total`.
3. Markieren Sie Abweichungen (z. B. mit einer zusätzlichen Spalte `is_correct`).
4. Speichern Sie das Ergebnis in einer neuen CSV-Datei `data/invoices_checked.csv`.

## Abgabe
- Lösung bitte **einmal als reines Python-Skript** (`main.py`).
- Und **einmal als Jupyter Notebook** (`solution.ipynb`).
- Schreiben Sie saubere, nachvollziehbare Kommentare.

