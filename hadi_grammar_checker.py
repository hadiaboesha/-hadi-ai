# @title هادي - النموذج الأولي الكامل { run: "auto" }

print("=" * 40)
print("🤖 هادي - مرشدك الذكي لإتقان الإنجليزية")
print("=" * 40 + "\n")

# --- بيانات المستخدم ---
name = "Hadi"  # @param {type:"string"}
language = "English"  # @param ["عربي", "English"]
level = "متقدم"  # @param ["مبتدئ", "متوسط", "متقدم"]

print("👤 المستخدم: " + name)
print("🌐 اللغة: " + language)
print("📊 المستوى: " + level)
print("\n" + "-" * 40 + "\n")

# --- قاموس الكلمات ---
basic_words = ["apple", "book", "school", "teacher", "student", "learn", "speak", "write", "read", "friend"]
intermediate_words = ["beautiful", "dangerous", "experience", "knowledge", "opportunity", "patience", "recommend", "struggle", "tradition", "wisdom"]
advanced_words = ["ambiguous", "benevolent", "conscientious", "detrimental", "exacerbate", "facetious", "gregarious", "hypothetical", "inevitable", "juxtapose"]

if level == "مبتدئ":
    word_list = basic_words
elif level == "متوسط":
    word_list = intermediate_words
else:
    word_list = advanced_words

# --- القسم 1: فحص كلمة ---
word = "Exacerbate"  # @param {type:"string"}

if language == "عربي":
    print("🔍 فحص كلمة: '" + word + "'")
    if word.lower() in word_list:
        print("✅ صحيح! '" + word + "' كلمة إنجليزية سليمة.\n")
    else:
        print("❌ '" + word + "' غير موجودة في قاموس مستواك الحالي.\n")
        print("📚 كلمات مستواك (" + level + "):")
        print(", ".join(word_list))

elif language == "English":
    print("🔍 Checking: '" + word + "'")
    if word.lower() in word_list:
        print("✅ Correct! '" + word + "' is a valid English word.\n")
    else:
        print("❌ '" + word + "' not found in your current level dictionary.\n")
        print("📚 Your level words (" + level + "):")
        print(", ".join(word_list))

# --- القسم 2: نصيحة هادي ---
print("\n" + "-" * 40 + "\n")

if language == "عربي":
    if level == "مبتدئ":
        print("💡 نصيحة هادي: ابدأ بالمفردات الأساسية. 15 دقيقة يومياً تكفي.")
    elif level == "متوسط":
        print("💡 نصيحة هادي: ركز على المحادثة وقواعد الأزمنة. شاهد فيديوهات مع ترجمة.")
    elif level == "متقدم":
        print("💡 نصيحة هادي: اقرأ مقالات أكاديمية وناقش مواضيع معقدة.")

elif language == "English":
    if level == "مبتدئ":
        print("💡 Hadi's Tip: Start with basic vocabulary. 15 mins/day is enough.")
    elif level == "متوسط":
        print("💡 Hadi's Tip: Focus on conversation and verb tenses.")
    elif level == "متقدم":
        print("💡 Hadi's Tip: Read academic articles and debate complex topics.")

print("\n" + "=" * 40)
print("🚀 هادي قيد التطوير... قريباً مع ذكاء اصطناعي حقيقي!")
