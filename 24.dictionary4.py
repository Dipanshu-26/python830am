
# dict.fromkeys() - is used to create a new dictionary using:
#     * A sequence of keys
#     * One default value for all keys

# Syntax
    # dict.fromkeys(keys, default_value)
        # * keys → list/tuple/string/set (any iterable)
        # * default_value → value assigned to all keys
        # (default is None if not provided)

#creating dictionary with keys
keys = ["name","age","city"]
info=dict.fromkeys(keys)
print(info)

info["name"]="dipnashu"
print(info)

dict1=dict.fromkeys("abc",0)
print(dict1)

key = ["abc"]
dict2=dict.fromkeys(key,0)
print(dict2)