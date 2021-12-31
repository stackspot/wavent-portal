"""CreateServiceUserPivotTable Migration."""

from masoniteorm.migrations import Migration


class CreateServiceUserPivotTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("service_user") as table:
            table.increments("id")
            table.unsigned("service_id")
            table.unsigned("user_id")
            table.foreign("service_id").references("id").on("services").on_delete("cascade")
            table.foreign("user_id").references("id").on("users").on_delete("cascade")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("service_user")
