import streamlit as st

st.title("Praktikum Quiz")
st.header("Praktikum Würth IT")

# --- Session State Initialisierung ---
defaults = {
    "punkte": 0,
    "frage1_punkte": False,
    "frage2_punkte": False,
    "frage3_punkte": False,
    "frage4_punkte": False,
    "frage3_done": False,
}
for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# --- Frage 1 ---
st.subheader("1. Frage")
st.header("Was bedeutet LLM?")

antwort1 = st.radio(
    "",
    ["Logical Learning Machine", "Large Logic Module", "Large Language Model", "Local Language Memory"],
    key="frage1"
)

if st.button("Antwort 1 prüfen"):
    if not st.session_state.frage1_punkte:
        st.session_state.frage1_punkte = True
        if antwort1 == "Large Language Model":
            st.success("Richtig ✅ (+100 Punkte)")
            st.session_state.punkte += 100
        else:
            st.error("Falsch ❌ (-100 Punkte)")
            st.session_state.punkte -= 100

st.divider()

# --- Frage 2 ---
st.subheader("2. Frage")
st.header("Was sind Tokens?")

antwort2 = st.radio(
    "",
    [
        "Kleine Texteinheiten, die ein KI-Modell verarbeitet",
        "Digitale Münzen zur Bezahlung von KI",
        "Sicherheits-Codes zur Anmeldung",
        "Gespeicherte Antworten eines Modells"
    ],
    key="frage2"
)

if st.button("Antwort 2 prüfen"):
    if not st.session_state.frage2_punkte:
        st.session_state.frage2_punkte = True
        if antwort2 == "Kleine Texteinheiten, die ein KI-Modell verarbeitet":
            st.success("Richtig ✅ (+100 Punkte)")
            st.session_state.punkte += 100
        else:
            st.error("Falsch ❌ (-100 Punkte)")
            st.session_state.punkte -= 100

st.divider()

# --- Frage 3 ---
st.subheader("3. Frage")
st.header("Wie heißt die Programmiersprache?")
st.image("language-2024210_1280.png", caption="Beispielbild", width=300)

antwort3 = st.text_input("Wie heißt die Programmiersprache?", key="antwort3")

if st.button("Antwort 3 prüfen"):
    if not st.session_state.frage3_punkte:
        st.session_state.frage3_punkte = True
        if antwort3.strip().lower() == "python":
            st.success("Richtig ✅ (+100 Punkte)")
            st.session_state.punkte += 100
        else:
            st.error("Falsch ❌ (-100 Punkte)")
            st.session_state.punkte -= 100

st.divider()

# --- Frage 4 ---
st.subheader("4. Frage")
st.header("In der KI werden Daten als Vektoren dargestellt. Diese Vektoren liegen im ...")
st.image("78318-vector.png", caption="Beispielbild", width=300)

antwort4 = st.text_input("Antwort eingeben", key="antwort4")

if st.button("Antwort 4 prüfen"):
    if not st.session_state.frage4_punkte:
        st.session_state.frage4_punkte = True
        if antwort4.strip().lower() == "vektorraum":
            st.success("Richtig ✅ (+100 Punkte)")
            st.session_state.punkte += 100
        else:
            st.error("Falsch ❌ (-100 Punkte)")
            st.session_state.punkte -= 100
        st.session_state.frage3_done = True  # ✅ Wird jetzt korrekt gesetzt

# ✅ Lösung anzeigen
if st.session_state.frage3_done:
    with st.expander("✅ Lösung anzeigen"):
        st.write("**Vektorraum**")

st.divider()

# --- Ergebnis ---
st.header("🏁 Quiz beendet")
punkte = st.session_state.punkte
st.subheader(f"Dein Punktestand: {punkte}")

if punkte >= 300:
    st.success("🎉 Sehr gut bestanden!")
elif punkte >= 100:
    st.warning("🙂 Bestanden")
else:
    st.error("❌ Leider nicht bestanden")

# 🔄 Neustart
if st.button("🔄 Quiz neu starten"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()
