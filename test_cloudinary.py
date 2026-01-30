import cloudinary
import cloudinary.uploader

# Test Cloudinary configuration
def test_cloudinary():
    try:
        # Configure Cloudinary
        cloudinary.config(
            cloud_name="dafag8jhg",
            api_key="256576913286665",
            api_secret="ZFZAXBI3oXwo-y64FA9dY0p2RPo",
            secure=True
        )
        
        # Test the connection by trying a simple upload test
        print("🔄 Testing Cloudinary connection...")
        
        # Create a simple test image data
        import io
        from PIL import Image
        
        # Create a small test image
        img = Image.new('RGB', (100, 100), color='red')
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='PNG')
        img_bytes.seek(0)
        
        # Try to upload the test image
        result = cloudinary.uploader.upload(
            img_bytes.getvalue(),
            public_id="test_connection",
            folder="test",
            overwrite=True
        )
        
        print("✅ Cloudinary connection successful!")
        print(f"Test image URL: {result['secure_url']}")
        
        # Clean up test image
        cloudinary.uploader.destroy("test/test_connection")
        print("🧹 Test image cleaned up")
        
        return True
        
    except Exception as e:
        print(f"❌ Cloudinary connection failed: {str(e)}")
        return False

if __name__ == "__main__":
    test_cloudinary()