"""CreateAppointmentsTable Migration."""

from masoniteorm.migrations import Migration


class CreateAppointmentsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("appointments") as table:
            table.increments("id").primary()
            table.datetime("start_time")
            table.datetime("finish_time")
            table.integer("client_id").nullable()
            table.integer("account_id").nullable()
            table.string("client_name", 128).nullable()
            table.string("client_email", 128).nullable()
            table.string("client_phone", 50).nullable()
            table.decimal("price", 10, 2)
            table.boolean("is_noshow").default(False)
            table.boolean("canceled").default(False)
            table.text("cancellation_reason").nullable()
            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("appointments")
