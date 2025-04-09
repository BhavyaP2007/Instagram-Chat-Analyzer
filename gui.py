import streamlit as st
import zipfile
import tempfile
import os
from pathlib import Path
import mainfile
# Upload ZIP file
if "count" not in st.session_state:
    st.session_state.count = 0
if st.session_state.count == 0:  
    st.write("Made after multiple headaches by 12th grader Bhavya")  
    st.title("📂 Upload a Folder as ZIP")
    uploaded_zip = st.file_uploader("Upload a zipped folder", type="zip")

    if uploaded_zip is not None:
        # Create a temporary directory
        temp_dir = tempfile.TemporaryDirectory()
        
        # Save and extract zip contents
        zip_path = os.path.join(temp_dir.name, "uploaded.zip")
        with open(zip_path, "wb") as f:
            f.write(uploaded_zip.read())

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir.name)    
        zip_path = str(zip_path)[:-12].replace("\\","/")+"/"
        for f1 in Path(zip_path).iterdir():
            if "your_instagram_activity" in str(f1):
                zip_path = str(f1).replace("\\","/")+"/messages/inbox"
                break
        print("\n\n\n\n",zip_path) 
        destination = mainfile.root_dir+"/collected_data"
        os.makedirs(destination,exist_ok=True)
        data = mainfile.zip_check(zip_path)
        st.success("ZIP file extracted successfully!")
        with st.expander("💬 Suspicious Messages", expanded=True):
            st.dataframe(data[0].iloc[:,[0,4]], use_container_width=True)     
            csv1 = data[0].to_csv(destination+"/messages.csv",index=False)

    # Collapsible Section: Photos

        if not data[1].empty:
            with st.expander("🖼️ Suspicious Photos", expanded=False):
                st.dataframe(data[1], use_container_width=True)
                csv2 = data[1].to_csv(destination+"/photos.csv",index=False)


    # Collapsible Section: Videos
        if not data[2].empty:
            with st.expander("🎥 Suspicious Videos", expanded=False):
                st.dataframe(data[2], use_container_width=True)
                csv3 = data[2].to_csv(destination+"/videos.csv",index=False)
        os.startfile(destination)                 
else:
    final = "Data Stored In Files at "+str(mainfile.root_dir+"/collected_data")
    st.title(final)