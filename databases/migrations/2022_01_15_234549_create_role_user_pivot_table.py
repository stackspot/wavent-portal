"""CreateRoleUserPivotTable Migration."""

from masoniteorm.migrations import Migration


class CreateRoleUserPivotTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("role_user") as table:
            table.increments("id")
            table.unsigned("user_id")
            table.unsigned("role_id")
            table.foreign("user_id").references("id").on("users").on_delete("cascade")
            table.foreign("role_id").references("id").on("roles").on_delete("cascade")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop_table_if_exists("role_user")
