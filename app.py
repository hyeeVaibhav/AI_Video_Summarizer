import streamlit as st
import os
from main import video_to_summary

st.title("AI Video Summarizer")

uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mkv", "mov"])

if uploaded_file is not None:
    st.video(uploaded_file)
    
    if st.button("Summarize Video"):
        with st.spinner("Processing video... This may take a few minutes depending on your CPU."):
            # Save uploaded file temporarily
            temp_video_path = "temp_uploaded_video.mp4"
            with open(temp_video_path, "wb") as f:
                f.write(uploaded_file.read())
            
            try:
                # Run the pipeline
                summary = video_to_summary(temp_video_path, use_chunking=True)
                st.success("Summarization Complete!")
                st.write("### Summary")
                
                # Format the continuous summary into bullet points
                sentences = [sentence.strip() for sentence in summary.split('.') if sentence.strip()]
                for sentence in sentences:
                    st.markdown(f"* {sentence}.")
                    
            except Exception as e:
                st.error(f"An error occurred: {e}")
            finally:
                # Clean up the uploaded video
                if os.path.exists(temp_video_path):
                    os.remove(temp_video_path)



                    ###conda activate video_summarizer
                    ### streamlit run app.py