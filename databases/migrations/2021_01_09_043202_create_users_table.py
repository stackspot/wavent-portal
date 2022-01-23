from masoniteorm.migrations import Migration


class CreateUsersTable(Migration):
    def up(self):
        """Run the migrations."""
        with self.schema.create("users") as table:
            table.increments("id").primary()
            table.string("name", 128)
            table.string("email").unique()
            table.string("password")
            table.boolean("is_active").default(False)
            table.boolean("is_admin").default(False)
            table.string("remember_token").nullable()
            table.string("phone", 50).nullable()
            table.timestamp("verified_at").nullable()
            table.timestamps()
            table.soft_deletes()

    def down(self):
        """Revert the migrations."""
        self.schema.drop_table_if_exists("users")
