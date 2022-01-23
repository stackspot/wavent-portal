"""CreateAppointmentServicePivotTable Migration."""

from masoniteorm.migrations import Migration


class CreateAppointmentServicePivotTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("appointment_service") as table:
            table.increments("id")
            table.unsigned("service_id").index()
            table.unsigned("appointment_id").index()
            table.foreign("service_id").references("id").on("services").on_delete("cascade")
            table.foreign("appointment_id").references("id").on("appointments").on_delete(
                "cascade"
            )
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop_table_if_exists("appointment_service")
