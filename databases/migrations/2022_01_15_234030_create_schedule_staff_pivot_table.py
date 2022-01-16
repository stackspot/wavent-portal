"""CreateScheduleStaffPivotTable Migration."""

from masoniteorm.migrations import Migration


class CreateScheduleStaffPivotTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("schedule_staff") as table:
            table.increments("id")
            table.unsigned("staff_id")
            table.unsigned("schedule_id")
            table.foreign("staff_id").references("id").on("staffs").on_delete("cascade")
            table.foreign("schedule_id").references("id").on("schedules").on_delete("cascade")
            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("schedule_staff")
