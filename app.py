import streamlit as st
from PIL import Image
import torch
import torchvision.transforms as transforms
import io

# =====================================================
# Streamlit Page Configuration (MUST be first)
# =====================================================
st.set_page_config(
    page_title="AI Image Super-Resolution",
    layout="centered"
)

# =====================================================
# Title & Aim (Aligned with Project Objective)
# =====================================================
st.title("🔍 AI Image Super-Resolution")

st.caption(
    "An AI-based application that enhances low-resolution images by "
    "reconstructing missing visual details using a pretrained deep learning model."
)

st.markdown("---")

# =====================================================
# Load AI Super-Resolution Model (Real-ESRGAN quality)
# =====================================================
@st.cache_resource
def load_model():
    """Load EDSR model for 4x super-resolution"""
    from super_image import EdsrModel
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = EdsrModel.from_pretrained('eugenesiow/edsr-base', scale=4)
    model = model.to(device)
    return model, device

# =====================================================
# AI Super-Resolution Function  
# =====================================================
def super_resolve(image: Image.Image) -> Image.Image:
    """
    AI-powered super-resolution using EDSR (Enhanced Deep Super-Resolution)
    - 4x upscaling with deep learning
    - Reconstructs realistic details and textures
    - Enhances facial features, edges, and fine details
    """
    model, device = load_model()
    
    # Convert PIL Image to tensor
    to_tensor = transforms.ToTensor()
    img_tensor = to_tensor(image).unsqueeze(0).to(device)
    
    # Run super-resolution
    with torch.no_grad():
        output_tensor = model(img_tensor)
    
    # Convert tensor back to PIL Image
    output_tensor = output_tensor.squeeze(0).cpu().clamp(0, 1)
    to_pil = transforms.ToPILImage()
    output = to_pil(output_tensor)
    
    return output

# =====================================================
# User Interface
# =====================================================
uploaded_file = st.file_uploader(
    "📤 Upload a low-resolution image",
    type=["jpg", "jpeg", "png"]
)

enhance_button = st.button("🚀 Enhance Image")

# =====================================================
# Processing Logic
# =====================================================
if uploaded_file and enhance_button:
    original_image = Image.open(uploaded_file).convert("RGB")

    st.subheader("Original Image")
    st.image(original_image, use_column_width=True)

    with st.spinner("Enhancing image resolution using AI..."):
        enhanced_image = super_resolve(original_image)

    st.subheader("Enhanced Image (Super-Resolved)")
    st.image(enhanced_image, use_column_width=True)

    # Download enhanced image
    buffer = io.BytesIO()
    enhanced_image.save(buffer, format="PNG")

    st.download_button(
        label="⬇️ Download Enhanced Image",
        data=buffer.getvalue(),
        file_name="super_resolved_image.png",
        mime="image/png"
    )

# =====================================================
# Footer
# =====================================================
st.markdown("---")
st.caption("Powered by EDSR (Enhanced Deep Super-Resolution) • PyTorch • Streamlit")
