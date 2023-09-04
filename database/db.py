import motor.motor_asyncio

class DBManager:
    def __init__(self, database_name, collection_name):
        self.client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
        print(self.client)
        self.database = self.client[database_name]
        print(self.database)
        self.collection = self.database[collection_name]
        print(self.collection)

    async def find_by_nickname(self, nickname):
        user = await self.collection.find_one({'nickname': nickname})
        return user

    async def delete_by_nickname(self, nickname):
        result = await self.collection.delete_one({'nickname': nickname})
        return result.deleted_count

    async def add_user(self, user_data):
        result = await self.collection.insert_one(user_data)
        return str(result.inserted_id)

    async def update_field_by_nickname(self, nickname, field_to_update, new_value, transformation_func):
        user = await self.collection.find_one({'nickname': nickname})
        if user:
            updated_value = transformation_func(user.get(field_to_update), new_value)
            update_result = await self.collection.update_one(
                {'nickname': nickname},
                {'$set': {field_to_update: updated_value}}
            )
            return update_result.modified_count
        return 0