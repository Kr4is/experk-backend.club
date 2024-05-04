import os

from dotenv import load_dotenv
from supabase import Client, create_client

load_dotenv()
supabase_url: str = os.environ.get("SUPABASE_URL")
supabase_key: str = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(supabase_url, supabase_key)


def get_cities():
    response = supabase.table("cities").select("*").execute()
    return response.data


def get_experiences():
    response = supabase.table("experiences").select("*").execute()
    return response.data


# def create_url(url: str) -> str:

#     secret_key = secret_key_from_existing_url(url)
#     # supabase.table('cities').insert({"id": key, "secret_key": secret_key, "original_url": url}).execute()

#     return secret_key


# def get_url_by_key(url_key: str) -> str:

#     response = (
#         supabase.table("cities")
#         .select("original_url")
#         .eq("secret_key", url_key)
#         .execute()
#     )
#     if response.data:
#         print(response.data)
#         return response.data[0]["original_url"]

#     return None


# def secret_key_from_existing_url(url: str) -> str:

#     response = (
#         supabase.table("cities").select("secret_key").eq("original_url", url).execute()
#     )

#     if response.data:
#         return response.data[0]["secret_key"]

#     return None
