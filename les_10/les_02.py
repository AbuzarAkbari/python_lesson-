while True:
    try:
        perUur = float(input("Wat verdien je per uur: "))
        hvlUur = float(input("Hoeveel uur heb je gewerkt: "))

        print(hvlUur, "uur werken levert ", perUur*hvlUur, " Euro op")
        break
    except ValueError:
        print("voer een cijfer in")
