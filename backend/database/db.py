from supabase import create_client
from app.config import settings

# Create a Supabase client
supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

async def init_db():
    # Test connection to Supabase
    try:
        response = supabase.table("posts").select("*").limit(1).execute()
        if response.data:
            print("✅ Connected to Supabase!")
        else:
            print("⚠️ Connected but no data found.")
    except Exception as e:
        print(f"❌ Failed to connect to Supabase: {e}")
