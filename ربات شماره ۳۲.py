# === بارگذاری داده‌ها هنگام شروع ربات ===
qa_data = load_qa_data()
welcomed_members_cache = load_welcomed_members()
group_rules = load_group_rules()

# کش ساده برای وضعیت عضویت کاربران در کانال‌های جوین اجباری تا فشار به API کم شود
# ساختار: { user_guid: { channel_id: bool } }
force_join_membership_cache = {}

# جلوگیری از ارسال تکراری پیام راهنما برای جوین اجباری در هر چت
# ساختار: set((chat_id, user_guid))
force_join_notified_users = set()

# بارگذاری کانفیگ اصلی (شامل ادمین‌ها و تنظیمات گروه‌ها)
config = load_config()
ADMIN_IDS = config["admin_ids"]
DEFAULT_CHANNEL_ID = config["default_channel_id"]
OPENWEATHER_API_KEY = config["openweathermap_api_key"]