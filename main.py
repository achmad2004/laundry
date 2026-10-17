
import questionary

layanan = questionary.select(
    "Pilih layanan laundry:",
    choices=[
        "Cuci Kering",
        "Cuci Setrika",
        "Setrika Saja"
    ]
).ask()

print("Layanan dipilih:", layanan)
