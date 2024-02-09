from pymongo import MongoClient

class Overlay:
    @staticmethod
    def save(name, type, position, size, content):
        try:
            # Connect to MongoDB
            cluster = MongoClient("mongodb+srv://abhinobbora6:Qwerty123@testing.0nfjjmp.mongodb.net/?retryWrites=true&w=majority")
            db = cluster['easy']
            col = db['go']

            overlay = {
                'name': name,
                'type': type,
                'position': position,
                'size': size,
                'content': content,
            }
            
            inserted_id = col.insert_one(overlay).inserted_id
            return str(inserted_id)
        except Exception as e:
            return str(e)  # Return the error message for debugging


    @staticmethod
    def find_by_id(col, id):
        return col.find_one({'id': id})

    # Implement other CRUD methods as needed

