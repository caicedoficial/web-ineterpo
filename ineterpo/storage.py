from django.core.files.storage import Storage
from django.conf import settings
from supabase import create_client
import os
import io

class SupabaseStorage(Storage):
    def __init__(self):
        self.supabase = create_client(
            settings.SUPABASE_URL,
            settings.SUPABASE_KEY
        )
        self.bucket_name = settings.SUPABASE_BUCKET_NAME

    def _save(self, name, content):
        file_data = content.read()
        
        self.supabase.storage.from_(self.bucket_name).upload(
            path=name,
            file=file_data,
            file_options={"contentType": content.content_type}
        )
        
        return name

    def _open(self, name, mode='rb'):
        response = self.supabase.storage.from_(self.bucket_name).download(name)
        return io.BytesIO(response)

    def url(self, name):
        return self.supabase.storage.from_(self.bucket_name).get_public_url(name)

    def exists(self, name):
        try:
            files = self.supabase.storage.from_(self.bucket_name).list()
            return any(file['name'] == name for file in files)
        except Exception:
            return False

    def delete(self, name):
        try:
            self.supabase.storage.from_(self.bucket_name).remove([name])
        except Exception:
            pass