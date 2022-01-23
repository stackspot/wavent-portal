"""CreateServiceStaffPivotTable Migration."""

from masoniteorm.migrations import Migration


class CreateServiceStaffPivotTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("service_staff") as table:
            table.increments("id")
            table.unsigned("staff_id").index()
            table.unsigned("service_id")
            table.foreign("staff_id").references("id").on("staffs").on_delete("cascade")
            table.foreign("service_id").references("id").on("services").on_delete("cascade")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop_table_if_exists("service_staff")
