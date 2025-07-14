def save_persona_to_file(persona_text, username):
    """
    Saves the generated persona to a text file.
    Example filename: persona_kojied.txt
    """
    filename = f"output/persona_{username}.txt"

    # Make sure the output folder exists
    import os
    os.makedirs("output", exist_ok=True)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(persona_text)

    print(f"✅ Persona saved to {filename}")
