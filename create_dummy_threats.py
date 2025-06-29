import os

def create_dummy_threats(folder_path):
    # Create ransom note
    with open(os.path.join(folder_path, "READ_ME_TO_RECOVER.txt"), 'w') as f:
        f.write("== YOUR FILES ARE ENCRYPTED ==\nSend 1 BTC to recover.")

    # Create .locked file
    with open(os.path.join(folder_path, "important_data.locked"), 'w') as f:
        f.write("[fake encrypted data]")

    # Create decrypt-named file
    with open(os.path.join(folder_path, "how_to_decrypt_instructions.docx"), 'w') as f:
        f.write("Fake document content")

    # Create fake executable
    with open(os.path.join(folder_path, "recover_my_files.exe"), 'w') as f:
        f.write("[malware placeholder]")

    print(f"\n✅ Created dummy threat files in '{folder_path}'")

if __name__ == "__main__":
    target = input("Enter folder path to create dummy threat files:\n> ").strip()
    if not os.path.isdir(target):
        print("❌ Invalid folder path")
    else:
        create_dummy_threats(target)