import streamlit as st
import hashlib
import pandas as pd
import base64
import os

HASH_ALGORITHMS = [
    "md5", "sha1", "sha256", "sha384", "sha512", "sha3_256", "sha3_384", "sha3_512"
]

def calculate_hashes(file):
    file_data = file.read()
    file.seek(0)  # Reset file pointer
    hashes = {algo: hashlib.new(algo, file_data).hexdigest() for algo in HASH_ALGORITHMS}
    return hashes

def export_hashes(file_name, file_size, file_type, hashes):
    base_name = os.path.splitext(file_name)[0]  # Remove extension
    csv_filename = f"{base_name}_hashes.csv"
    data = {
        "Name": file_name,
        "File Size": f"{file_size} bytes",
        "File Type": file_type
    }
    data.update(hashes)
    df = pd.DataFrame([data])
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{csv_filename}">Download Hashes</a>'
    return href

st.title("File Hashing and Validation Utility")

tab1, tab2 = st.tabs(["Generate Hashes", "Verify Hash"])

with tab1:
    st.header("Generate File Hashes")
    uploaded_file = st.file_uploader("Upload a file to hash", type=None)
    if uploaded_file is not None:
        file_name = uploaded_file.name
        file_size = len(uploaded_file.getvalue())
        file_type = uploaded_file.type
        hashes = calculate_hashes(uploaded_file)
        
        st.write(f"### File Name: {file_name}")
        st.write(f"### File Size: {file_size} bytes")
        st.write(f"### File Type: {file_type}")
        
        for algo, hash_value in hashes.items():
            st.write(f"### {algo.upper()}:")
            st.code(hash_value, language="plaintext")
        
        st.markdown(export_hashes(file_name, file_size, file_type, hashes), unsafe_allow_html=True)

with tab2:
    st.header("Verify File Hash")
    user_hash = st.text_input("Enter file hash for comparison")
    
    # Display supported hashes in smaller red font
    st.markdown(
        "<p style='color: red; font-size: 12px;'>Supported Hashes: MD5, SHA-1, SHA-256, SHA-384, SHA-512, SHA3-256, SHA3-384, SHA3-512</p>", 
        unsafe_allow_html=True
    )
    
    file_to_verify = st.file_uploader("Upload file to verify", type=None)
    
    if file_to_verify and user_hash:
        computed_hashes = calculate_hashes(file_to_verify)
        match_found = False
        for algo, computed_hash in computed_hashes.items():
            if computed_hash == user_hash:
                st.success(f"✅ Found a file hash match: {algo.upper()}\n{computed_hash}")
                match_found = True
                break
        if not match_found:
            st.error("❌ No matching hash found.")
