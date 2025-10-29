# schemas.py
from marshmallow import Schema, fields, EXCLUDE

# 基礎：Item/Store 的共同（最小）欄位
class PlainItemSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    id = fields.Int(dump_only=True)          # 通常 DB 是 Int
    name = fields.Str(required=True)
    price = fields.Float(required=True)

class PlainStoreSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    id = fields.Int(dump_only=True)          # 通常 DB 是 Int
    name = fields.Str(required=True)

class PlainTagSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()

# Update：用於 PUT/PATCH，欄位都非必填
class ItemUpdateSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    name = fields.Str()
    price = fields.Float()
    store_id = fields.Int()

# 完整的 Item：在 PlainItem 基礎上，補上 store 關聯
class ItemSchema(PlainItemSchema):
    # 載入時要有 store_id；回傳不顯示（load_only）
    store_id = fields.Int(required=True, load_only=True)
    # 回傳時顯示完整的 store（dump_only）
    store = fields.Nested(PlainStoreSchema(), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)

# 完整的 Store：在 PlainStore 基礎上，補上 items 關聯
class StoreSchema(PlainStoreSchema):
    # 回傳時顯示底下的 items（dump_only）
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)

class TagSchema(PlainTagSchema):
    store_id = fields.Int(load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)
    item = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)

class TagAndItemSchema(Schema):
    message = fields.Str()
    item = fields.Nested(ItemSchema)
    tag = fields.Nested(TagSchema)

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)

class UserRegisterSchema(UserSchema):
    email = fields.Str(required=True)