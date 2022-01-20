"""CreatePermissionRolePivotTable Migration."""

from masoniteorm.migrations import Migration


class CreatePermissionRolePivotTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("permission_role") as table:
            table.increments("id")
            table.unsigned("role_id")
            table.unsigned("permission_id")
            table.foreign("role_id").references("id").on("roles").on_delete("cascade")
            table.foreign("permission_id").references("id").on("permissions").on_delete("cascade")
            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("permission_role")
