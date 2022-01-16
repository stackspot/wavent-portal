"""CreateProvidersTable Migration."""

from masoniteorm.migrations import Migration


class CreateProvidersTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("providers") as table:
            table.increments("id").primary()
            table.string("name", 128)
            table.string("email", 100).nullable()
            table.string("phone", 50).nullable()
            table.string("address", 150).nullable()
            table.text("description").nullable()
            table.string("logo").nullable()
            table.string("brand_image").nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("providers")
