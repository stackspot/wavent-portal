"""CreateStaffsTable Migration."""

from masoniteorm.migrations import Migration


class CreateStaffsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("staffs") as table:
            table.increments("id")
            table.string("name", 128).nullable()
            table.string("email", 128).nullable()
            table.string("phone", 50).nullable()
            table.unsigned("account_id").index()
            table.foreign("account_id").references("id").on("accounts").on_delete("cascade")
            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop_table_if_exists("staffs")
