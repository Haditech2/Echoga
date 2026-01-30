import os
import cloudinary
import cloudinary.uploader
from django.core.management.base import BaseCommand
from django.conf import settings
from pathlib import Path


class Command(BaseCommand):
    help = 'Upload static images to Cloudinary'

    def handle(self, *args, **options):
        # Configure Cloudinary
        cloudinary.config(
            cloud_name=settings.CLOUDINARY_CLOUD_NAME,
            api_key=settings.CLOUDINARY_API_KEY,
            api_secret=settings.CLOUDINARY_API_SECRET,
            secure=True
        )

        # Define the static images directory
        static_images_dir = Path(settings.BASE_DIR) / 'static' / 'images'
        
        if not static_images_dir.exists():
            self.stdout.write(
                self.style.ERROR(f'Static images directory not found: {static_images_dir}')
            )
            return

        # Upload each image
        uploaded_count = 0
        failed_count = 0
        
        for image_file in static_images_dir.glob('*'):
            if image_file.is_file() and image_file.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.webp']:
                try:
                    # Upload to Cloudinary with folder structure
                    result = cloudinary.uploader.upload(
                        str(image_file),
                        folder="echoga_foundation/images",
                        public_id=image_file.stem,  # Use filename without extension as public_id
                        overwrite=True,
                        resource_type="image"
                    )
                    
                    self.stdout.write(
                        self.style.SUCCESS(
                            f'✅ Uploaded {image_file.name} -> {result["secure_url"]}'
                        )
                    )
                    uploaded_count += 1
                    
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f'❌ Failed to upload {image_file.name}: {str(e)}')
                    )
                    failed_count += 1

        # Summary
        self.stdout.write(
            self.style.SUCCESS(
                f'\n📊 Upload Summary:'
                f'\n✅ Successfully uploaded: {uploaded_count} images'
                f'\n❌ Failed uploads: {failed_count} images'
            )
        )
        
        if uploaded_count > 0:
            self.stdout.write(
                self.style.SUCCESS(
                    f'\n🌐 Your images are now available at:'
                    f'\nhttps://res.cloudinary.com/echoga/image/upload/echoga_foundation/images/[image-name]'
                )
            )