"""UserTableSeeder Seeder."""
from app.models.User import User
from masoniteorm.seeds import Seeder


class UserTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        User.create(
            {
                "name": "Admin",
                "email": "Admin@example.com",
                "password": "secret",
                "phone": "+123456789",
            }
        )
